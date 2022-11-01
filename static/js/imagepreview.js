// Target specific ID
// Preview Image from the url inserted on input
$(function() {
    $("#imageurl").on('input', function() {
        let url = $("#imageurl").val();
        $("#imagePreview").attr("src", url);
    });
});