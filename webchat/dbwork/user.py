import webchat.models as db
from django.db.models import Q
import random
import secrets
import os
import json



#регистрация
def regUser(data):
    user = db.User()
    user.login = data['login']
    user.password = data['password']

    #есть ли такой пользователь?
    check = db.User.objects.filter(login = data['login'])
    if check:
        return (False , "Такой пользователь существует")

    #добавление пользователя
    key = user.add_session()
    user.save()

    return (True , key)

#авторизация
def authUser(data):
    user = db.User()
    user.login = data['login']
    user.password = data['password']
    
    #есть ли такой пользователь?
    check = db.User.objects.filter(login = data['login'])
    if not check:
        return (False , "Пользователь не существует")
    
    #проверка пароля и бана
    if check[0].check_passwd(data['password']):  
    #установка сессии
        if check[0].check_ban():
                return(False , 'ban')

        key = str(secrets.token_hex())
        check.update(session_key = key)
        return ('True' , key)
    else:
        return ('False' , "Неправильный пароль")
    
def check_session(key):
    # Есть ли такая сессия
    user = db.User.objects.filter(session_key = key)
    if user:
        if user[0].check_ban():
            return(False , 'ban')
        return (True , user[0].login)
    else:
        return (False , 'not found')
    
def find_user(login):
    check = db.User.objects.filter(login = login)
    if not check:
        return (False , "Такого пользователя нет")
    else:
        return (True , login)
    
def get_chats(login):
    user_id = db.User.objects.filter(login=login)[0].id
    print(user_id)
    #поулчаем все чаты с дублями
    chats = db.Chat.objects.filter(Q(User_id_1=user_id) | Q(User_id_2=user_id))
    #убрать дубли
    template = []
    for i in chats:
        if not i.id in template:
            template.append(i)
    chats = template
    # получить определенные значения
    # список логинов
    logins = []
    for i in chats:
        if i.User_id_1 == i.User_id_2:
            logins.append(login)
        elif i.User_id_1 == user_id:
            logins.append(db.User.objects.filter(id=i.User_id_2)[0].login)
        else:
            logins.append(db.User.objects.filter(id=i.User_id_1)[0].login)
    return logins






    