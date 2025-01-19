// assets/js/mathjax.js
document.addEventListener("DOMContentLoaded", function() {
  // Ensure MathJax re-renders when the page is loaded
  MathJax.typeset();

  // Trigger MathJax rendering after expanding the details section
  var details = document.querySelectorAll("details");
  details.forEach(function(detail) {
    detail.addEventListener("toggle", function() {
      if (detail.open) {
        MathJax.typeset();  // Re-render MathJax when the section is expanded
      }
    });
  });
});

