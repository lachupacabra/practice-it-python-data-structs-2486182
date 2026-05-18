#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MD_FILE="${1:-"$ROOT_DIR/brick-phone-data-ai-architecture.md"}"
HTML_FILE="${2:-"${MD_FILE%.md}.html"}"
PDF_FILE="${3:-"${MD_FILE%.md}.pdf"}"
TMP_DIR="$(mktemp -d)"

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

if [[ ! -f "$MD_FILE" ]]; then
  echo "Markdown source not found: $MD_FILE" >&2
  exit 1
fi

if [[ -n "${CHROME_BIN:-}" ]]; then
  CHROME="$CHROME_BIN"
elif [[ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]]; then
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif command -v google-chrome >/dev/null 2>&1; then
  CHROME="$(command -v google-chrome)"
elif command -v google-chrome-stable >/dev/null 2>&1; then
  CHROME="$(command -v google-chrome-stable)"
elif command -v chromium >/dev/null 2>&1; then
  CHROME="$(command -v chromium)"
else
  echo "Chrome or Chromium is required for Mermaid validation and PDF export." >&2
  echo "Set CHROME_BIN=/path/to/chrome if it is installed in a custom location." >&2
  exit 1
fi

mkdir -p "$(dirname "$HTML_FILE")" "$(dirname "$PDF_FILE")"

echo "Generating standalone HTML..."
MD_FILE="$MD_FILE" HTML_FILE="$HTML_FILE" node --input-type=module <<'NODE'
import fs from "node:fs/promises";

const mdFile = process.env.MD_FILE;
const htmlFile = process.env.HTML_FILE;
const markdown = await fs.readFile(mdFile, "utf8");
const expectedMermaid = (markdown.match(/^```mermaid\s*$/gm) || []).length;

async function download(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Failed to download ${url}: ${response.status} ${response.statusText}`);
  }
  return response.text();
}

function safeScript(source) {
  return source.replace(/<\/script/gi, "<\\/script");
}

function safeJson(value) {
  return JSON.stringify(value)
    .replace(/</g, "\\u003C")
    .replace(/\u2028/g, "\\u2028")
    .replace(/\u2029/g, "\\u2029");
}

const [markedJs, mermaidJs] = await Promise.all([
  download("https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"),
  download("https://cdn.jsdelivr.net/npm/mermaid@10.9.3/dist/mermaid.min.js")
]);

