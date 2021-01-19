import random 
import os
import time
import socket
import linecache
import threading

address = ('localhost', 9000)
answer = random.randint(0, 1000)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(15)
server_socket.settimeout(5)

def run(server_input, index):
  while True:
    current_turn = "1"
    server_input.sendall(current_turn.encode("utf-8"))
    time.sleep(.200)
    response = server_input.recv(1024)
    response = response.rstrip()
    current_number = int(response.decode())
    print("Player", index, "Attempt")
    print(current_number)
    print()
    state = ""
    if current_number == answer:
      state = "0"
    elif current_number > answer:
      state = "1"
    elif current_number < answer:
      state = "2"
    server_input.sendall(state.encode("utf-8"))
    time.sleep(.200)
    if current_number == answer:
      print("Player", index, "wins!")
      break

def main():
  index = 1
  print("Server Started!")
  print()
  print("Number:")
  print(answer)
  print()
  while True:
    try:
      server_input, address = server_socket.accept()
      print("New Connection Found!")
      print()
      thread = threading.Thread(target = run, args = (server_input, index,))
      thread.start()
      index = index + 1
    except socket.timeout:
      pass	

main()