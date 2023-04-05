$(document).ready(function () {
	$("#saveCamera_btn").click(function (e) {
		e.preventDefault();
		form = $("#createCamera_form");
		if (form[0].checkValidity()) {
			form.submit();
		} else {
			form.each(function () {
				let inputs = $("#createCamera_form :input");
				inputs.each(function () {
					if (!this.validity.valid) {
						$(this)
							.next(".invalid-feedback")
							.text(this.validationMessage)
							.addClass("d-block");
					} else {
						$(this)
							.next(".invalid-feedback")
							.removeClass("d-block");
					}
				});
			});
		}
	});

	$('input[type="checkbox"]').click(function () {
		$('input[type="checkbox"]').not(this).prop('checked', false);
	});

	$("#watchCameraForm_btn").click(function (e) {
		e.preventDefault();
		//$("#watchCamera_form").submit();
	});

	$("#deleteCameraModal").on("show.coreui.modal", function (event) {
		let button = $(event.relatedTarget);
		$("#deleteCameraId_input").val(button.data("camera-id"));
		$("#camera_name_div").text(button.data("camera-name"));
	});

	function isNumber(n) { return /^-?[\d.]+(?:e-?\d+)?$/.test(n); } 
	if (isNumber(this.URL.split('/')[4])) {
		console.log("Camera founded:", cameraById_json);
		$("#editCameraModal").modal("show");
		$("#id_field").val()
	}
});