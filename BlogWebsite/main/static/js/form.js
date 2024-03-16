    function myFunction() {
      var checkBox = document.getElementById("is_published");
      var text = document.querySelector(".div_published_at");
      if (checkBox.checked == true) {
        text.style.display = "block";
      } else {
        text.style.display = "none";
      }
    }