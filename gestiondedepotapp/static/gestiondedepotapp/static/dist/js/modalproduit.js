$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-produit').modal('show');
            },
            success: function(data){
                $('#modal-produit .modal-content').html(data.html_form);
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
                    $('#table-produit tbody').html(data.produit);
                    $('#modal-produit').modal('hide');
                } else {
                    $('#modal-produit .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-produit').on("submit", ".create-form", SaveForm);

// Update form
$('#table-produit').on("click", ".show-form-update", ShowForm);
$('#modal-produit').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-produit').on("click", ".show-form-delete", ShowForm);
$('#modal-produit').on("submit", ".delete-form", SaveForm);

});