export function highlightPython(code) {
  if (!code) return '';

  // Single regex to capture tokens in order:
  // 1. Comments: #[^\n]*
  // 2. Strings: Triple-quoted blocks ('''...''' or """...""") or single line strings ("..." or '...')
  // 3. Keywords: def, class, if, elif, else, while, for, in, and, or, not, is, import, from, as, return, pass, break, continue, try, except, finally, lambda
  // 4. Built-ins / special: print, input, len, str, int, float, list, range, dict, set, tuple, type, abs, max, min, sum, open, self
  // 5. Booleans and None: True, False, None
  // 6. Numbers: integers and floats (\b\d+(?:\.\d+)?\b)
  // 7. Function names: \b\w+(?=\()
  const tokenRegex = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|"[^"\\]*(?:\\.[^"\\]*)*"|'[^'\\]*(?:\\.[^'\\]*)*')|(\b(?:def|class|if|elif|else|while|for|in|and|or|not|is|import|from|as|return|pass|break|continue|try|except|finally|lambda)\b)|(\b(?:print|input|len|str|int|float|list|range|dict|set|tuple|type|abs|max|min|sum|open|self)\b)|(\b(?:True|False|None)\b)|(\b\d+(?:\.\d+)?\b)|(\b\w+(?=\())/g;

  let lastIndex = 0;
  let html = '';
  let match;

  const escapeHtml = (text) => {
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  };

  // Reset regex index
  tokenRegex.lastIndex = 0;

  while ((match = tokenRegex.exec(code)) !== null) {
    // Add text before the match
    if (match.index > lastIndex) {
      html += escapeHtml(code.slice(lastIndex, match.index));
    }

    const [fullMatch, comment, string, keyword, builtin, boolean, number, funcName] = match;
    const escaped = escapeHtml(fullMatch);

    if (comment) {
      html += `<span class="py-comment">${escaped}</span>`;
    } else if (string) {
      html += `<span class="py-string">${escaped}</span>`;
    } else if (keyword) {
      html += `<span class="py-keyword">${escaped}</span>`;
    } else if (builtin) {
      html += `<span class="py-builtin">${escaped}</span>`;
    } else if (boolean) {
      html += `<span class="py-boolean">${escaped}</span>`;
    } else if (number) {
      html += `<span class="py-number">${escaped}</span>`;
    } else if (funcName) {
      html += `<span class="py-func">${escaped}</span>`;
    } else {
      html += escaped;
    }

    lastIndex = tokenRegex.lastIndex;
  }

  if (lastIndex < code.length) {
    html += escapeHtml(code.slice(lastIndex));
  }

  return html;
}
