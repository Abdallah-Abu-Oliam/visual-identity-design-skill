#!/usr/bin/env bash
#
# export.sh — rasterise an SVG logo to PNG at standard sizes.
#
# Derived from the logo-designer-skill project. MODIFIED — see "Modifications" below.
#   Source:  https://github.com/neonwatty/logo-designer-skill
#   License: MIT — Copyright (c) 2026 Jeremy Watt
#   Full licence text: ../../NOTICE
#
# Modifications from the original:
#   1. The `sharp` branch scaled to a square canvas while every other converter scaled
#      by width. A 1024x512 wordmark therefore exported as a padded square on machines
#      with sharp installed, and as a correct 2:1 image everywhere else. Now scales by
#      width on all five paths.
#   2. Added a guard against live <text> elements. Rasterisers substitute whatever font
#      they can find, which distorts Latin wordmarks and can break Arabic letter joining
#      outright. Override with --allow-text.
#   3. Added a monochrome export — required for engraving, foil, stamping, and
#      one-colour print. Suppress with --no-mono.
#   4. Install hints are now platform-aware; the original suggested Homebrew only.
#
set -euo pipefail

ALLOW_TEXT=0
MAKE_MONO=1
ARGS=()
for a in "$@"; do
  case "$a" in
    --allow-text) ALLOW_TEXT=1 ;;
    --no-mono)    MAKE_MONO=0 ;;
    -h|--help)
      echo "Usage: export.sh <input.svg> <output-dir> [--allow-text] [--no-mono]"
      exit 0 ;;
    *) ARGS+=("$a") ;;
  esac
done

INPUT_SVG="${ARGS[0]:?Usage: export.sh <input.svg> <output-dir> [--allow-text] [--no-mono]}"
OUTPUT_DIR="${ARGS[1]:?Usage: export.sh <input.svg> <output-dir> [--allow-text] [--no-mono]}"
SIZES=(16 32 48 192 512 1024 2048)
MONO_SIZES=(512 1024)
BASENAME="logo"

[ -f "$INPUT_SVG" ] || { echo "ERROR: no such file: $INPUT_SVG" >&2; exit 1; }
mkdir -p "$OUTPUT_DIR"

# --- Guard: live <text> ------------------------------------------------------------
if grep -qi '<text' "$INPUT_SVG"; then
  if [ "$ALLOW_TEXT" -eq 0 ]; then
    cat >&2 <<'EOF'
ERROR: This SVG still contains <text> elements.

A finished mark must have its type converted to <path> outlines. Rasterisers substitute
whatever font they happen to find, so the PNG can differ from what was designed:

  - Latin wordmarks render in the wrong typeface, with the wrong spacing.
  - Arabic is contextual. A substituted font can break letter joining entirely,
    producing disconnected letterforms that read as broken.

Convert the text to outlines, then export again.
Re-run with --allow-text only when exporting a draft you do not intend to ship.
EOF
    exit 1
  fi
  echo "WARNING: <text> present — fonts will be substituted at raster time. (--allow-text)" >&2
  echo "" >&2
fi

# --- Detect converter --------------------------------------------------------------
TOOL=""
if command -v resvg &>/dev/null; then TOOL="resvg"
elif npx --yes @aspect-build/resvg --help &>/dev/null 2>&1; then TOOL="npx-resvg"
elif command -v node &>/dev/null && node -e "require('sharp')" &>/dev/null 2>&1; then TOOL="sharp"
elif command -v inkscape &>/dev/null; then TOOL="inkscape"
elif command -v rsvg-convert &>/dev/null; then TOOL="rsvg-convert"
else
  echo "ERROR: No SVG-to-PNG converter found." >&2
  echo "" >&2
  echo "Install one of the following:" >&2
  echo "  npm install -g @aspect-build/resvg     (recommended — works on every platform)" >&2
  case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*)
      echo "  winget install Inkscape.Inkscape" >&2
      echo "  choco install inkscape                 (if you use Chocolatey)" >&2
      echo "  scoop install inkscape                 (if you use Scoop)" >&2 ;;
    Darwin)
      echo "  brew install inkscape" >&2
      echo "  brew install librsvg" >&2 ;;
    *)
      echo "  sudo apt install inkscape              (Debian/Ubuntu)" >&2
      echo "  sudo apt install librsvg2-bin          (provides rsvg-convert)" >&2 ;;
  esac
  exit 1
fi

# --- Rasterise: always scale by WIDTH, never force a square ------------------------
render() {  # render <src.svg> <out.png> <width>
  local src="$1" out="$2" w="$3"
  case "$TOOL" in
    resvg)        resvg "$src" "$out" --width "$w" ;;
    npx-resvg)    npx --yes @aspect-build/resvg "$src" "$out" --width "$w" ;;
    sharp)        node -e "
                    const sharp=require('sharp');
                    sharp('$src').resize({ width: $w })
                      .png().toFile('$out')
                      .then(()=>process.exit(0))
                      .catch(e=>{console.error(e);process.exit(1);});
                  " ;;
    inkscape)     inkscape "$src" --export-type=png --export-filename="$out" --export-width="$w" ;;
    rsvg-convert) rsvg-convert -w "$w" -o "$out" "$src" ;;
  esac
}

echo "Using: $TOOL"
echo ""

cp "$INPUT_SVG" "$OUTPUT_DIR/$BASENAME.svg"

for SIZE in "${SIZES[@]}"; do
  render "$INPUT_SVG" "$OUTPUT_DIR/${BASENAME}-${SIZE}.png" "$SIZE"
  echo "  ${BASENAME}-${SIZE}.png"
done

# --- Monochrome ---------------------------------------------------------------------
if [ "$MAKE_MONO" -eq 1 ]; then
  MONO_SVG="$OUTPUT_DIR/${BASENAME}-mono.svg"
  # Flatten every colour to black while preserving `none`.
  #
  # The protection markers deliberately destroy the `="` and `:` shape, so the flatten
  # passes below cannot match them. Keeping the marker inside quotes does not work — the
  # flatten pass matches any quoted value and would turn fill="none" solid black,
  # filling in every hollow shape in the mark.
  sed -E \
    -e 's/(fill|stroke)="(none|transparent)"/\1@@ATTR@@/g' \
    -e 's/(fill|stroke):[[:space:]]*(none|transparent)/\1@@STYLE@@/g' \
    -e 's/(fill|stroke)="[^"]*"/\1="#000000"/g' \
    -e 's/(fill|stroke):[[:space:]]*[^;"]*/\1:#000000/g' \
    -e 's/(fill|stroke)@@ATTR@@/\1="none"/g' \
    -e 's/(fill|stroke)@@STYLE@@/\1:none/g' \
    "$INPUT_SVG" > "$MONO_SVG"

  echo ""
  echo "  ${BASENAME}-mono.svg   (single colour — engraving, foil, stamping, 1-colour print)"
  for SIZE in "${MONO_SIZES[@]}"; do
    render "$MONO_SVG" "$OUTPUT_DIR/${BASENAME}-mono-${SIZE}.png" "$SIZE"
    echo "  ${BASENAME}-mono-${SIZE}.png"
  done
  echo ""
  echo "  NOTE: the monochrome version flattens flat fills and strokes. Check it —"
  echo "        gradients and overlapping shapes may need redrawing by hand."
fi

echo ""
echo "Done. Files in: $OUTPUT_DIR"
