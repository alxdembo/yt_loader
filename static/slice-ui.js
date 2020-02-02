$(document).ready(function () {
    $("button").click(function () {
        $.get("/", function (data) {
            // $(".result").html(data);
        }).done(function () {
            alert("success");
        });
    });
});
