from basic_api_client_python import API as API

API_HOST = 'API_HOST'
ID_INSTANCE = 'ID_INSTANCE'
API_TOKEN_INSTANCE = 'API_TOKEN_INSTANCE'

basicAPI = API.BasicApi(ID_INSTANCE, API_TOKEN_INSTANCE, API_HOST)

def main():
    chatIds = [
        "11001234567@c.us"
    ]
    resultCreate = basicAPI.groups.createGroup('GroupName', 
        chatIds)

    if resultCreate.code == 200:
        print(resultCreate.data)
        resultSend = basicAPI.sending.sendMessage(resultCreate.data['chatId'], 
            'Message text')
        if resultSend.code == 200:
            print(resultSend.data)
        else:
            print(resultSend.error)    
    else:
        print(resultCreate.error)

if __name__ == "__main__":
    main()