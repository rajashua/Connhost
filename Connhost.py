from socket import *
from os import *
from sys import argv
from threading import Thread

IP = argv[0]
Port = argv[1]

DB = {}

s = ""
conn, addr = ""

def Main():
  try:
    global s
    global conn
    global addr
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((IP, Port))
    conn, addr = s.accept()
  except:
    print(f"{IP} not found")
    
def Send():
  try:
    while True:
      Command = input(DB[Directory])
      conn.send(Command).encode()
  except:
    print("Error")
    
def Recv():
  try:
    while True:
      global DB
      Data = conn.recv(1024).decode()
      DB = Data
      if not DB[Result] == "":
        print(DB[Result])
  except:
    print("Error")
    
t = Thread(target=Recv)
t.start()


t2 = Thread(target=Send)
t2.start()
