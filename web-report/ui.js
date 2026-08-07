/* ==========================================================================
   Overflow marks. Classic script (no modules) so the page runs from file://.

   A table that continues past its right edge says so with a dashed border.
   The mark is measured rather than assumed, and clears the moment the reader
   reaches the end, so it never claims content that is not there. Without JS
   the static `.scrolls` class stands as the default and errs toward telling
   the reader there is more.
   ========================================================================== */
(function () {
  'use strict';

  function marks() {
    var els = document.querySelectorAll('.tbl-wrap, .topbar__nav');

    function measure(el) {
      el.classList.add('measured');
      var more = el.scrollWidth - el.clientWidth - el.scrollLeft > 2;
      el.classList.toggle('is-clipped', more);
    }

    for (var i = 0; i < els.length; i++) {
      (function (el) {
        measure(el);
        el.addEventListener('scroll', function () {
          measure(el);
        });
      })(els[i]);
    }

    var t;
    window.addEventListener('resize', function () {
      clearTimeout(t);
      t = setTimeout(function () {
        for (var j = 0; j < els.length; j++) measure(els[j]);
      }, 120);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', marks);
  } else {
    marks();
  }
})();
