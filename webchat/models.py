from django.db import models
import secrets

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    session_key = models.CharField(max_length=128) 

    def add_session(self):
        key = str(secrets.token_hex())
        self.session_key = key
        return key
    
    def check_passwd(self , passwd):
        if self.password == passwd:
            return True
        else:
            return False

    def __str__(self):
        return self.login

class Chat(models.Model):
    User_id_1 = models.IntegerField(default=0)
    User_id_2 = models.IntegerField(default=0)

        

    def __str__(self):
        return "{} {}".format(self.User_id_1 , self.User_id_2)

class Message(models.Model):
    chat_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

        

    def __str__(self):
        return "{} {}".format(self.User_id_1 , self.User_id_2)