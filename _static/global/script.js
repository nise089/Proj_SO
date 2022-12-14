function setSliderValue(event, value) {
    let targetElement = $(`#${event.target.id}`);
    targetElement.siblings('.slidertd').val(value);
}

function setControlFieldValue(event) {
    $(`#${event.target.id}`).siblings('.slider-check').val(1);
}

function showSlider(event) {
	max = $(`#${event.target.id}`).width();
	cur = event.offsetX;
	let slider = $(`#${event.target.id}`).siblings('.slidertd');
	let sliderMin = slider.attr('min');
	let sliderMax = slider.attr('max');

    now = (cur/max)*(sliderMax-sliderMin) + sliderMin;
	now = Math.round(now);

	$(`#${event.target.id}`).hide();
	slider.show();
	setSliderValue(event, now);
	setControlFieldValue(event);
}

$('.next-button').on('click', function(e) {
    let sliderFields = $('.slider-check');

    var allTrue = true;
    sliderFields.each(function(index) {
        if($(this).val() == 0) {
            allTrue = false;
            let errorMessage = $(this).parent().parent().next('.error-message');
            errorMessage.show();
        } else {
            let errorMessage = $(this).parent().parent().next('.error-message');
            errorMessage.hide();
        }
    });

    if(!allTrue) {
        e.preventDefault();
    }
});