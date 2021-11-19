$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-fournisseur').modal('show');
            },
            success: function(data){
                $('#modal-fournisseur .modal-content').html(data.html_form);
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
                    $('#table-fournisseur tbody').html(data.fournisseur);
                    $('#modal-fournisseur').modal('hide');
                } else {
                    $('#modal-fournisseur .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-fournisseur').on("submit", ".create-form", SaveForm);

// Update form
$('#table-fournisseur').on("click", ".show-form-update", ShowForm);
$('#modal-fournisseur').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-fournisseur').on("click", ".show-form-delete", ShowForm);
$('#modal-fournisseur').on("submit", ".delete-form", SaveForm);

});