$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-embal').modal('show');
            },
            success: function(data){
                $('#modal-embal .modal-content').html(data.html_form);
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
                    $('#table-embal tbody').html(data.embal);
                    $('#modal-embal').modal('hide');
                } else {
                    $('#modal-embal .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-embal').on("submit", ".create-form", SaveForm);

// Update form
$('#table-embal').on("click", ".show-form-update", ShowForm);
$('#modal-embal').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-embal').on("click", ".show-form-delete", ShowForm);
$('#modal-embal').on("submit", ".delete-form", SaveForm);

});