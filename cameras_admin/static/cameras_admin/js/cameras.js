$(document).ready(function () {
	$("#saveCamera_btn").click(function (e) {
		e.preventDefault();
		$("#createCamera_form").submit();
	});

	$("#sendRTSP_btn").click(function (e) {
		e.preventDefault();
		$("#sendCamera_form").submit();
	});
});