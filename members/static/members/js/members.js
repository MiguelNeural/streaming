$(document).ready(function () {
    $("#saveMember_btn").click(function (e) {
        e.preventDefault();
        form = $("#createMember_form");
        console.log($("#newRole_field"));
        console.log(form);
        if (form[0].checkValidity()) {
            console.log("Is valid");
            form.submit();
        } else {
            console.log("Is not valid");
            form.each(function () {
                let inputs = $("#createMember_form :input");
                inputs.each(function () {
                    if (!this.validity.valid) {
                        $(this).next(".invalid-feedback").text(this.validationMessage).addClass("d-block");
                    } else {
                        $(this).next(".invalid-feedback").removeClass("d-block");
                    }
                });
            });
        }
    });
    
    function isNumber(n) { return /^-?[\d.]+(?:e-?\d+)?$/.test(n); } 
	
	if (isNumber(this.URL.split('/')[4]) && this.URL.split('/')[3]=='members') {
        const memberJson = JSON.parse($("#memberJSON").val())[0];
        console.log(memberJson.fields.role);
		$("#id_field").val(memberJson.pk);
		$("#editName_field").val(memberJson.fields.name);
        $("#editPassword_field").val(memberJson.fields.password);
        $('#editRole_field option[value="' + memberJson.fields.role + '"]').prop('selected', true);

		$("#editMemberModal").modal("show");
    }
    
    $("#editMember_btn").click(function (e) {
		e.preventDefault();
		form = $("#editMember_form");
		if (form[0].checkValidity()) {
			form.submit();
		}
		else {
			form.each(function () {
				let inputs = $("#editMember_form :input");
				inputs.each(function () {
					if (!this.validity.valid) {
						$(this).next(".invalid-feedback").text(this.validationMessage).addClass("d-block");
					} else {
						$(this).next(".invalid-feedback").removeClass("d-block");
					}
				});
			});
		}
	});
});