const html = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Brick Phone Wireless: Data Architecture and AI Ecosystem</title>
  <style>
    :root {
      color-scheme: light;
      --ink: #172033;
      --muted: #526070;
      --soft: #eef3f8;
      --line: #d7e0ea;
      --accent: #0f766e;
      --accent-soft: #dff7f2;
      --code-bg: #111827;
      --code-fg: #eef2ff;
      --table-head: #f3f7fb;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      background: #f6f8fb;
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      font-size: 16px;
      line-height: 1.62;
    }

    .document-shell {
      max-width: 1120px;
      margin: 0 auto;
      padding: 40px 28px 72px;
    }

    .paper {
      background: #fff;
      border: 1px solid var(--line);
      box-shadow: 0 16px 48px rgba(23, 32, 51, 0.08);
      padding: 48px;
    }

    #export-status {
      margin-bottom: 18px;
      color: var(--muted);
      font-size: 13px;
    }

    h1, h2, h3 {
      line-height: 1.18;
      letter-spacing: 0;
    }

    h1 {
      margin: 0 0 22px;
      color: #0f172a;
      font-size: 38px;
    }

    h2 {
      margin: 42px 0 14px;
      padding-top: 10px;
      border-top: 1px solid var(--line);
      color: #0f172a;
      font-size: 25px;
    }

    h3 {
      margin: 28px 0 10px;
      color: #213049;
      font-size: 19px;
    }

    p {
      margin: 0 0 14px;
    }

    ul, ol {
      margin-top: 8px;
      padding-left: 24px;
    }

    li {
      margin: 4px 0;
    }

    a {
      color: #0f766e;
      text-decoration-thickness: 1px;
      text-underline-offset: 3px;
    }

    table {
      width: 100%;
      margin: 18px 0 26px;
      border-collapse: collapse;
      font-size: 14px;
    }

    th, td {
      border: 1px solid var(--line);
      padding: 10px 12px;
      vertical-align: top;
    }

    th {
      background: var(--table-head);
      color: #1f2937;
      font-weight: 700;
    }

    code {
      border-radius: 5px;
      background: #eef3f8;
      padding: 0.1em 0.35em;
      color: #18324a;
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
      font-size: 0.92em;
    }

    pre {
      overflow-x: auto;
      border-radius: 8px;
      background: var(--code-bg);
      color: var(--code-fg);
      padding: 18px;
      page-break-inside: avoid;
    }

    pre code {
      background: transparent;
      color: inherit;
      padding: 0;
      font-size: 13px;
      line-height: 1.55;
    }

    blockquote {
      margin: 20px 0;
      border-left: 4px solid var(--accent);
      background: var(--accent-soft);
      padding: 12px 16px;
      color: #164e63;
    }

    .mermaid {
      width: 100%;
      margin: 22px 0 30px;
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfdff;
      padding: 18px;
      text-align: center;
      page-break-inside: avoid;
    }

    .mermaid svg {
      max-width: 100%;
      height: auto;
    }

    body[data-export-error] #export-status {
      color: #b42318;
      font-weight: 700;
    }

    @media print {
      @page {
        size: Letter;
        margin: 0.55in;
      }

      body {
        background: #fff;
        font-size: 12px;
      }

      .document-shell {
        max-width: none;
        padding: 0;
      }

      .paper {
        border: 0;
        box-shadow: none;
        padding: 0;
      }

      #export-status {
        display: none;
      }

      h1 {
        font-size: 28px;
      }

      h2 {
        font-size: 18px;
      }

      h3 {
        font-size: 14px;
      }

      table {
        font-size: 9.5px;
      }

      th, td {
        padding: 5px 6px;
      }

      pre {
        white-space: pre-wrap;
        font-size: 9px;
      }

      .mermaid {
        padding: 10px;
        margin: 14px 0 18px;
      }
    }
  </style>
</head>
<body>
  <main class="document-shell">
    <article class="paper">
      <div id="export-status">Rendering Markdown and Mermaid diagrams...</div>
      <div id="content"></div>
    </article>
  </main>

  <script>
${safeScript(markedJs)}
  </script>
  <script>
${safeScript(mermaidJs)}
  </script>
  <script>
    (async function renderDocument() {
      const markdown = ${safeJson(markdown)};
      const expectedMermaid = ${expectedMermaid};
      const content = document.getElementById("content");
      const status = document.getElementById("export-status");

      function escapeHtml(value) {
        return value
          .replace(/&/g, "&amp;")
          .replace(/</g, "&lt;")
          .replace(/>/g, "&gt;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&#039;");
      }

      function setReady(message) {
        status.textContent = message;
        document.body.dataset.exportReady = "true";
        window.__EXPORT_READY__ = true;
      }

      function setError(error) {
        const message = error && error.message ? error.message : String(error);
        status.textContent = "Mermaid render failed: " + message;
        document.body.dataset.exportError = message;
        document.body.dataset.exportReady = "true";
        window.__EXPORT_READY__ = true;
      }

      try {
        window.__EXPORT_READY__ = false;
        content.innerHTML = window.marked.parse(markdown, {
          gfm: true,
          breaks: false
        });

        const codeBlocks = content.querySelectorAll("pre > code");
        codeBlocks.forEach((code) => {
          const className = code.getAttribute("class") || "";
          if (!className.includes("language-mermaid")) {
            return;
          }

          const diagram = document.createElement("div");
          diagram.className = "mermaid";
          diagram.textContent = code.textContent;
          code.parentElement.replaceWith(diagram);
        });

        const diagrams = Array.from(content.querySelectorAll(".mermaid"));
        if (diagrams.length === 0) {
          setReady("Rendered with no Mermaid diagrams detected.");
          return;
        }

        window.mermaid.initialize({
          startOnLoad: false,
          securityLevel: "strict",
          theme: "base",
          flowchart: {
            curve: "basis",
            htmlLabels: true
          },
          themeVariables: {
            primaryColor: "#dff7f2",
            primaryTextColor: "#172033",
            primaryBorderColor: "#0f766e",
            lineColor: "#526070",
            secondaryColor: "#eef3f8",
            tertiaryColor: "#ffffff",
            fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
          }
        });

        await window.mermaid.run({ nodes: diagrams });

        const rendered = content.querySelectorAll(".mermaid svg").length;
        if (rendered < expectedMermaid) {
          throw new Error("Only rendered " + rendered + " of " + expectedMermaid + " Mermaid diagrams.");
        }

        diagrams.forEach((diagram) => {
          diagram.setAttribute("data-rendered", "true");
        });
        setReady("Rendered " + rendered + " Mermaid diagrams.");
      } catch (error) {
        const failedBlocks = content.querySelectorAll(".mermaid");
        failedBlocks.forEach((block) => {
          if (!block.querySelector("svg")) {
            block.innerHTML = "<pre><code>" + escapeHtml(block.textContent) + "</code></pre>";
          }
        });
        setError(error);
      }
    })();
  </script>
