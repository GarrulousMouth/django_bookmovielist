$(function() {
    $('#id_elems-year_of_issue').datepicker({
        changeYear: true,
        showButtonPanel: true,
        dateFormat: 'yy',
        onClose: function(dateText, inst) { 
            var year = $("#ui-datepicker-div .ui-datepicker-year :selected").val();
            $(this).datepicker('setDate', new Date(year, 1));
        }
    });
$("#id_elems-year_of_issue'").focus(function () {
        $(".ui-datepicker-month").hide();
    });
});

$(`#id_elems-bookmovieid`).prop('disabled', true);

$('#id_elems-chapter').change(function () {
    // Получение элемента
    let send_data = this.value;
    $(`#id_elems-bookmovieid`).prop('disabled', false);
    // Отпрвка ajax запроса
    $.ajax({
        url: "current",
        method: 'get',
        dataType: 'json',
        data: {send_data: send_data},
        success: function(data) {
            // Парсинг JSON
            let json = JSON.parse(data);
            // Показ всех элементов списка
            $(`#id_elems-bookmovieid`).find('option').show()
            let elems = []
            for (let elem of json) {
                elems.push(elem.pk)
            }
            // Сокрытие ненужных элементов
            for (let i of elems) {
                $(`#id_elems-bookmovieid option[value=${i}]`).hide()
            }
        },
        error: function() {
            console.log('Сервер не ответил')
        }
    })
})