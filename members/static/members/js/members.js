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
});