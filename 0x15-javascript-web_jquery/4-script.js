$(function(){
    $("#toggle_header").on('click', function(){
        if($("header" ).is($('.red'))){
            $('header').removeClass('red').addClass('green');  
        } else if ($("header").is($('.green'))) {
            $('header').removeClass('green').addClass('red');
        }
    });
});