$(document).ready(function () {
  $("#sandeep").click(function () {
    $.ajax({
      url: "index/",
      type: "GET",
      dataType: "json",
      success: function (response) {
        $(".recom-1").html(response);
        console.log(response);
        console.log("success");

      }
    })
  });
});