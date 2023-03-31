$(document).ready(function () {
	$("#saveCamera_btn").click(function (event) {
		console.log("sumbit")
		event.preventDefault();
		$("#createCamera_form").submit();
	});
});