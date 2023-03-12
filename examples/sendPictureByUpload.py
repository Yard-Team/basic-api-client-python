from basic_api_client_python import API as API

API_HOST = 'API_HOST'
ID_INSTANCE = 'ID_INSTANCE'
API_TOKEN_INSTANCE = 'API_TOKEN_INSTANCE'

basicAPI = API.BasicApi(ID_INSTANCE, API_TOKEN_INSTANCE, API_HOST)

def main():
    result = basicAPI.sending.sendFileByUpload('11001234567@c.us',
        "C:\\Games\\PicFromDisk.png",
        'PicFromDisk.png', 'Picture from disk')
    print(result.data)

if __name__ == "__main__":
    main()