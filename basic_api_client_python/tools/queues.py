from basic_api_client_python.response import Response


class Queues:
    def __init__(self, basicApi) -> None:
        self.basicApi = basicApi
        
    def clearMessagesQueue(self) -> Response:
            'The method is aimed for clearing the queue of messages to be sent.'

            return self.basicApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/ClearMessagesQueue/{{apiTokenInstance}}')

    def showMessagesQueue(self) -> Response:
            'The method is aimed for getting a list of messages in the queue '\
            'to be sent. Messages sending rate is managed by Messages sending '\
            'delay parameter.'

            return self.basicApi.request('GET', 
                '{{host}}/waInstance{{idInstance}}'
                '/ShowMessagesQueue/{{apiTokenInstance}}')