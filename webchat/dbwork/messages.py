import webchat.models as db
from django.db.models import Q


def open_chat(user , opponent):

    #ищем id пользователя 
    user_id = db.User.objects.filter(login = user)[0].id

    #ищем id собеседника
    opponent_id = db.User.objects.filter(login = opponent)[0].id

    #ищем чат в бд
    chat = db.Chat.objects.filter(Q(User_id_1=user_id) & Q(User_id_2=opponent_id))
    
    #пробуем по другому
    if not chat:
        chat = db.Chat.objects.filter(Q(User_id_1=opponent_id) & Q(User_id_2=user_id))
    
    # если все таки не нашли то создаем
    if not chat:
        chat = db.Chat()
        chat.User_id_1 = user_id
        chat.User_id_2 = opponent_id
        chat.save()
        return(False , [])
    #если все таки нашли то грузим сообщения
    else:
        messages = db.Message.objects.filter(chat_id=chat[0].id)
        temp = []
        for i in messages:

            login = db.User.objects.filter(id=i.user_id)[0].login
            text = i.body
            if login == user:
                me = 'self'
            else:
                me = ''

            temp.append({
                'login' : login,
                'text' : text,
                'self' : me
            })

        return(True , temp)


def save_message(user , opponent , text):
    # ищем chat_id
    #ищем id пользователя 
    user_id = db.User.objects.filter(login = user)[0].id

    #ищем id собеседника
    opponent_id = db.User.objects.filter(login = opponent)[0].id

    #ищем чат в бд
    chat = db.Chat.objects.filter(Q(User_id_1=user_id) & Q(User_id_2=opponent_id))
    
    #пробуем по другому
    if not chat:
        chat = db.Chat.objects.filter(Q(User_id_1=opponent_id) & Q(User_id_2=user_id))

    message = db.Message()
    message.user_id = user_id
    message.chat_id = chat[0].id
    message.body = text
    message.save()

    return (True , 'Сообщение сохранено')


def get_messages_from_users(user , opponent):

    messages = db.Message.objects.filter(Q(user_id=user) & Q(opponent_id=opponent))

    if not messages:
       messages = db.Message.objects.filter(Q(user_id=opponent) & Q(opponent_id=user)) 
    response = []
    
    for i in messages:
        temp = {}
        if i.user_id == user:
            temp['self'] = 'self'
        else:
           temp['self'] = 'noself' 
        
        temp['login'] = i.user_id
        temp['text'] = i.body

        response.append(temp)

    print(response)
    return response
