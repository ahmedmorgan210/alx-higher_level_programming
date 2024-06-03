$(function(){
    $.ajax({
        type: "GET",
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        success: function(data){
                const name = data.name;
                $("#character").append(name);           
            // $.each(data, function(){
            //     const name = data.name;
            //     $("#character").append(name);
            // });
        },
        error: function(){
            alert("getting data failed")
        }
    });
});