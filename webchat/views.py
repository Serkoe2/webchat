from django.shortcuts import render  , redirect
from django.http import HttpResponse , HttpResponseRedirect

import json
from . import dbwork

def index(request):

    if request.method == 'GET':

        key = request.session.get('site')
        if key:
            result = dbwork.user.check_session(key)
            if result[0]:
                #отправляем в личный кабинет
                return redirect('main/')
            elif result[1] == 'not found':
                return render(request , 'index.html')
            elif result[1] == 'ban':
                return render(request , 'ban.html')

        else:
            return render(request , 'index.html')

    elif request.method == 'POST':
        data = {}
        data['login'] = request.POST.get('login')
        data['password'] = request.POST.get('password')
    
        status = dbwork.user.authUser(data)
        if not status[0]:
            
            if status[1] == 'ban':
                return render(request , 'ban.html')
            else:
                return render(request , 'index.html', { 'message' : status[1]})
        else:
            #response = HttpResponseRedirect('/webchat/main/')
            #response.set_cookie('site' , status[1])
            request.session['site'] = status[1]
            return redirect('main/')   


def reg(request):

    if request.method == 'POST':
        data = {}
        data['login'] = request.POST.get('login')
        data['password'] = request.POST.get('password')
        
        status = dbwork.user.regUser(data)
        
        if not status[0]:
            return render(request , 'registration.html', { 'message' : status[1]})

        request.session['site'] = status[1]
        return redirect('/webchat/main/')
    
    return render(request , 'registration.html')

def main(request):
    print("------------------------")
    key = request.session.get('site')
    print(key)
    #нет ключа
    if not key:
        return redirect('/webchat/')

    login = dbwork.user.check_session(key)
    #нет сессии в бд
    if not login[0]:
        return redirect('/webchat/')

    if request.method == 'GET':
        chats = dbwork.user.get_chats(login[1])
        print(chats)
        return render(request , 'app.html' , {'name' : login[1] , 'chats': chats})

    elif request.method == 'POST':
        data = request.POST.get('finder')
        resp = dbwork.user.find_user(data)
        print(resp)
        return HttpResponse(json.dumps(resp))

def chat(request , id):
    key = request.session.get('site')
    #нет ключа
    if not key:
        return redirect('/webchat/')   

    login = dbwork.user.check_session(key)
    #нет сессии в бд
    if not login[0]:
        return redirect('/webchat/')
    
    if request.method == 'GET':

        return render(request , 'chat.html')

    if request.method == 'POST':
        query = request.POST.get('query')
        if query == 'render':
            #загрузить сообщения пользователей 
            data = dbwork.messages.open_chat(login[1] , id)
            print(data)
            return HttpResponse(json.dumps(data))

        elif query == 'add_message':
            message = request.POST.get('message')
            dbwork.messages.save_message(login[1] , id , message)

            return HttpResponse(json.dumps(login[1]))
    
def logout(request):
        request.session['site'] = ''
        return redirect('/webchat')  

    
