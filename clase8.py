# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 18:24:03 2023

@author: Usuario
"""

import emoji
#Crear una cadena de texto con emojis
mensaje = "¡Hola! :smiley: Esto es un ejemplo :thumbsup:"
#Imprimir la cadena con emojis
print(emoji.emojize(mensaje))
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', language='alias'))
print(emoji.emojize("Python is fun :red_heart:"))
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))