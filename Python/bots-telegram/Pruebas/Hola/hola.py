# -*- coding: utf-8 -*-
 
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
 
TOKEN = ''
 
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
#############################################
#Listener
def listener(messages): 
    for m in messages: 
        if m.content_type == 'text': 
            cid = m.chat.id 
	    respuesta = responder(m.text)
	    if respuesta:
            #print "[" + str(cid) + "]: " + m.text
		bot.send_message(cid,respuesta)
 
bot.set_update_listener(listener) 
#############################################
#Funciones

@bot.message_handler(commands=['foto'])
def command_foto(m):
    cid = m.chat.id
    bot.send_photo( cid, open( 'david.jpeg', 'rb')) 
 
@bot.message_handler(commands=['iee'])
def command_iee(m): 
    cid = m.chat.id 
    bot.send_message( cid, 'ieeeee!') 


def responder(mensaje):
	textos = { '5': 'Por el culo te la hinco!', 'iee': 'ieeeee!', 'hola': 'calla!' }
	respuesta = textos[mensaje]
	return respuesta
#############################################
#Peticiones
bot.polling(none_stop=True) 
