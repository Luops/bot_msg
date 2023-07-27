from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas import api_hash, api_id
import threading
from flask import Flask, jsonify
from telethon.sync import TelegramClient
from telethon import events

app = Flask(__name__)

sessao = 'Repassar mensagem';
database_lock = threading.Lock()

@app.route('/enviar_mensagem', methods=['POST'])

def main():
    print('Monitorando mensagens...')
    client = TelegramClient(sessao, api_id, api_hash)
    client.on(events.NewMessage(chats = [868907524])) #Grupo que quer copiar
    async def enviar_mensagem(event):
        await client.send_message(919563201, event.raw_text) #Grupo que quer colar
    client.start()
    client.run_until_disconnected()
    return jsonify({'status': 'Mensagens estão sendo monitoradas e repassadas.'})

if __name__ == '__main__':
    app.run(debug=True)

#def obter_chats():
    
    #client = TelegramClient(sessao, api_id, api_hash)
    #client.start()
    #dialogs = client.get_dialogs()
    #for dialog in dialogs:
        #print('-------------------')
        #if dialog.id < 0:
            #print(f'Grupo: {dialog.title}')
            #print(f'ID: {dialog.id}')
        #else:
            #print(f'Nome: {dialog.title}')
            #print(f'ID: {dialog.id}')
        #print('-------------------')
    #client.disconnect()

#obter_chats()
