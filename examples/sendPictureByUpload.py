from basic_api_client_python import API as API

ID_INSTANCE = '1101000001'
API_TOKEN_INSTANCE = '3e03ea9ff3324e228ae3dfdf4d48e409bfa1b1ad0b0c46bf8c'

basicAPI = API.BasicApi(ID_INSTANCE, API_TOKEN_INSTANCE)

def main():
    result = basicAPI.sending.sendFileByUpload('11001234567@c.us',
        "C:\\Games\\PicFromDisk.png",
        'PicFromDisk.png', 'Picture from disk')
    print(result.data)

if __name__ == "__main__":
    main()