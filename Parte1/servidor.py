import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index,delete,edit,error

CUR_DIR = Path(__file__).parent

SERVER_HOST = 'localhost'
SERVER_PORT = 8080

NOTE_TEMPLATE = '''  <li>
    <h3>{title}</h3>
    <p>{details}</p>
  </li>
'''

RESPONSE_TEMPLATE = '''HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="img/logo-getit.png">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{notes}
</ul>

</body>
</html>
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)

    filepath = CUR_DIR / route
    if filepath.is_file():
        if filepath.suffix == '.css':
            response = build_response(headers='Content-type: text/css; chrset=utf-8')+read_file(filepath)
        else:
            response = build_response() + read_file(filepath)
    elif route == '':
        response = index(request)
    elif route.startswith('delete'):
        id=int(route.split('/')[-1])
        response=delete(id)
    elif route.startswith('edit'):
        id=int(route.split('/')[-1])
        response=edit(request,id)

    else:
        response= error()

    client_connection.sendall(response)

    client_connection.close()
server_socket.close()