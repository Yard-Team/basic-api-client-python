from basic_api_client_python import API as API

API_HOST = 'API_HOST'
ID_INSTANCE = 'ID_INSTANCE'
API_TOKEN_INSTANCE = 'API_TOKEN_INSTANCE'

basicAPI = API.BasicApi(ID_INSTANCE, API_TOKEN_INSTANCE, API_HOST)

def main():
    result = basicAPI.sending.sendFileByUrl('11001234567@c.us', 
        'https://www.google.ru/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', 
        'googlelogo_color_272x92dp.png', 'Google logo')
    print(result.data)

if __name__ == "__main__":
    main()