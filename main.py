clients = 'pablo,ricardo,'


def creatClient(clientName):
    global clients
    
    if clientName not in clients:
        clients += clientName
        _addComma()
    else:
        print('El cliente ya esta en la lista de clientes')


def listClients():
    global clients
    
    print(clients)


def _addComma():
    global clients
    
    clients += ','


def _printWelcome():
    print('BIENVENIDO AL PROGRAMA DE VENTAS')
    print('*' * 50)
    print('¿Que quieres hacer hoy?')
    print('[C]rear cliente')
    print('[E]liminar cliente')

if __name__ == '__main__':
    _printWelcome()
    
    command = input()
    
    if command == 'C':
        clientName = input('¿Cual es el nombre del cliente? ')
        creatClient(clientName)
        listClients()
        
    elif command == 'E':
        pass
    
    else:
        print('Comando invalido. Porfavor digite un comando correcto')