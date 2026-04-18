"use client";

import React, { useEffect, useRef } from "react";

type SourceHints = {
  file?: string;
  component?: string;
  routeHint?: string;
  source?: string;
  mapKey?: string;
};

type TargetPayload = {
  tag: string;
  selector: string;
  xpath: string;
  textPreview?: string;
  dataTestId?: string;
  id?: string;
  role?: string;
  name?: string;
  rect?: {
    x: number;
    y: number;
    width: number;
    height: number;
    top: number;
    right: number;
    bottom: number;
    left: number;
  };
  sourceHints?: SourceHints;
};

type Payload = {
  page: {
    route: string;
  };
  target?: TargetPayload;
  targets?: TargetPayload[];
};

type Props = {
  children: React.ReactNode;
  enabled?: boolean;
};

export default function LlmInspectorOverlay({
  children,
  enabled = process.env.NODE_ENV === "development",
}: Props) {
  const hoverOverlayRef = useRef<HTMLDivElement | null>(null);
  const labelRef = useRef<HTMLDivElement | null>(null);
  const selectedLayerRef = useRef<HTMLDivElement | null>(null);
  const toastTimeoutRef = useRef<number | null>(null);
  const currentElRef = useRef<Element | null>(null);
  const selectedElsRef = useRef<Element[]>([]);
  const altHeldRef = useRef(false);

  useEffect(() => {
    if (!enabled) return;

    const hoverOverlay = document.createElement("div");
    hoverOverlayRef.current = hoverOverlay;
    Object.assign(hoverOverlay.style, {
      position: "fixed",
      zIndex: "2147483646",
      pointerEvents: "none",
      border: "2px solid #00ff88",
      background: "rgba(0,255,136,0.08)",
      boxSizing: "border-box",
      display: "none",
      borderRadius: "4px",
    } satisfies Partial<CSSStyleDeclaration>);

    const selectedLayer = document.createElement("div");
    selectedLayerRef.current = selectedLayer;
    Object.assign(selectedLayer.style, {
      position: "fixed",
      inset: "0",
      zIndex: "2147483645",
      pointerEvents: "none",
    } satisfies Partial<CSSStyleDeclaration>);

    const label = document.createElement("div");
    labelRef.current = label;
    Object.assign(label.style, {
      position: "fixed",
      zIndex: "2147483647",
      pointerEvents: "none",
      background: "#111",
      color: "#00ff88",
      font: "12px/1.4 monospace",
      padding: "6px 8px",
      borderRadius: "6px",
      maxWidth: "560px",
      whiteSpace: "nowrap",
      overflow: "hidden",
      textOverflow: "ellipsis",
      display: "none",
      boxShadow: "0 4px 12px rgba(0,0,0,0.35)",
    } satisfies Partial<CSSStyleDeclaration>);

    document.body.appendChild(selectedLayer);
    document.body.appendChild(hoverOverlay);
    document.body.appendChild(label);

    function clearToastTimeout() {
      if (toastTimeoutRef.current) {
        window.clearTimeout(toastTimeoutRef.current);
        toastTimeoutRef.current = null;
      }
    }

    function showLabelText(text: string) {
      const labelEl = labelRef.current;
      if (!labelEl) return;
      labelEl.textContent = text;
      labelEl.style.display = "block";
    }

    function hideLabel() {
      const labelEl = labelRef.current;
      if (!labelEl) return;
      labelEl.style.display = "none";
    }

    function positionLabel(rect: DOMRect) {
      const labelEl = labelRef.current;
      if (!labelEl) return;
      labelEl.style.left = `${Math.max(8, rect.left)}px`;
      labelEl.style.top = `${Math.max(8, rect.top - 32)}px`;
    }

    function setSelectionDisabled(disabled: boolean) {
      document.documentElement.style.userSelect = disabled ? "none" : "";
      (
        document.documentElement.style as CSSStyleDeclaration & {
          webkitUserSelect?: string;
          msUserSelect?: string;
        }
      ).webkitUserSelect = disabled ? "none" : "";
      (
        document.documentElement.style as CSSStyleDeclaration & {
          webkitUserSelect?: string;
          msUserSelect?: string;
        }
      ).msUserSelect = disabled ? "none" : "";
    }

    function clearNativeSelection() {
      window.getSelection()?.removeAllRanges();
    }

    function getBestText(el: Element): string {
      const text = ((el as HTMLElement).innerText || el.textContent || "")
        .replace(/\s+/g, " ")
        .trim();

      return text.slice(0, 220);
    }

    function getAccessibleName(el: Element): string | undefined {
      const ariaLabel = el.getAttribute("aria-label");
      if (ariaLabel?.trim()) return ariaLabel.trim();

      const labelledBy = el.getAttribute("aria-labelledby");
      if (labelledBy) {
        const joined = labelledBy
          .split(/\s+/)
          .map((id) => document.getElementById(id)?.textContent?.trim() || "")
          .filter(Boolean)
          .join(" ")
          .trim();

        if (joined) return joined.slice(0, 160);
      }

      const htmlEl = el as HTMLInputElement | HTMLTextAreaElement | HTMLElement;
      const value =
        "value" in htmlEl && typeof htmlEl.value === "string"
          ? htmlEl.value.trim()
          : "";

      if (value) return value.slice(0, 160);

      const text = getBestText(el);
      if (text) return text.slice(0, 160);

      return undefined;
    }

    function isLikelyGeneratedClass(className: string) {
      if (className.startsWith("css-")) return true;
      if (className.startsWith("jsx-")) return true;
      if (className.startsWith("_")) return true;
      if (/^[A-Za-z0-9_-]{20,}$/.test(className)) return true;
      return false;
    }

    function cssPath(el: Element | null): string {
      if (!(el instanceof Element)) return "";

      const parts: string[] = [];
      let node: Element | null = el;

      while (node && node.nodeType === 1 && node !== document.body) {
        let part = node.nodeName.toLowerCase();

        const nodeId = (node as HTMLElement).id;
        if (nodeId) {
          part += `#${CSS.escape(nodeId)}`;
          parts.unshift(part);
          break;
        }

        const classes = Array.from(node.classList).filter(
          (c) => !isLikelyGeneratedClass(c)
        );

        if (classes.length) {
          part += classes
            .slice(0, 2)
            .map((c) => `.${CSS.escape(c)}`)
            .join("");
        }

        const parent = node.parentElement;
        if (parent) {
          const sameTagSiblings = Array.from(parent.children).filter(
            (child) => child.nodeName === node?.nodeName
          );

          if (sameTagSiblings.length > 1) {
            part += `:nth-of-type(${sameTagSiblings.indexOf(node) + 1})`;
          }
        }

        parts.unshift(part);
        node = node.parentElement;
      }

      return parts.join(" > ");
    }

    function xpath(el: Element | null): string {
      if (!(el instanceof Element)) return "";

      const parts: string[] = [];
      let node: Element | null = el;

      while (node && node.nodeType === 1) {
        let index = 1;
        let sib = node.previousElementSibling;

        while (sib) {
          if (sib.nodeName === node.nodeName) index++;
          sib = sib.previousElementSibling;
        }

        parts.unshift(`${node.nodeName.toLowerCase()}[${index}]`);
        node = node.parentElement;
      }

      return `/${parts.join("/")}`;
    }

    function getStableSelector(el: Element): string {
      const dataTestId = el.getAttribute("data-testid");
      if (dataTestId) {
        return `${el.tagName.toLowerCase()}[data-testid="${CSS.escape(dataTestId)}"]`;
      }

      const nodeId = (el as HTMLElement).id;
      if (nodeId) {
        return `${el.tagName.toLowerCase()}#${CSS.escape(nodeId)}`;
      }

      const ariaLabel = el.getAttribute("aria-label");
      if (ariaLabel) {
        return `${el.tagName.toLowerCase()}[aria-label="${CSS.escape(ariaLabel)}"]`;
      }

      const name = el.getAttribute("name");
      if (name) {
        return `${el.tagName.toLowerCase()}[name="${CSS.escape(name)}"]`;
      }

      const classes = Array.from(el.classList).filter(
        (c) => !isLikelyGeneratedClass(c)
      );

      if (classes.length) {
        return `${el.tagName.toLowerCase()}${classes
          .slice(0, 2)
          .map((c) => `.${CSS.escape(c)}`)
          .join("")}`;
      }

      return cssPath(el);
    }

    function getSourceHintsObject(el: Element): SourceHints | undefined {
      let node: Element | null = el;
      const out: SourceHints = {};

      while (node && node !== document.documentElement) {
        out.file ||= node.getAttribute("data-file") || undefined;
        out.component ||= node.getAttribute("data-component") || undefined;
        out.routeHint ||= node.getAttribute("data-route") || undefined;
        out.source ||= node.getAttribute("data-source") || undefined;
        out.mapKey ||= node.getAttribute("data-map-key") || undefined;
        node = node.parentElement;
      }

      return Object.keys(out).length ? out : undefined;
    }

    function compact<T extends Record<string, unknown>>(obj: T): T {
      const entries = Object.entries(obj).filter(([, value]) => {
        if (value == null) return false;
        if (typeof value === "string" && value.trim() === "") return false;
        if (Array.isArray(value) && value.length === 0) return false;
        if (
          typeof value === "object" &&
          !Array.isArray(value) &&
          Object.keys(value as object).length === 0
        ) {
          return false;
        }
        return true;
      });

      return Object.fromEntries(entries) as T;
    }

    function buildTarget(el: Element): TargetPayload {
      const rect = el.getBoundingClientRect();
      const textPreview = getBestText(el);
      const dataTestId = el.getAttribute("data-testid") || undefined;
      const id = (el as HTMLElement).id || undefined;
      const role = el.getAttribute("role") || undefined;
      const name = getAccessibleName(el);
      const sourceHints = getSourceHintsObject(el);

      return compact({
        tag: el.tagName.toLowerCase(),
        selector: getStableSelector(el),
        xpath: xpath(el),
        textPreview: textPreview || undefined,
        dataTestId,
        id,
        role,
        name,
        rect: {
          x: Math.round(rect.x),
          y: Math.round(rect.y),
          width: Math.round(rect.width),
          height: Math.round(rect.height),
          top: Math.round(rect.top),
          right: Math.round(rect.right),
          bottom: Math.round(rect.bottom),
          left: Math.round(rect.left),
        },
        sourceHints,
      });
    }

    function buildPayload(elements: Element[]): Payload {
      const route = `${window.location.pathname}${window.location.search}${window.location.hash}`;
      const targets = elements.map(buildTarget);

      if (targets.length === 1) {
        return {
          page: {
            route,
          },
          target: targets[0],
        };
      }

      return {
        page: {
          route,
        },
        targets,
      };
    }

    function getLabelText(el: Element): string {
      const dataTestId = el.getAttribute("data-testid");
      if (dataTestId) return `[data-testid="${dataTestId}"]`;

      const nodeId = (el as HTMLElement).id;
      if (nodeId) return `#${nodeId}`;

      const name = getAccessibleName(el);
      if (name) return `${el.tagName.toLowerCase()} · ${name}`;

      return getStableSelector(el);
    }

    function renderSelectedOverlays() {
      const layer = selectedLayerRef.current;
      if (!layer) return;

      layer.innerHTML = "";

      for (const el of selectedElsRef.current) {
        if (!document.contains(el)) continue;

        const rect = el.getBoundingClientRect();
        const box = document.createElement("div");

        Object.assign(box.style, {
          position: "fixed",
          left: `${rect.left}px`,
          top: `${rect.top}px`,
          width: `${rect.width}px`,
          height: `${rect.height}px`,
          border: "2px solid #3b82f6",
          background: "rgba(59,130,246,0.14)",
          boxSizing: "border-box",
          borderRadius: "4px",
          pointerEvents: "none",
        } satisfies Partial<CSSStyleDeclaration>);

        layer.appendChild(box);
      }
    }

    function drawHover(el: Element) {
      const hoverOverlay = hoverOverlayRef.current;
      if (!hoverOverlay) return;

      const rect = el.getBoundingClientRect();
      hoverOverlay.style.display = "block";
      hoverOverlay.style.left = `${rect.left}px`;
      hoverOverlay.style.top = `${rect.top}px`;
      hoverOverlay.style.width = `${rect.width}px`;
      hoverOverlay.style.height = `${rect.height}px`;

      showLabelText(getLabelText(el));
      positionLabel(rect);
    }

    function hideHover() {
      const hoverOverlay = hoverOverlayRef.current;
      if (hoverOverlay) hoverOverlay.style.display = "none";
    }

    function isIgnoredElement(el: Element | null) {
      return (
        el === hoverOverlayRef.current ||
        el === labelRef.current ||
        el === selectedLayerRef.current
      );
    }

    function isSelected(el: Element) {
      return selectedElsRef.current.includes(el);
    }

    function toggleSelected(el: Element) {
      if (isSelected(el)) {
        selectedElsRef.current = selectedElsRef.current.filter((x) => x !== el);
      } else {
        selectedElsRef.current = [...selectedElsRef.current, el];
      }
      renderSelectedOverlays();
    }

    function setSingleSelected(el: Element) {
      selectedElsRef.current = [el];
      renderSelectedOverlays();
    }

    function clearAllSelections() {
      selectedElsRef.current = [];
      renderSelectedOverlays();
    }

    async function writeTextWithFallback(text: string): Promise<void> {
      const clipboardAvailable =
        typeof navigator !== "undefined" &&
        !!navigator.clipboard &&
        typeof navigator.clipboard.writeText === "function";

      if (clipboardAvailable && document.hasFocus() && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
        return;
      }

      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.setAttribute("readonly", "true");
      textarea.setAttribute("aria-hidden", "true");

      Object.assign(textarea.style, {
        position: "fixed",
        top: "0",
        left: "-9999px",
        width: "1px",
        height: "1px",
        opacity: "0",
        pointerEvents: "none",
      } satisfies Partial<CSSStyleDeclaration>);

      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      textarea.setSelectionRange(0, textarea.value.length);

      let copied = false;

      try {
        copied = document.execCommand("copy");
      } catch {
        copied = false;
      } finally {
        document.body.removeChild(textarea);
      }

      if (copied) return;

      console.log("LLM inspector payload (clipboard fallback failed):", text);

      const promptResult = window.prompt(
        "Clipboard access failed. Copy this payload manually:",
        text
      );

      if (promptResult === null) {
        throw new Error("Clipboard copy failed because the document was not focused.");
      }
    }

    async function copyPayload(
      elements: Element[],
      anchorEl?: Element,
      message?: string
    ) {
      if (!elements.length) return;

      const payload = buildPayload(elements);
      const text = JSON.stringify(payload, null, 2);

      await writeTextWithFallback(text);
      console.log("Copied LLM inspector payload:", payload);

      clearToastTimeout();

      if (anchorEl) {
        const rect = anchorEl.getBoundingClientRect();
        showLabelText(
          message ||
            (elements.length > 1
              ? `Copied multi-select payload (${elements.length} elements)`
              : "Copied LLM payload to clipboard")
        );
        positionLabel(rect);
      } else {
        showLabelText(
          message ||
            (elements.length > 1
              ? `Copied multi-select payload (${elements.length} elements)`
              : "Copied LLM payload to clipboard")
        );
      }

      toastTimeoutRef.current = window.setTimeout(() => {
        if (currentElRef.current && altHeldRef.current) {
          const currentRect = currentElRef.current.getBoundingClientRect();
          showLabelText(getLabelText(currentElRef.current));
          positionLabel(currentRect);
        } else {
          hideLabel();
        }
      }, 1200);
    }

    function onMouseDown(e: MouseEvent) {
      if (!e.altKey) return;

      e.preventDefault();
      e.stopPropagation();
      clearNativeSelection();
      window.focus();
    }

    function onMouseMove(e: MouseEvent) {
      altHeldRef.current = e.altKey;

      if (!e.altKey) {
        currentElRef.current = null;
        clearToastTimeout();
        hideHover();
        hideLabel();
        clearAllSelections();
        setSelectionDisabled(false);
        clearNativeSelection();
        return;
      }

      const el = document.elementFromPoint(e.clientX, e.clientY);
      if (!el || isIgnoredElement(el)) {
        currentElRef.current = null;
        hideHover();
        hideLabel();
        return;
      }

      currentElRef.current = el;
      drawHover(el);
    }

    function onScrollOrResize() {
      if (
        currentElRef.current &&
        document.contains(currentElRef.current) &&
        altHeldRef.current
      ) {
        drawHover(currentElRef.current);
      } else {
        hideHover();
      }

      selectedElsRef.current = selectedElsRef.current.filter((el) =>
        document.contains(el)
      );
      renderSelectedOverlays();
    }

    function onClick(e: MouseEvent) {
      if (!e.altKey) return;

      const el = document.elementFromPoint(e.clientX, e.clientY);
      if (!el || isIgnoredElement(el)) return;

      e.preventDefault();
      e.stopPropagation();
      e.stopImmediatePropagation();
      clearNativeSelection();
      window.focus();

      if (e.shiftKey) {
        toggleSelected(el);

        void copyPayload(
          selectedElsRef.current,
          el,
          isSelected(el)
            ? `Selected ${selectedElsRef.current.length} element${selectedElsRef.current.length === 1 ? "" : "s"}`
            : `Deselected · ${selectedElsRef.current.length} remaining`
        ).catch((error) => {
          console.error("Failed to copy LLM inspector payload:", error);
          showLabelText("Copy failed · payload logged");
        });

        return;
      }

      setSingleSelected(el);

      void copyPayload([el], el).catch((error) => {
        console.error("Failed to copy LLM inspector payload:", error);
        showLabelText("Copy failed · payload logged");
      });
    }

    function onKeyDown(e: KeyboardEvent) {
      if (e.key === "Alt") {
        altHeldRef.current = true;
        setSelectionDisabled(true);
        clearNativeSelection();
      }

      if (e.key === "Escape") {
        currentElRef.current = null;
        clearToastTimeout();
        hideHover();
        hideLabel();
        clearAllSelections();
        setSelectionDisabled(false);
        clearNativeSelection();
        return;
      }

      if (e.key === "Enter" && e.altKey && e.shiftKey) {
        e.preventDefault();
        e.stopPropagation();
        clearNativeSelection();

        if (selectedElsRef.current.length > 0) {
          const anchor =
            currentElRef.current ||
            selectedElsRef.current[selectedElsRef.current.length - 1];

          void copyPayload(
            selectedElsRef.current,
            anchor || undefined,
            `Copied multi-select payload (${selectedElsRef.current.length} elements)`
          ).catch((error) => {
            console.error("Failed to copy LLM inspector payload:", error);
            showLabelText("Copy failed · payload logged");
          });
        }
      }
    }

    function onKeyUp(e: KeyboardEvent) {
      if (e.key === "Alt") {
        altHeldRef.current = false;
        currentElRef.current = null;
        clearToastTimeout();
        hideHover();
        hideLabel();
        clearAllSelections();
        setSelectionDisabled(false);
        clearNativeSelection();
      }
    }

    document.addEventListener("mousedown", onMouseDown, true);
    document.addEventListener("mousemove", onMouseMove, true);
    document.addEventListener("click", onClick, true);
    document.addEventListener("keydown", onKeyDown, true);
    document.addEventListener("keyup", onKeyUp, true);
    window.addEventListener("scroll", onScrollOrResize, true);
    window.addEventListener("resize", onScrollOrResize);

    return () => {
      clearToastTimeout();
      setSelectionDisabled(false);
      clearNativeSelection();

      document.removeEventListener("mousedown", onMouseDown, true);
      document.removeEventListener("mousemove", onMouseMove, true);
      document.removeEventListener("click", onClick, true);
      document.removeEventListener("keydown", onKeyDown, true);
      document.removeEventListener("keyup", onKeyUp, true);
      window.removeEventListener("scroll", onScrollOrResize, true);
      window.removeEventListener("resize", onScrollOrResize);

      hoverOverlay.remove();
      selectedLayer.remove();
      label.remove();
    };
  }, [enabled]);

  return <>{children}</>;
}
