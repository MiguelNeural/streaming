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

	function isNumber(n) { return /^-?[\d.]+(?:e-?\d+)?$/.test(n); }
	
	if (isNumber(this.URL.split('/')[4]) && this.URL.split('/')[3] == 'cameras') {
		const cameraJson = JSON.parse($("#cameraJSON").val())[0];
		const peopleCount = $("#editPeopleCount_checkbox");
		const faceRec = $("#editFaceRec_checkbox");
		const vehicles = $("#editVehicles_checkbox");

		$("#id_field").val(cameraJson.pk);
		$("#editName_field").val(cameraJson.fields.name);
		$("#editRtsp_field").val(cameraJson.fields.rtsp);

		if (cameraJson.fields.peop_c_service) {
			peopleCount.attr('checked', true);
		}
		if (cameraJson.fields.face_rec_service) {
			faceRec.attr('checked', true);
		}
		if (cameraJson.fields.vehicles_service) {
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

	$("#editCameraModal").on("hidden.coreui.modal", function () {
		console.log("modal editar escondido");
		window.location.href = "/cameras"
	});

	if (this.URL.split('/')[4] == "delete") {
		$("#deleteCameraModal").modal("show");
	}

	$("#deleteCamera_btn").click(function (e) {
		e.preventDefault();
		form = $("#deleteCamera_form");
		form.submit();
	});

	$("#deleteCameraModal").on("hidden.coreui.modal", function () {
		console.log("modal eliminar escondido");
		window.location.href = "/cameras"
	});

	var icon_search =  `<svg class="btn-icon" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 96 960 960" width="24"><path d="M180 975q-24 0-42-18t-18-42V312h60v603h474v60H180Zm120-120q-24 0-42-18t-18-42V235q0-24 18-42t42-18h440q24 0 42 18t18 42v560q0 24-18 42t-42 18H300Zm0-60h440V235H300v560Zm0 0V235v560Z"/></svg>`

	$("#cameras_table").DataTable({
		paging: true,
		pageLength: 10,
		lengthChange: true,
		autoWidth: true,
		searching: true,
		bInfo: false,
		bSort: true,
		
		"columnDefs": [{
			"targets": [5, 6, 7],
			"orderable": false,
		}],
		dom: 'lBfrtip',
		buttons: [
			{extends: 'copy', text: icon_search, className: 'btn btn-dark', titleAttr: 'Copiar'}
		]
	});
	
	$("#searchInTable").keyup(function () {
		$("#cameras_table").DataTable().search($(this).val()).draw();
	})
});