</body>
</html>
`;

await fs.writeFile(htmlFile, html, "utf8");
console.log(`Wrote ${htmlFile}`);
NODE

HTML_URL="$(HTML_FILE="$HTML_FILE" node -e 'console.log(require("node:url").pathToFileURL(process.env.HTML_FILE).href)')"
EXPECTED_MERMAID="$(grep -c '^```mermaid' "$MD_FILE" || true)"
DOM_FILE="$TMP_DIR/rendered-dom.html"
CHROME_LOG="$TMP_DIR/chrome.log"

echo "Validating Mermaid render in headless Chrome..."
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --allow-file-access-from-files \
  --disable-dev-shm-usage \
  --virtual-time-budget=30000 \
  --dump-dom "$HTML_URL" > "$DOM_FILE" 2> "$CHROME_LOG"

if grep -Eq '<body[^>]*data-export-error' "$DOM_FILE"; then
  echo "Mermaid validation failed. Chrome log:" >&2
  cat "$CHROME_LOG" >&2
  exit 1
fi

if ! grep -q 'data-export-ready="true"' "$DOM_FILE"; then
  echo "Timed out waiting for the HTML export to finish rendering." >&2
  cat "$CHROME_LOG" >&2
  exit 1
fi

SVG_COUNT="$(grep -o '<div class="mermaid"[^>]*data-rendered="true"[^>]*><svg' "$DOM_FILE" | wc -l | tr -d ' ')"
if [[ "$SVG_COUNT" -lt "$EXPECTED_MERMAID" ]]; then
  echo "Expected $EXPECTED_MERMAID rendered Mermaid diagrams, found $SVG_COUNT." >&2
  cat "$CHROME_LOG" >&2
  exit 1
fi

echo "Generating PDF from rendered HTML..."
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --allow-file-access-from-files \
  --disable-dev-shm-usage \
  --no-pdf-header-footer \
  --virtual-time-budget=30000 \
  --print-to-pdf="$PDF_FILE" "$HTML_URL" > "$CHROME_LOG" 2>&1

if [[ ! -s "$PDF_FILE" ]]; then
  echo "PDF export failed or produced an empty file." >&2
  cat "$CHROME_LOG" >&2
  exit 1
fi

PDF_BYTES="$(wc -c < "$PDF_FILE" | tr -d ' ')"
if [[ "$PDF_BYTES" -lt 10000 ]]; then
  echo "PDF export looks unexpectedly small: $PDF_BYTES bytes." >&2
  cat "$CHROME_LOG" >&2
  exit 1
fi

echo "Done."
echo "HTML: $HTML_FILE"
echo "PDF:  $PDF_FILE"
echo "Mermaid diagrams rendered: $SVG_COUNT"
