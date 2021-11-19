$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-paramprixemballage').modal('show');
            },
            success: function(data){
                $('#modal-paramprixemballage .modal-content').html(data.html_form);
            }
        });
    };
    var SaveForm = function() {
        var form = $(this);
        $.ajax({
            url: form.attr('data-url'),
            data: form.serialize(),
            type: form.attr('method'),
            dataType: 'json',
            success: function(data) {
                if(data.form_is_valid) {
                    $('#table-paramprixemballage tbody').html(data.paramembal);
                    $('#modal-paramprixemballage').modal('hide');
                } else {
                    $('#modal-paramprixemballage .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-paramprixemballage').on("submit", ".create-form", SaveForm);

// Update form
$('#table-paramprixemballage').on("click", ".show-form-update", ShowForm);
$('#modal-paramprixemballage').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-paramprixemballage').on("click", ".show-form-delete", ShowForm);
$('#modal-paramprixemballage').on("submit", ".delete-form", SaveForm);

});