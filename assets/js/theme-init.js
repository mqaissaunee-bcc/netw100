/* Applies saved theme and text size before first paint to avoid a flash. */
(function () {
  try {
    var s = JSON.parse(localStorage.getItem('netw100-v1') || '{}');
    var p = s.prefs || {};
    if (p.theme === 'light' || p.theme === 'dark') document.documentElement.setAttribute('data-theme', p.theme);
    if (p.fs) document.documentElement.style.fontSize = p.fs + '%';
  } catch (e) { /* storage unavailable */ }
})();
