$(document).ready(function () {
    $("button").click(function () {
        $.get("/", function (data) {
            // $(".result").html(data);
        }).done(function () {
            alert("success");
        });
    });
});
console.log(Flask.url_for("api_v1_slicer"));