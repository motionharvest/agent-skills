#!/bin/bash

# agent-skills installer
# Symlinks skills to various agent tools: Claude Code, Cursor CLI, Python, OpenCode, Codex

set -e

SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SKILLS_DIR"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Available skills (exclude .git, README, etc)
AVAILABLE_SKILLS=(
  "perfect-design"
  "audience-research"
  "reference-site-analysis"
  "ux-methodology-process"
  "ux-methodology-design"
  "persona-archetypes"
  "audience-site-brief"
  "cas-agent-setup"
  "cas-operational-loop"
  "inspector-overlay"
)

# Filter to only skills that exist
SKILLS_TO_INSTALL=()
for skill in "${AVAILABLE_SKILLS[@]}"; do
  if [ -d "$SKILLS_DIR/$skill" ]; then
    SKILLS_TO_INSTALL+=("$skill")
  fi
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}agent-skills installer${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Tool detection and setup
setup_claude_code() {
  local skill=$1
  local claude_skills_dir="$HOME/.claude/skills"

  if [ ! -d "$claude_skills_dir" ]; then
    mkdir -p "$claude_skills_dir"
    echo -e "${GREEN}✓${NC} Created $claude_skills_dir"
  fi

  local link_path="$claude_skills_dir/$skill"
  if [ -L "$link_path" ]; then
    rm "$link_path"
  fi

  ln -s "$SKILLS_DIR/$skill" "$link_path"
  echo -e "${GREEN}✓${NC} Symlinked $skill → Claude Code (~/.claude/skills/)"
}

setup_cursor_cli() {
  local skill=$1
  local cursor_skills_dir="$HOME/.cursor/skills"

  if [ ! -d "$cursor_skills_dir" ]; then
    mkdir -p "$cursor_skills_dir"
    echo -e "${GREEN}✓${NC} Created $cursor_skills_dir"
  fi

  local link_path="$cursor_skills_dir/$skill"
  if [ -L "$link_path" ]; then
    rm "$link_path"
  fi

  ln -s "$SKILLS_DIR/$skill" "$link_path"
  echo -e "${GREEN}✓${NC} Symlinked $skill → Cursor CLI (~/.cursor/skills/)"
}

setup_python() {
  local skill=$1
  local python_skills_dir="$HOME/.skills"

  if [ ! -d "$python_skills_dir" ]; then
    mkdir -p "$python_skills_dir"
    echo -e "${GREEN}✓${NC} Created $python_skills_dir"
  fi

  local link_path="$python_skills_dir/$skill"
  if [ -L "$link_path" ]; then
    rm "$link_path"
  fi

  ln -s "$SKILLS_DIR/$skill" "$link_path"
  echo -e "${GREEN}✓${NC} Symlinked $skill → Python (~/.skills/)"
}

setup_opencode() {
  local skill=$1
  local opencode_skills_dir="$HOME/.opencode/skills"

  if [ ! -d "$opencode_skills_dir" ]; then
    mkdir -p "$opencode_skills_dir"
    echo -e "${GREEN}✓${NC} Created $opencode_skills_dir"
  fi

  local link_path="$opencode_skills_dir/$skill"
  if [ -L "$link_path" ]; then
    rm "$link_path"
  fi

  ln -s "$SKILLS_DIR/$skill" "$link_path"
  echo -e "${GREEN}✓${NC} Symlinked $skill → OpenCode (~/.opencode/skills/)"
}

setup_codex() {
  local skill=$1
  local codex_skills_dir="$HOME/.codex/skills"

  if [ ! -d "$codex_skills_dir" ]; then
    mkdir -p "$codex_skills_dir"
    echo -e "${GREEN}✓${NC} Created $codex_skills_dir"
  fi

  local link_path="$codex_skills_dir/$skill"
  if [ -L "$link_path" ]; then
    rm "$link_path"
  fi

  ln -s "$SKILLS_DIR/$skill" "$link_path"
  echo -e "${GREEN}✓${NC} Symlinked $skill → Codex (~/.codex/skills/)"
}

# Prompt for which tools to install
echo -e "${YELLOW}Which tools do you use?${NC}"
echo ""
read -p "Install for Claude Code? (y/n) " -n 1 -r && echo
install_claude=$REPLY

read -p "Install for Cursor CLI? (y/n) " -n 1 -r && echo
install_cursor=$REPLY

read -p "Install for Python? (y/n) " -n 1 -r && echo
install_python=$REPLY

read -p "Install for OpenCode? (y/n) " -n 1 -r && echo
install_opencode=$REPLY

read -p "Install for Codex? (y/n) " -n 1 -r && echo
install_codex=$REPLY

echo ""
echo -e "${YELLOW}Available skills:${NC}"
for i in "${!SKILLS_TO_INSTALL[@]}"; do
  echo "  $((i+1)). ${SKILLS_TO_INSTALL[$i]}"
done
echo ""

read -p "Install all skills? (y/n) " -n 1 -r && echo
install_all=$REPLY

selected_skills=()
if [[ $install_all =~ ^[Yy]$ ]]; then
  selected_skills=("${SKILLS_TO_INSTALL[@]}")
else
  echo ""
  echo -e "${YELLOW}Select skills to install (comma-separated numbers, or leave blank for none):${NC}"
  read -r selections

  IFS=',' read -ra SELECTION_ARRAY <<< "$selections"
  for sel in "${SELECTION_ARRAY[@]}"; do
    sel=$(echo "$sel" | xargs) # trim whitespace
    if [[ $sel =~ ^[0-9]+$ ]] && [ "$sel" -ge 1 ] && [ "$sel" -le "${#SKILLS_TO_INSTALL[@]}" ]; then
      selected_skills+=("${SKILLS_TO_INSTALL[$((sel-1))]}")
    fi
  done
fi

if [ ${#selected_skills[@]} -eq 0 ]; then
  echo -e "${YELLOW}No skills selected. Exiting.${NC}"
  exit 0
fi

echo ""
echo -e "${BLUE}Installing ${#selected_skills[@]} skill(s)...${NC}"
echo ""

# Install selected skills to selected tools
for skill in "${selected_skills[@]}"; do
  echo -e "${BLUE}→ $skill${NC}"

  [[ $install_claude =~ ^[Yy]$ ]] && setup_claude_code "$skill"
  [[ $install_cursor =~ ^[Yy]$ ]] && setup_cursor_cli "$skill"
  [[ $install_python =~ ^[Yy]$ ]] && setup_python "$skill"
  [[ $install_opencode =~ ^[Yy]$ ]] && setup_opencode "$skill"
  [[ $install_codex =~ ^[Yy]$ ]] && setup_codex "$skill"

  echo ""
done

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Installation complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Skills are now symlinked to:"
[[ $install_claude =~ ^[Yy]$ ]] && echo "  • Claude Code: ~/.claude/skills/"
[[ $install_cursor =~ ^[Yy]$ ]] && echo "  • Cursor CLI: ~/.cursor/skills/"
[[ $install_python =~ ^[Yy]$ ]] && echo "  • Python: ~/.skills/"
[[ $install_opencode =~ ^[Yy]$ ]] && echo "  • OpenCode: ~/.opencode/skills/"
[[ $install_codex =~ ^[Yy]$ ]] && echo "  • Codex: ~/.codex/skills/"
echo ""
echo "See SKILLS.md for skill descriptions and usage."
echo ""
