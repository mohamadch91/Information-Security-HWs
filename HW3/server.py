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
def send_data(connection:connection,json : json) -> None:
    """send data to client connected

    Args:
        connection (connection): Socket connection between client and server
        json (json): data to send
    """
    connection.send(json.encode())
# receive data from client
def recive_data(connection: connection) -> json:
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

def accpet_client_data(connection : connection) -> None:
    """accept client data
    Args:
        connection (connection): Socket connection between client and server
    
    Returns:
        None
    """
    while True:
        try:
            data = recive_data(connection)
            data = json_parser(data)
            for key in data:
                value=data[key]
                for key2 in value:
                    value2=value[key2]
                    print(value2)
            
            time.sleep(random.randint(1,10))
        except:           
            connection.close()
            break    

#main
if __name__== '__main__':
    print("server started at port 45678")
    server=create_server('0.0.0.0',45678)
    
    while True:
        connection,address=accept_client(server)        
        # print_lock.acquire()
        start_new_thread(accpet_client_data, (connection,))
        
        
