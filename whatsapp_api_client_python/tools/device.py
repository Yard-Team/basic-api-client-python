from whatsapp_api_client_python.response import Response


class Device:
    def __init__(self, basicApi) -> None:
        self.basicApi = basicApi
        
    def getDeviceInfo(self) -> Response:
            'The method is aimed for getting information about the device '\
            '(phone) running WhatsApp Business application.'
            
            return self.basicApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetDeviceInfo/{{apiTokenInstance}}')