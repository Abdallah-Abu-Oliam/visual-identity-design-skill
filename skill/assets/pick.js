/* ==========================================================================
   pick.js — the readback layer for every gate page.

   Copy to brand/pick.js at Phase 2 alongside preview.css, and link it from any
   page where the user chooses something: art direction boards, logo concepts,
   palette options, pattern before/after.

       <script src="../pick.js" data-key="art-direction"></script>

   Markup contract — one attribute:

       <article class="card" data-pick="seal"> … <button class="pick">Choose</button> … </article>

   Anything carrying data-pick becomes selectable. A descendant <button class="pick">
   toggles it; if there is no button, the element itself is clickable.

   The model then reads the answer back with ONE call, the same on every page:

       Pick.collect()   ->  { key:"art-direction", picked:"seal", at:"2026-..." }

   Selection persists to localStorage, so a closed tab loses nothing.

   Options:
       data-key    storage key. Defaults to the page filename.
       data-multi  present = allow several. Absent = single choice.
       data-limit  soft cap. Going over is REPORTED, never blocked — an overflow
                   is a signal that taste is unresolved, not a filling error.
   ========================================================================== */

(function () {
  var s = document.currentScript || {};
  var KEY = 'pick:' + (s.getAttribute && s.getAttribute('data-key')
            || location.pathname.split('/').pop().replace('.html', '') || 'page');
  var MULTI = s.getAttribute && s.getAttribute('data-multi') !== null;
  var LIMIT = s.getAttribute && parseInt(s.getAttribute('data-limit') || '0', 10);

  var picked = MULTI ? [] : null;

  function nodes() { return [].slice.call(document.querySelectorAll('[data-pick]')); }
  function isOn(v) { return MULTI ? picked.indexOf(v) > -1 : picked === v; }

  function paint() {
    nodes().forEach(function (n) {
      var on = isOn(n.dataset.pick);
      n.classList.toggle('on', on);
      var b = n.querySelector('button.pick');
      if (b) b.classList.toggle('on', on);
    });
    var st = document.getElementById('status');
    if (st) {
      var sel = MULTI ? picked : (picked ? [picked] : []);
      if (!sel.length) st.textContent = 'Nothing chosen yet';
      else {
        var label = sel.map(function (v) {
          var n = document.querySelector('[data-pick="' + v + '"]');
          return (n && n.dataset.label) || v;
        }).join(' · ');
        st.innerHTML = 'Chosen: <b>' + label + '</b>';
        if (LIMIT && sel.length > LIMIT) {
          st.innerHTML += ' — over the limit of ' + LIMIT +
            '. That is a signal, not an error: it says the choice is unresolved.';
        }
      }
    }
    try { localStorage.setItem(KEY, JSON.stringify(Pick.collect())); } catch (e) {}
  }

  function toggle(v) {
    if (MULTI) {
      var i = picked.indexOf(v);
      if (i > -1) picked.splice(i, 1); else picked.push(v);
    } else {
      picked = (picked === v) ? null : v;
    }
    paint();
  }

  window.Pick = {
    collect: function () {
      return { key: KEY, picked: picked, at: new Date().toISOString() };
    },
    set: function (v) { picked = v; paint(); return window.Pick.collect(); },
    clear: function () { picked = MULTI ? [] : null; try { localStorage.removeItem(KEY); } catch (e) {} paint(); }
  };

  function wire() {
    nodes().forEach(function (n) {
      var target = n.querySelector('button.pick') || n;
      target.addEventListener('click', function (e) { e.preventDefault(); toggle(n.dataset.pick); });
    });
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) { var d = JSON.parse(raw); if (d && d.picked != null) picked = d.picked; }
    } catch (e) {}
    paint();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire);
  else wire();
})();
