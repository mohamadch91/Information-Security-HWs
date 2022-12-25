from multiprocessing import connection
from dataclasses import *

import socket
import json
import threading
import time
import random
from _thread import *

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
    return connection.recv(2048).decode()


#accept client connection
def accept_client(s :socket) -> connection:
    """accept client connection

    Args:
        s (Socket): Socket object to accept client connection

    Returns:
        Coonection,address: Socket connection between client and server, client ip and port
    """
    connection, address = s.accept()
    print('Connection from: ' + str(address))
   
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
            value2=value[key2]
            print(value2)
def input_data() -> dict:
    """input data

    Returns:
        dict: input data
    """
    data={}
    data["command"]=input("Enter command: ")
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
            input=input_data()
            input=json_convert(input)
            send_command(connection,input)
            data = recieve_data(connection)
            data = json_parser(data)
            print_data(data)
            time.sleep(random.randint(1,10))
        except:           
            connection.close()
            break    

#main
if __name__== '__main__':
    print("server started at port 45678")
    server=create_server('0.0.0.0',45679)
    
    while True:
        connection,address=accept_client(server)        
        # print_lock.acquire()
        start_new_thread(accpet_client_data, (connection,))
        
        
