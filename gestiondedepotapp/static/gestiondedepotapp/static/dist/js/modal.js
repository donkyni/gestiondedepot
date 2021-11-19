$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-site').modal('show');
            },
            success: function(data){
                $('#modal-site .modal-content').html(data.html_form);
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
                    $('#table-site tbody').html(data.site);
                    $('#modal-site').modal('hide');
                } else {
                    $('#modal-site .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-site').on("submit", ".create-form", SaveForm);

// Update form
$('#table-site').on("click", ".show-form-update", ShowForm);
$('#modal-site').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-site').on("click", ".show-form-delete", ShowForm);
$('#modal-site').on("submit", ".delete-form", SaveForm);

});