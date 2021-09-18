CONNECTED_CLIENTS_DICT = {}
ROOMS = {}


def connect_client(user):
    CONNECTED_CLIENTS_DICT[user['platform']] = user

def get_connected_clients():
    return list(CONNECTED_CLIENTS_DICT.values())

def remove_connected_client(id):
    try:
        CONNECTED_CLIENTS_DICT.pop(id)
    except:
        pass