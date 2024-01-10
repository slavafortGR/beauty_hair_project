document.getElementById('json_file_input').addEventListener('change', function() {
    let form = document.getElementById('config_form');
    let isFileSelected = !!this.files.length;

    Array.from(form.elements).forEach(function(input) {
        if (input.name.startsWith('gcal_')) {
            input.required = !isFileSelected;
        }
    });
});
