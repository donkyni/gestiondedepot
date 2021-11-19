$(document).ready(function(){
    var ShowForm = function(){
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $('#modal-tabledepotstock').modal('show');
            },
            success: function(data){
                $('#modal-tabledepotstock .modal-content').html(data.html_form);
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
                    $('#table-tabledepotstock tbody').html(data.depot);
                    $('#modal-tabledepotstock').modal('hide');
                } else {
                    $('#modal-tabledepotstock .modal-content').html(data.html_form)
                }
            }
        })
        return false;
    };

// Create a form
$(".show-form").click(ShowForm);
$('#modal-tabledepotstock').on("submit", ".create-form", SaveForm);

// Update form
$('#table-tabledepotstock').on("click", ".show-form-update", ShowForm);
$('#modal-tabledepotstock').on("submit", ".update-form", SaveForm);

// Delete form
$('#table-tabledepotstock').on("click", ".show-form-delete", ShowForm);
$('#modal-tabledepotstock').on("submit", ".delete-form", SaveForm);

});