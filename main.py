import discord
import os
import search_english
from dotenv import load_dotenv
from flask import Flask
from threading import Thread
import search_latin
import logging 
from variables import *




app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

# Use python-dotenv pakcage to get variables stored in .env file of your project
load_dotenv()

client = discord.Client()




# instantiate RunPeeWeb class from search_runpee.py
english = search_english.English()

latin = search_latin.Latin()



url = "https://en.wiktionary.org/wiki/Appendix:"
tags = ["#Present", "#Imperfect", "#Future"]
conj = ["blank", "Latin_first_conjugation", "Latin_second_conjugation", "Latin_third_conjugation", "Latin_fourth_conjugation"]

if not os.path.isdir('./logs'):
    os.mkdir('./logs')
    
logging.basicConfig(level=logging.INFO, filename="./logs/dictionarium.log", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Vote for Robertus'))
    
    print(f'{client.user} is now online!')
    logging.info(f'{client.user} has connected to Discord')
    
    


@client.event
async def on_message(message): 
  if message.author == client.user:
      return  
    
  author = message.author
  m_name = author.name
  # lower case message
 

 
      
  # lower case message
  message_content = message.content.lower()  

  if message.content.startswith(f'$imp'):
    await message.channel.send(imperative)

  if message.content.startswith(f'$voc'):
    await message.channel.send(vocative)

  if message.content.startswith(f'$nom'):
      await message.channel.send(nominative)

  if message.content.startswith(f'$gen'):
      await message.channel.send(genitive)

  if message.content.startswith(f'$dat'):
      await message.channel.send(dative)

  if message.content.startswith(f'$acc'):
      await message.channel.send(accusative)

  if message.content.startswith(f'$datType'):
      await message.channel.send(dativeType)

  if message.content.startswith(f'$abl'):
      await message.channel.send(ablative)

 
  if message.content.startswith(f'$hello'):
    await message.channel.send(hello_message)


  if message.content.startswith(f'$commands'):
       await message.channel.send(commands_message)


  if message.content.startswith(f'$help'):
       await message.channel.send(help_message)
       
  if message.content.startswith(f'$first'):
    Url = url + conj[1]
    await message.channel.send(Url)
    
  if message.content.startswith(f'$second'):
    Url = url + conj[2]
    await message.channel.send(Url)
    
  if message.content.startswith(f'$third'):
    Url = url + conj[3]
    await message.channel.send(Url)
    
  if message.content.startswith(f'$fourth'):
    Url = url + conj[4]
    await message.channel.send(Url)




  if f'$latin' in message_content:
    key_words, search_words = latin.key_words_search_words(message_content)
    result_links = latin.search(key_words)
    search_words = f"**{search_words}**"
    logs = f"{search_words} requested by {m_name}"
    links = latin.send_link(search_words, result_links)

    if len(links) > 0:
      logging.info(f'{logs}')
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)
       
  if f'$english' in message_content:

    key_words, search_words = english.key_words_search_words(message_content)
    result_links = english.search(key_words)
    logs = f"{search_words} requested by {m_name}"
    search_words = f"**{search_words}**"
    links = english.send_link(search_words, result_links)

 
    
    if len(links) > 0:
      logging.info(f'{logs}')
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)






client.run(os.getenv('TOKEN'))