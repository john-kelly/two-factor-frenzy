$(function () {
    var viewWidth = $(window).width() * .3;
    var rightVal = -viewWidth;

    $("#toggleDiv").mouseenter(function () {
        rightVal = (rightVal * - 1) - viewWidth;
        $(this).parent().animate(
            {right: rightVal + 'px'}, {queue: false, duration: 500}
        );
    });
});
