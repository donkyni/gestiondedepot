$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-pertesrembourser').modal('show');
            },
            success: function(data){
                $('#modal-pertesrembourser .modal-content').html(data.html_form);
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
                    $('#table-pertesrembourser tbody').html(data.remboursement);
                    $('#modal-pertesrembourser').modal('hide');
                } else {
                    $('#modal-pertesrembourser .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Update form
$('#table-pertesrembourser').on("click", ".show-form-update", ShowForm);
$('#modal-pertesrembourser').on("submit", ".update-form", SaveForm);


});