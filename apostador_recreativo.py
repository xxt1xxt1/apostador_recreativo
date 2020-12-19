import requests
from time import sleep
from bs4 import BeautifulSoup
import telepot
from telepot.loop import MessageLoop


def run(): 
    #urls = "https://m.livesoccertv.com/pt-br/match/3329101/leicester-city-vs-west-ham-united/"
    urls = "https://m.livesoccertv.com/pt-br/match/3715728/rennes-vs-bordeaux/"
    p = requests.get(urls) 
    sou = BeautifulSoup(p.text, 'html.parser')
    r = sou.get_text()
    nome= urls[46:]
    for a in range(100):
        for b in range(100):
            for n in ["Final"]:
                if f"{a or n}\n\n\n\nFinal\n\n \n\n\n\n\n" in r:
                    sl= f"🕘{a or n}"   
    
    for a in range(100):
        for b in range(100):
            if f"\n\n\n\n\n{a} : {b}\n\n\n\n" in r:
                tt= f"⚽Placar: {a} X {b}"       
        
    for a in range(100):
        for b in range(100):
            if f"Estatísticas\nEventos\n\n\n\n\n{a}\n\n\n\n\n\n\nPosse de bola, %\n\n\n\n\n\n\n{b}\n" in r:
                t= f"💹Posse de bola {a}%-{b}%"          
                
    for a in range(100):
        for b in range(100):
            if f"\n{a}\n\n\n\n\n\n\nChutes\n\n\n\n\n\n\n{b}\n\n" in r:
                t1= f"🔘Chutes Total: {a}-{b}"           
                
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nChutes no alvo\n\n\n\n\n\n\n{b}\n\n" in r:
                t2= f"🎯Chutes no alvo: {a}-{b}"          
                
                
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nFouls\n\n\n\n\n\n\n{b}\n\n" in r:
                t3= f"📍Falta: {a}-{b}"
                               
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nCantos\n\n\n\n\n\n\n{b}\n\n" in r:
                t5= f"⛳Cantos: {a}-{b}"
               
                
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nCartões amarelos\n\n\n\n\n\n\n{b}\n\n" in r:
                t6= f"☡Cartão Amarelo: {a}-{b}"                         
                
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nCartões vermelhos\n\n\n\n\n\n\n{b}\n\n" in r:
                t7= f"🔴Cartão Vermelho: {a}-{b}"               
                
    for a in range(100):
        for b in range(100):
            if f"\n\n{a}\n\n\n\n\n\n\nDefesas\n\n\n\n\n\n\n{b}\n\n\n\n\n\n\nEstatísticas\n" in r:
                t8= f"🛡Defesas: {a}-{b}"
    
    #return f"\n{nome}\n{sl}\n{tt}\n{t}\n{t1}\n{t2}\n{t3}\n{t5}\n{t6}\n{t7}\n{t8}"
    return f"\n{nome}\n{tt}\n{t}\n{t1}\n{t2}\n{t3}\n{t5}\n{t6}\n{t7}\n{t8}"       
  
    #return f"{nome}"

def enviarMsg(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, f'Olá {msg["chat"]["first_name"]}\nsou o rôbo 🤖 para Aposta recreativa\n \n⚽JOGOS AO VIVO🕒\n{time1}\n')
    #bot.sendMessage(chat_id, f'Olá  {msg["chat"]["first_name"]}\n{time1}')



#bot = telepot.Bot('1042579294:AAFnwnLs4b9equhsHmA5MLSwHoH63DM8WgA')
bot = telepot.Bot('1065119614:AAHboPzLbH24addYDnykT5-zyqkoSiPqJIs')

if __name__ == "__main__":
    time1= run()
    
    MessageLoop(bot,enviarMsg).run_as_thread()
    while 1: 
        sleep(10)
    
  
