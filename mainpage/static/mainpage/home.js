"use strict";

$(document).ready(function(){

    resizeActivityImage();
    resizeActivityImage2();

    $(window).resize(function(){
        resizeActivityImage();
        resizeActivityImage2();
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
        } else if ($(window).width() == 768){
            $(this).find(".words").height(newHeight-12);
            $(this).height(newHeight);
        } else {
            $(this).find(".words").height(newHeight-22);
            $(this).height(newHeight);
        }
    });
}

function resizeActivityImage2() {
    $(".activity_image").each(function(){
        var width = $(".activity_image").width();
        $(this).height(width);
    });
}