from zad3.mail_server import MailServer
from zad3.template_engine import TemplateEngine


class Messenger:

    def __init__(self, client_id):
        if not isinstance(client_id, str):
            raise TypeError('Id must be of string type!')

        self.client_id = client_id
        self.mail_server = MailServer()
        self.template_engine = TemplateEngine()

    def send_message(self, to_id, message):
        if not (isinstance(to_id, str) and isinstance(message, str)):
            raise TypeError('Input must be of string type!')

        return self.mail_server.send(self.template_engine.write(to_id, message))

    def receive_message(self, from_id):
        if not isinstance(from_id, str):
            raise TypeError('Id must be of string type!')

        return self.mail_server.receive(from_id)
