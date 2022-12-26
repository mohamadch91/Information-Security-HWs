# AUT information security course HomeWorke 3

## Description

This project is a simple client-server python CLI tool to get OS data from a client and send it to a server.

## Requirements

- Python 3.6 or higher
- pip3

## Installation

```bash
pip3 install -r requirements.txt
```

## Usage

### Server

```bash
python3 server.py
```

### Client

```bash
python3 client.py
```


## Code structure

### Server

The server is a simple python script that listens to a port and accepts connections from clients. When a client connects, the server reads the data sent by the client and prints it to the console.

### Client

The client is a simple python script that connects to a server and sends the data it collects to the server. The data is collected using the `psutil` ,`platform` ,`cpuinfo` library.

data collecting in [data_getter.py](data_getter.py) file.

