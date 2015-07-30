$(document).ready(function(){

    resizeActivityImage();

    $(window).resize(function(){
        resizeActivityImage();
    });

});

function resizeActivityImage() {

    $(".activity").each(function(){

        var width = $(".pic").width();
        var newHeight = width*2/3;

        $(this).find(".pic").height(newHeight);
        if ($(window).width() < 768) {
            $(this).find(".words").height(newHeight-32);
            $(this).height(2*newHeight-20);
        } else {
            $(this).find(".words").height(newHeight-22);
            $(this).height(newHeight);
        }
    });
}