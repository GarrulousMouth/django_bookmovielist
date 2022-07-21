// Отключение элемента
$(`#id_elems-bookmovieid`).prop('disabled', true);

$('#id_elems-chapter').change(function () {
    // Получение элемента
    let send_data = this.value;
    // Включение элемента
    $(`#id_elems-bookmovieid`).prop('disabled', false);
    // Получение первого элемента с последующим удалением, если значение равно пустой строке
    let emptyElem = $(`#id_elems-bookmovieid`).find(':first-child');
    if (emptyElem.val() === '') {
        emptyElem.remove()
    }
    // Отключение элемента, если значение другого равно пустой строке
    if (this.value === '') {
        $(`#id_elems-bookmovieid`).prop('disabled', true);
    }
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
            // Список ключей элементов и названий, полученных с сервера
            let elems = {}
            for (let elem of json) {
                elems[elem.pk] = elem.fields.name
            }


            // let elemsBookmovieid = $('#id_elems-bookmovieid>option')
            // for (let i of elemsBookmovieid) {
            //     // Если элемент отсутствует в массиве
            //     if (jQuery.inArray(+i.value, elems) == -1) {
            //         $('#id_elems-bookmovieid').find(`option[value=${i.value}]`).hide();
            //     }

            // Удалених всех дочерних элементов
            $('#id_elems-bookmovieid').empty()
            // Добавление элементов
            for(let val in elems) {
                $('#id_elems-bookmovieid').append(`<option value="${val}">${elems[val]}</option>`)
            }
            // Выбор первого элемента
            $(`#id_elems-bookmovieid option[value=${elems[0]}]`).prop('selected', true)
        },
        error: function() {
            console.log('Сервер не ответил')
        }
    })
})