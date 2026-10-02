(function () {
  "use strict";
  var set = function (id, text) {
    var el = document.getElementById(id);
    if (el) { el.textContent = text; }
  };
  fetch("version.json", { cache: "no-store" })
    .then(function (r) {
      if (!r.ok) { throw new Error("HTTP " + r.status); }
      return r.json();
    })
    .then(function (v) {
      set("d-status", v.status || "unknown");
      set("d-version", v.version || "-");
      set("d-commit", v.commit || "-");
      set("d-env", v.environment || "-");
      set("d-built", v.built_at || "-");
      var hist = document.getElementById("history");
      if (hist && Array.isArray(v.history)) {
        v.history.forEach(function (h) {
          var tr = document.createElement("tr");
          [h.version, h.commit, h.status, h.date].forEach(function (cell) {
            var td = document.createElement("td");
            td.textContent = cell;
            tr.appendChild(td);
          });
          hist.appendChild(tr);
        });
      }
    })
    .catch(function (err) {
      set("d-status", "Unavailable (" + err.message + ")");
    });
})();
