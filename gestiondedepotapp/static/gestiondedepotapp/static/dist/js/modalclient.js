$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-client').modal('show');
            },
            success: function(data){
                $('#modal-client .modal-content').html(data.html_form);
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
                    $('#table-client tbody').html(data.client);
                    $('#modal-client').modal('hide');
                } else {
                    $('#modal-client .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-client').on("submit", ".create-form", SaveForm);

// Update form
$('#table-client').on("click", ".show-form-update", ShowForm);
$('#modal-client').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-client').on("click", ".show-form-delete", ShowForm);
$('#modal-client').on("submit", ".delete-form", SaveForm);

});