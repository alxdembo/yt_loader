$(document).ready(function () {
    $("button").click(function () {
        let options = {
            beforeSubmit: function () {
                $(".lds-dual-ring").removeClass('hidden');
            },
            url: Flask.url_for('api.api_v1_slicer', {'source': 'youtube'}),
            type: 'get',

            error: function (e) {
                $(".lds-dual-ring").addClass('hidden');
                $("#result").removeClass('hidden');
                $('#result').val('Error, please try again. ' + JSON.parse(e.responseText).error_message)
            },
            success: function (e) {
                $(".lds-dual-ring").css("display", "none");
                $("#result").removeClass('hidden');
                $('#result').val(e.url)
            }
        };

        $("#slice-form").ajaxSubmit(options);
    });
});
