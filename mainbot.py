from pickle import TRUE
from sre_constants import NEGATE
from webbrowser import get
import vk_api , json
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload
from config import main_token


vk_session = vk_api.VkApi(token = main_token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def getbutton(text , color):
    return {
                "action":{
                    "type" : "text",
                    "payload" : "{\"button\" : \"" + "1" + "\"}",
                    "label" : f"{text}"
                },
                "color" : f"{color}"
            }

keyboard = {
    "one_time" : False,
    "buttons" : [
        [getbutton('Хочу начать заниматься баскетболлом!', 'positive'), getbutton('Информация по вопросам рекламы', 'positive')],
        [getbutton('Составы команд чемпионата', 'positive'), getbutton('Наши контакты', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii= False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


basketboard = {
    "one_time" : False,
    "buttons" : [
        [getbutton('Мужской' , 'positive') , getbutton('Женский' , 'secondary')]
        
    ]
}
basketboard = json.dumps(basketboard, ensure_ascii= False).encode('utf-8')
basketboard = str(basketboard.decode('utf-8'))


marketboard = {
    "one_time" : False,
    "buttons" :[
        [getbutton('Пост на стену в группе' , 'positive') , getbutton('Что-то ещё' , 'positive')]
    ]
}
marketboard = json.dumps(marketboard, ensure_ascii= False).encode('utf-8')
marketboard = str(marketboard.decode('utf-8'))


commandsboard = {
    "one_time" : False,
    "buttons": [
        [getbutton('Авангард' , 'positive') , getbutton('Зарево' , 'positive')],
        [getbutton('Авангард' , 'positive') , getbutton('Зарево' , 'positive')]
    ]
}
commandsboard = json.dumps(commandsboard , ensure_ascii = False).encode('utf-8')
commandsboard = str(commandsboard.decode('utf-8'))
 

def sender(id,text):
    vk_session.method('messages.send', {'user_id' : id , 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})
    
def basketsender(id ,text):
    vk_session.method('messages.send', {'user_id':id ,'message':text , 'random_id' : 0 , 'keyboard' : basketboard})
    
def marketsender(id , text):
    vk_session.method('messages.send' , {'user_id': id ,'message' :text , 'random_id' : 0, 'keyboard' : marketboard})

def commandsender(id , text):
    vk_session.method('messages.send' , {'user_id': id ,'message' :text , 'random_id' : 0, 'keyboard' : commandsboard})
    
def photosender(id ,url):
    vk.messages.send(user_id = id , attachment = url, random_id = 0)
    
def commandmembers():
        if message == "Авангард" :
            f = open("Couches.txt")
            a = f.read()
            sender(id, a)
            photosender(id , "photo-123243743_457262583")    
        if message == "Зарево" :
            f = open("Couches.txt")
            a = f.read()
            sender(id , a)
            photosender(id , "photo-123243743_457262632")        

print("Начинаю работать с вами!")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.message
            id = event.user_id
            
            if message == "+start":
                sender(id , "Приветствуем , ниже вы можете увидеть список действий , котороые можно произвести со мной!")
            elif message == "Хочу начать заниматься баскетболлом!" :
                basketsender(id , "Ниже вам нужно будет выбрать ваш пол")
            elif message == "Мужской" :
                sender(id , "Следующим сообщением я вам отправлю наших тренеров , а так же их контакты")
                f = open("Couches.txt")
                a = f.read()
                sender(id , a) 
            #if message == "Женский" :
            elif message == "Информация по вопросам рекламы" : 
                marketsender(id ,"Ниже вам нужно будет выбрать тип рекламы, которая вас интерисует")
            elif message == "Пост на стену в группе":
                sender(id , "Ниже прикрепите информацию о том , что вы хотите у нас прорекламировать , я пока напишу моим руководителям!")
                sender(269316818 ," @id269316818(Данил), вам пришло новое сообщение о рекламе, проверьте личные сообщение группы!")
                #sender(233935675, "@id233935675(Дарья), вам пришло новое сообщение о рекламе, проверьте личные сообщение группы!")
                # sender(id , "Мы уведомили наших руководителей о вас , ожидайте ответа!")
                # sender(269316818 , "Вам пришло новое сообщение о рекламе, проверьте личные сообщение группы!")        
            elif message == "Составы команд чемпионата" :
                commandsender(id , "Ниже представлены составы комманд чемпионата , выберите одну из них")
            commandmembers()
                