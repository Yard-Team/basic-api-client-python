from basic_api_client_python.response import Response


class Marking:
    def __init__(self, basicApi) -> None:
        self.basicApi = basicApi
        
    def readChat(self, chatId: str, idMessage: str) -> Response:
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'idMessage': idMessage,
            }

            return self.basicApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/ReadChat/{{apiTokenInstance}}',
                requestBody)