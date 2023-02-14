from whatsapp_api_client_python.response import Response

class Journals:
    def __init__(self, basicApi) -> None:
        self.basicApi = basicApi
        
    def getChatHistory(self, chatId: str, count: str) -> Response:
            'The method returns the chat message history.'

            requestBody = {
                'chatId': chatId,
                'count': count,
            }

            return self.basicApi.request('POST', 
                '{{host}}/waInstance{{idInstance}}'
                '/GetChatHistory/{{apiTokenInstance}}',
                requestBody)

    def lastIncomingMessages(self) -> Response:
            'The method returns the chat message history.'

            return self.basicApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/LastIncomingMessages/{{apiTokenInstance}}')

    def lastOutgoingMessages(self) -> Response:
            'The method returns the last outgoing messages of the account.'
            'Outgoing messages are stored on the server for 24 hours.'

            return self.basicApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/LastOutgoingMessages/{{apiTokenInstance}}')