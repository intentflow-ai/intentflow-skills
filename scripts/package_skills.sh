#!/usr/bin/env bash
# Zip each skill for upload to the Claude app (Customize > Skills > Upload a skill),
# plus one archive with every skill for Claude Code (~/.claude/skills/).
#
# Usage: bash scripts/package_skills.sh [output-folder]   (default: dist)
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:-dist}"
mkdir -p "$out"
out="$(cd "$out" && pwd)"

cd "$root/skills"
for dir in */; do
  name="${dir%/}"
  rm -f "$out/$name.zip"
  zip -qrX "$out/$name.zip" "$name" -x '*.DS_Store'
  echo "packaged $name.zip"
done

rm -f "$out/intentflow-skills-all.zip"
zip -qrX "$out/intentflow-skills-all.zip" */ -x '*.DS_Store'
echo "packaged intentflow-skills-all.zip"
