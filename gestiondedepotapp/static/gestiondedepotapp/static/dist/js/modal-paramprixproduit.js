$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-paramprixproduit').modal('show');
            },
            success: function(data){
                $('#modal-paramprixproduit .modal-content').html(data.html_form);
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
                    $('#table-paramprixproduit tbody').html(data.paramprixproduit);
                    $('#modal-paramprixproduit').modal('hide');
                } else {
                    $('#modal-paramprixproduit .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-paramprixproduit').on("submit", ".create-form", SaveForm);

// Update form
$('#table-paramprixproduit').on("click", ".show-form-update", ShowForm);
$('#modal-paramprixproduit').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-paramprixproduit').on("click", ".show-form-delete", ShowForm);
$('#modal-paramprixproduit').on("submit", ".delete-form", SaveForm);

});