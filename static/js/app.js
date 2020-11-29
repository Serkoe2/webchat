function find(){
    console.log('-----------')
    q = $('.submit-input')[0].value

    $.ajax({
        url : '/webchat/main/',
        type: "POST",
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value },
        data : { finder : q},
        dataType : "json",
        success: success,
        })
    
}
function success(response){
    if (response[0]) {
        $(`<div class="wrapper_find">  \
        <a href="/webchat/chat/${response[1]}" class="get_chat">${response[1]}</a> \
        </div>`).appendTo(".find")
    } else {
        alert(response[1])
    }
    
}

$('.submit').bind('click' , find)