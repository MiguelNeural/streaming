$(document).ready(function () {
	$("#saveCamera_btn").click(function (e) {
		e.preventDefault();
		$("#createCamera_form").submit();
	});

	$("#enviarRTSP_btn").click(function (e) {
		e.preventDefault();
		$("#enviarRTSP_form").submit();
	});
});