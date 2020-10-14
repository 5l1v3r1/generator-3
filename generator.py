#!/usr/bin/python3
#PROYECTO 2020-2021
#Creado por Osososo

#Github:https://github.com/oscarsanchezt

#Colores 

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#
import random, os, webbrowser
import time

def borrarpant():
    if os.name == "nt":
        os.system ("clear")
    else:
        os.system ("clear")

#Logo ASCII

borrarpant()
print(RED+"◉ INICIANDO GENERADOR..."+RESET)
time.sleep(2)
print("")
print(GREEN+"✔ INICIADO CORRECTAMENTE"+RESET)
time.sleep(1)
borrarpant()
time.sleep(2)
print(RED+"")
print("      ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄   ")
print("     ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █· ")
print("     ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄  ")
print("     ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌ ")
print("     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀ "+RESET)
print(RED+"                        Random(rev1.0)"+RESET)
print("")
print (MAGENTA+"         ========== > By Osososo < ========== "+RESET)
print (GREEN+"                   Cancelar Ctrl+c"+RESET)
print (" ")


        
length=int(input (YELLOW+"> Longitud de Contraseña: "+RESET))

print ("")
time.sleep(2)

print (CYAN+"     ✔ CONTRASEÑA GENERADA "+RESET)
print (" ")
time.sleep(1)

char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"

password= (RED+"║⊗ Contraseña:║ "+RESET)
print(RED+"╔═════════════╗"+RESET)

for i in range(length):

     password+=random.choice(char)


print(password)
print(RED+"╚═════════════╝"+RESET)

print ("")
quit()