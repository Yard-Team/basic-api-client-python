from os import environ

from whatsapp_api_client_python import API

ID_INSTANCE = environ['ID_INSTANCE']
API_TOKEN_INSTANCE = environ['API_TOKEN_INSTANCE']

restApi = API.RestApi('https://api.green-api.com', 
                        ID_INSTANCE, 
                        API_TOKEN_INSTANCE)

def API():
    restApi.sending.sendMessage('120363025955348359@g.us', 'Message text')

if __name__ == "__main__":
    API()