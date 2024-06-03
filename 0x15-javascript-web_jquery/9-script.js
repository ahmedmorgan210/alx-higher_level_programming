$(function(){
    $.ajax({
        type: "GET",
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        success: function(data){
            $("#hello").append(data.hello);
        }
    });
});