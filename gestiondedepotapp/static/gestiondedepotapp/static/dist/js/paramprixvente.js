$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-paramprixvente').modal('show');
            },
            success: function(data){
                $('#modal-paramprixvente .modal-content').html(data.html_form);
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
                    $('#table-paramprixvente tbody').html(data.paramprixvente);
                    $('#modal-paramprixvente').modal('hide');
                } else {
                    $('#modal-paramprixvente .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-paramprixvente').on("submit", ".create-form", SaveForm);

// Update form
$('#table-paramprixvente').on("click", ".show-form-update", ShowForm);
$('#modal-paramprixvente').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-paramprixvente').on("click", ".show-form-delete", ShowForm);
$('#modal-paramprixvente').on("submit", ".delete-form", SaveForm);

});