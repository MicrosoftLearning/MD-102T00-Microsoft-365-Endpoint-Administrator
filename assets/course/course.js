// Course site enhancements for the AB-650 labs. Runs at the end of <body>.
(function () {
  'use strict';

  // GitHub alert syntax (> [!NOTE]) renders natively on github.com, but kramdown on
  // GitHub Pages leaves "[!NOTE]" as literal text. Turn those blockquotes into callouts.
  var titles = { NOTE: 'Note', TIP: 'Tip', IMPORTANT: 'Important', WARNING: 'Warning', CAUTION: 'Caution' };
  var marker = /^\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*/;
  document.querySelectorAll('blockquote').forEach(function (quote) {
    var first = quote.querySelector('p');
    if (!first || !first.firstChild || first.firstChild.nodeType !== Node.TEXT_NODE) return;
    var match = first.firstChild.nodeValue.match(marker);
    if (!match) return;
    var type = match[1];
    first.firstChild.nodeValue = first.firstChild.nodeValue.replace(marker, '');
    if (!first.textContent.trim() && !first.querySelector('img')) first.remove();
    quote.classList.add('callout', 'callout-' + type.toLowerCase());
    var title = document.createElement('p');
    title.className = 'callout-title';
    title.textContent = titles[type];
    quote.insertBefore(title, quote.firstChild);
  });

  // Open a collapsed learning path on the index page when its link is followed.
  function openTarget() {
    if (!location.hash) return;
    var target = document.getElementById(decodeURIComponent(location.hash.substring(1)));
    if (!target) return;
    var details = target.closest('details');
    if (details) details.open = true;
    target.scrollIntoView();
  }
  openTarget();
  window.addEventListener('hashchange', openTarget);
})();
