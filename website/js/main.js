(function () {
  "use strict";

  var year = document.getElementById("year");
  if (year) { year.textContent = String(new Date().getFullYear()); }

  var btn = document.getElementById("menu-btn");
  var list = document.getElementById("nav-list");
  if (btn && list) {
    btn.addEventListener("click", function () {
      var open = list.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  var form = document.getElementById("contact-form");
  if (form) {
    var status = document.getElementById("form-status");
    var emailOk = function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); };
    var setErr = function (id, msg) {
      var el = document.getElementById(id + "-error");
      if (el) { el.textContent = msg; }
      return msg === "";
    };
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.elements.name.value.trim();
      var email = form.elements.email.value.trim();
      var message = form.elements.message.value.trim();
      var a = setErr("name", name ? "" : "Enter your name.");
      var b = setErr("email", emailOk(email) ? "" : "Enter a valid email address.");
      var c = setErr("message", message.length >= 10 ? "" : "Write at least 10 characters.");
      if (a && b && c) {
        var subject = encodeURIComponent("Website message from " + name);
        var body = encodeURIComponent(message + "\n\n" + name + " <" + email + ">");
        status.textContent = "Opening your email app...";
        window.location.href = "mailto:hello@example.com?subject=" + subject + "&body=" + body;
      } else {
        status.textContent = "Fix the highlighted fields and send again.";
      }
    });
  }
})();
