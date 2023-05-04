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
		window.location.href = "/cameras"
	});

	var icon_search =  `<svg class="btn-icon" height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 96 960 960"><path d="M180 975q-24 0-42-18t-18-42V312h60v603h474v60H180Zm120-120q-24 0-42-18t-18-42V235q0-24 18-42t42-18h440q24 0 42 18t18 42v560q0 24-18 42t-42 18H300Zm0-60h440V235H300v560Zm0 0V235v560Z"/></svg>`
	var icon_excel = `<svg class="btn-icon" height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 50 50"><path d="M 28.875 0 C 28.855469 0.0078125 28.832031 0.0195313 28.8125 0.03125 L 0.8125 5.34375 C 0.335938 5.433594 -0.0078125 5.855469 0 6.34375 L 0 43.65625 C -0.0078125 44.144531 0.335938 44.566406 0.8125 44.65625 L 28.8125 49.96875 C 29.101563 50.023438 29.402344 49.949219 29.632813 49.761719 C 29.859375 49.574219 29.996094 49.296875 30 49 L 30 44 L 47 44 C 48.09375 44 49 43.09375 49 42 L 49 8 C 49 6.90625 48.09375 6 47 6 L 30 6 L 30 1 C 30.003906 0.710938 29.878906 0.4375 29.664063 0.246094 C 29.449219 0.0546875 29.160156 -0.0351563 28.875 0 Z M 28 2.1875 L 28 6.53125 C 27.867188 6.808594 27.867188 7.128906 28 7.40625 L 28 42.8125 C 27.972656 42.945313 27.972656 43.085938 28 43.21875 L 28 47.8125 L 2 42.84375 L 2 7.15625 Z M 30 8 L 47 8 L 47 42 L 30 42 L 30 37 L 34 37 L 34 35 L 30 35 L 30 29 L 34 29 L 34 27 L 30 27 L 30 22 L 34 22 L 34 20 L 30 20 L 30 15 L 34 15 L 34 13 L 30 13 Z M 36 13 L 36 15 L 44 15 L 44 13 Z M 6.6875 15.6875 L 12.15625 25.03125 L 6.1875 34.375 L 11.1875 34.375 L 14.4375 28.34375 C 14.664063 27.761719 14.8125 27.316406 14.875 27.03125 L 14.90625 27.03125 C 15.035156 27.640625 15.160156 28.054688 15.28125 28.28125 L 18.53125 34.375 L 23.5 34.375 L 17.75 24.9375 L 23.34375 15.6875 L 18.65625 15.6875 L 15.6875 21.21875 C 15.402344 21.941406 15.199219 22.511719 15.09375 22.875 L 15.0625 22.875 C 14.898438 22.265625 14.710938 21.722656 14.5 21.28125 L 11.8125 15.6875 Z M 36 20 L 36 22 L 44 22 L 44 20 Z M 36 27 L 36 29 L 44 29 L 44 27 Z M 36 35 L 36 37 L 44 37 L 44 35 Z"/></svg>`
	var icon_print = `<svg class="btn-icon" height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 96 960 960"><path d="M658 408V276H302v132h-60V216h476v192h-60Zm-518 60h680-680Zm599 95q12 0 21-9t9-21q0-12-9-21t-21-9q-12 0-21 9t-9 21q0 12 9 21t21 9Zm-81 313V684H302v192h356Zm60 60H242V760H80V514q0-45.05 30.5-75.525Q141 408 186 408h588q45.05 0 75.525 30.475Q880 468.95 880 514v246H718v176Zm102-236V513.785Q820 494 806.775 481 793.55 468 774 468H186q-19.55 0-32.775 13.225Q140 494.45 140 514v186h102v-76h476v76h102Z"/></svg>`
	var icon_pdf = `<svg class="btn-icon" height="20" width="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 96 960 960"><path d="M331 625h37v-83h48q15.725 0 26.362-10.638Q453 520.725 453 505v-48q0-15.725-10.638-26.362Q431.725 420 416 420h-85v205Zm37-120v-48h48v48h-48Zm129 120h84q15 0 26-10.638 11-10.637 11-26.362V457q0-15.725-11-26.362Q596 420 581 420h-84v205Zm37-37V457h47v131h-47Zm133 37h37v-83h50v-37h-50v-48h50v-37h-87v205ZM260 856q-24 0-42-18t-18-42V236q0-24 18-42t42-18h560q24 0 42 18t18 42v560q0 24-18 42t-42 18H260Zm0-60h560V236H260v560ZM140 976q-24 0-42-18t-18-42V296h60v620h620v60H140Zm120-740v560-560Z"/></svg>`
	
	$("#cameras_table thead tr").clone(true).addClass('filters').appendTo("#cameras_table thead");

	$("#cameras_table").DataTable({
		paging: true,
		pageLength: 10,
		lengthChange: true,
		autoWidth: false,
		searching: true,
		bInfo: true,
		bSort: true,
		"columnDefs": [{
			"targets": [5, 6, 7],
			"orderable": false,
		}],

		initComplete: function () {
			var api = this.api();
			api.columns([ 1, 2, 3, 4,]).eq(0).each(function (col_idx) {
				var cell = $(".filters th").eq($(api.column(col_idx).header()).index());
				var title = $(cell).text();
				$(cell).html("<input type='text' placeholder='" + title + "'/>");

				$("input", $(".filters th").eq($(api.column(col_idx).header()).index())).off("keyip change").on("keyup change", function (e) {
					e.stopPropagation();
					$(this).attr("title", $(this).val());
					var regexr = "({search})";
					var cursorPosition = this.selectionStart;
					api.column(col_idx).search(
						this.value != "" ? regexr.replace("{search}", "(((" + this.value + ")))") : "",
						this.value != "",
						this.value == ""
					).draw();

					$(this).focus()[0].setSelectionRange(cursorPosition, cursorPosition);
				});

			});
			api.columns([ 0, 5, 6, 7 ]).eq(0).each(function (col_idx) {
				var cell = $(".filters th").eq($(api.column(col_idx).header()).index());
				$(cell).html("");
			});
		},

		dom: 'Bfrltip',
		buttons: [
			{
				extend: 'copy', text: icon_search, className: 'btn btn-dark btn-sm', titleAttr: 'Copiar',
				exportOptions: { columns: [ 1, 2, 3, 4 ] },
			},
			{
				extend: 'excel', text: icon_excel, className: 'btn btn-dark btn-sm', titleAttr: 'Exportar xlsx',
				exportOptions: { columns: [1, 2, 3, 4] },
			},
			{
				extend: 'print', text: icon_print, className: 'btn btn-dark btn-sm', titleAttr: 'Imprimir',
				exportOptions: { columns: [1, 2, 3, 4] },
				customize: function (win) {
					$(win.document.body).css('font-size', '10pt');
					$(win.document.body).fin('table').addClass('compact').css('font-size', 'inherit');
				},
			},
			{
				extend: 'pdf', text: icon_pdf, className: 'btn btn-dark btn-sm', titleAttr: 'Exportar pdf',
				exportOptions: { columns: [1, 2, 3, 4] },
				tableHeader: {
					alignment: 'center',
				},
				customize: function (doc) {
					doc.styles.tableHeader.alignment = 'center';
					doc.styles.tableBodyEven.alignment = 'center';
					doc.styles.tableBodyOdd.alignment = 'center';
					doc.defaultStyle.fontSize = 6;
					doc.styles.tableHeader.fontSize = 7;
					doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1).join('*').split('');
				},
			},
		],
	});
	
	$("#searchInTable").keyup(function () {
		$("#cameras_table").DataTable().search($(this).val()).draw();
	})
	nums = $("#cameras_table_info").text().split(" ")[1] + "," + $("#cameras_table_info").text().split(" ")[3];
	console.log(nums);
});