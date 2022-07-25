// Отключение элемента
$(`#id_elems-bookmovieid`).prop('disabled', true);

$('#id_elems-chapter').change(function () {
    // Получение элемента
    let send_data = this.value;
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
            // Список ключей элементов и названий, полученных с сервера
            let elems = {}
            for (let elem of json) {
                elems[elem.pk] = elem.fields.name
            }
            if (Object.keys(elems).length) {
                // Получение первого элемента с последующим удалением, если значение равно пустой строке
                let emptyElem = $(`#id_elems-bookmovieid`).find(':first-child');
                if (emptyElem.val() === '') {
                    emptyElem.remove()
                }
                // Включение элемента
                $(`#id_elems-bookmovieid`).prop('disabled', false);
                // Удалених всех дочерних элементов
                $('#id_elems-bookmovieid').empty()
                // Добавление элементов
                for(let val in elems) {
                    $('#id_elems-bookmovieid').append(`<option value="${val}">${elems[val]}</option>`)
                }
                // Выбор первого элемента
                $(`#id_elems-bookmovieid option[value=${elems[0]}]`).prop('selected', true)
            } else {
                // Отключение элемента, если пустой объект
                $(`#id_elems-bookmovieid`).prop('disabled', true);
            }
        },
        error: function() {
            console.log('Сервер не ответил')
        }
    })
})


$( document ).ready(function() {
    $('#create-chapter').click(function(event) {
        event.preventDefault();
        $('#formboxchapter').css('display', 'block').animate({ opacity: 1 }, 198)
    })

    $('#formboxchapter-close').click(function(event) {
        event.preventDefault();
        $('#formboxchapter').animate({ opacity: 0 }, 198, function() {
            $(this).css('display', 'none');
        })
    })
});

$( document ).ready(function() {
    $('#create-element').click(function(event) {
        event.preventDefault();
        $('#formboxelem').css('display', 'block').animate({ opacity: 1 }, 198)
    })

    $('#formboxelem-close').click(function(event) {
        event.preventDefault();
        $('#formboxelem').animate({ opacity: 0 }, 198, function() {
            $(this).css('display', 'none');
        })
    })
});