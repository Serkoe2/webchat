//первый рендер страницы
function render_message(data){
    console.log(data)
    data[1].forEach( element =>  {
        $(`<div class="user ${element['self']}">        \
        <div class="wrapper">                           \
        <div class="logo"></div>                        \
        <div class="login">${element['login']} </div>   \
        </div>                                          \
        <div class="message">${element['text']}</div>   \
        </div>`).appendTo('.window_chat')  
    } );
   
}

function load_data(){
    $.ajax({
        url : document.location.href,
        type: "POST",
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
        data : { query: 'render'},
        dataType : "json",
        success: function(response) {
            render_message(response)
        },
        })
}

//добавление сообщения
function add_message(e){
    data = $('.send').value
    $.ajax({
        url : document.location.href,
        type: "POST",
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
        data : { query: 'add_message' , message:  $('textarea')[0].value },
        dataType : "json",
        success: success
        })
}

function success(response){
    $(`<div class="user self">                      \
    <div class="wrapper">                           \
    <div class="logo"></div>                        \
    <div class="login">${response}</div>                           \
    </div>                                          \
    <div class="message">${ $('textarea')[0].value } </div>   \
    </div>`).appendTo('.window_chat')  
    
    $('textarea')[0].value = ''
}

$(document).ready (function () {
// При загрузке страницы рендерим данные
$('.send').bind('click' , add_message )
load_data()
})



