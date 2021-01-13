from uuid import uuid4


class Subscriber:

    def __init__(self):
        self.clients = []

    def add_client(self, f_name, l_name):
        if not (isinstance(f_name, str) and isinstance(l_name, str)):
            raise TypeError('Input must be of string type!')

        self.clients.append({
            'id': str(uuid4()),
            'name': {'first': f_name, 'last': l_name},
            'mailbox': {
                'sent': [],
                'received': []
            }
        })
        return True

    def get_ids(self):
        return [client['id'] for client in self.clients]

    def remove_client(self, client_id):
        if not isinstance(client_id, str):
            raise TypeError('Input must be of string type!')

        if not any(client['id'] == client_id for client in self.clients):
            return ValueError('Id does not exists!')

        self.clients = [client for client in self.clients if client.get('id') != client_id]
        return True

    def send_message(self, from_id, to_id, message):
        if not (isinstance(from_id, str) and isinstance(to_id, str) and isinstance(message, str)):
            raise TypeError('Input must be of string type!')

        if not message:
            raise ValueError('Message can not be empty!')

        if not all(client_id in self.get_ids() for client_id in [from_id, to_id]):
            raise ValueError('Id does not exists!')

        for client in self.clients:
            if client['id'] == from_id:
                client['mailbox']['sent'].append({
                    'from': from_id,
                    'to': to_id,
                    'message': message
                })
            elif client['id'] == to_id:
                client['mailbox']['received'].append({
                    'from': from_id,
                    'to': to_id,
                    'message': message
                })
        return True
