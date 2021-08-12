document.getElementById("MyBtn").addEventListener("click", () => {
  var x = document.getElementById("others");

  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
});