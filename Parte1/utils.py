import json

def extract_route(request):
    string = ''
    start = False
    contagem = 0
    for i in request:
        if i == '/'and contagem == 0:
            start = True
            contagem = 1
        
        elif i == ' ':
            start = False

        elif start:
            string += i
    return string



def read_file(path):
    with open(path,mode='r+b') as file:
        return file.read()
    

def load_data(jsons):
    with open(f'Parte1/data/{jsons}',mode="r") as file:
        return (json.loads(file.read()))
    
def load_template(name):
    with open("Parte1/templates/" +(name),'r') as file:
        return (file.read())
    

def anota_json(params):
    with open("Parte1/data/notes.json","r+") as file:
        file_data=json.load(file)
        file_data.append(params)
        file.seek(0)
        json.dump(file_data,file,indent=4)

def build_response(body='', code=200, reason='OK', headers=''):
    status_line = f'HTTP/1.1{code}{reason}\n'
    response = f'{status_line}{headers}\n{body}'
    return response.encode()

            