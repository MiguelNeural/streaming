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
		const button = $(event.relatedTarget);
		$("#deleteCameraId_input").val(button.data("camera-id"));
		$("#camera_name_div").text(button.data("camera-name"));
	});

	function isNumber(n) { return /^-?[\d.]+(?:e-?\d+)?$/.test(n); } 
	
	if (isNumber(this.URL.split('/')[4])) {
		const cameraJson = JSON.parse($("#cameraJSON").val())[0];
		const peopleCount = $("#editPeopleCount_checkbox");
		const faceRec = $("#editFaceRec_checkbox");
		const vehicles = $("#editvehicles_checkbox");

		$("#id_field").val(cameraJson.pk);
		$("#editName_field").val(cameraJson.fields.name);
		$("#editRtsp_field").val(cameraJson.fields.rtsp);

		if(cameraJson.fields.peop_c_service) {
			peopleCount.attr('checked', true);
		}
		if(cameraJson.fields.face_rec_service) {
			faceRec.attr('checked', true);
		}
		if(cameraJson.fields.vehicles_service) {
			vehicles.attr('checked', true);
		}

		$("#editCameraModal").modal("show");
	}

	$("#editCamera_btn").click(function (e) {
		e.preventDefault();
		form = $("#editCamera_form");
		if (form[0].checkValidity()) {
			form.submit();
		}
		else {
			form.each(function () {
				let inputs = $("#editCamera_form :input");
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
});