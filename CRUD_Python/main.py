import sys


clients = [
    {
        'ID' : 1,
        'name' : 'Pablo',
        'company' : 'Google',
        'email' : 'pablo@google.com',
        'position' : 'Software Engineer',
    }
]


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
        print('Created Client!')       
    else:
        print('Client already is in the client\'s list')


def update_client(client, update_client):
    global clients

    if client in clients:
        index = clients.index(client)
        clients[index] = update_client                 
    else:
        False


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print(f'{client_name} is not in the client\'s list')


def search_client(client_id):
    global clients

    for client in clients:
        if client['ID'] == client_id:
            return client
        else:
            continue
    return False


def list_clients():

    for client in (clients):
        print(f"{client['ID']} / {client['name']} / {client['company']} / {client['email']} / {client['position']}")


def _get_client_id():
    client_id = None

    while not client_id:
        client_id = int(input('What is the ID of the client? '))

        if client_id == 'exit':
            client_id = None
            break
    if not client_id:
        sys.exit()

    return client_id


def _get_client_field(field_name):
    field = None

    while not field:
        field = input(f'What is the client {field_name}? ')

        if field == 'exit':
            field = None
            sys.exit()

    return field


def _print_welcome():
    print('*' * 25)
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 25)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[E]xit Platzi Ventas')


if __name__ == '__main__':


    _print_welcome()
    while True:
        
        command = input()
        command = command.upper()
        
        if command == 'C':
            client = {
                'ID' : len(clients)+1,
                'name' : _get_client_field('name'),
                'company' : _get_client_field('company'),
                'email' : _get_client_field('email'),
                'position' : _get_client_field('position'),                
            }
            create_client(client)

        elif command == 'L':
                list_clients()

        elif command == 'U':
        
            client_id = _get_client_id()
            client = search_client(client_id)

            if client:
                print(f"{client['ID']} / {client['name']} / {client['company']} / {client['email']} / {client['position']}")
                print("Update client: ")
                
                client['name'] = _get_client_field('name')
                client['company'] = _get_client_field('company')
                client['email'] = _get_client_field('email')
                client['position'] = _get_client_field('position')

                print('Updated Client')
                
            else:
                print(f"{client_id} is not in the client's list")
        
        elif command == 'D':
        
            client_id = _get_client_id()
            client = search_client(client_id)

            if client:
                print(f"{client['ID']} / {client['name']} / {client['company']} / {client['email']} / {client['position']}")
                print((f"Are you sure of delete to client ID {client_id}? "))
                print("[Y]es")
                print("[N]o")
                alert = input()
                alert = alert.upper()

                if alert == 'Y':
                    clients.remove(client)
                    print('Deleted Client.')
                elif alert == 'N':
                    pass
                else:
                    print(f'Te command {alert} is invalid.')
            
        elif command == 'S':
        
            client_id = _get_client_id()
            client = search_client(client_id)
            
            if client:
                print(f"{client['ID']} / {client['name']} / {client['company']} / {client['email']} / {client['position']}")
            else:
                print(f"{client_id} is not in the client's list")

        elif command == 'E':
            print('We see you soon!')
            sys.exit()
        
        elif command == 'M' or 'MENU':
            _print_welcome()

        else:
            print('Invalid command.')
        
    
    
    