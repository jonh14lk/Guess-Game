import socket

def main():
  print("Welcome to Guess Game!")
  print("Your mission is to recover the beautiful number X")
  print()
  address = ('localhost', 2000)
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(address)
  print("Connection Was Found!")
  print("")
  while True:
    response = client_socket.recv(1024)
    response = response.rstrip()
    is_turn = response.decode()
    if is_turn == "1":
      print("Type a number that belongs to range [0, 1000]")
      text = input()
      client_socket.sendall(text.encode('utf-8'))
      response = client_socket.recv(1024)
      response = response.rstrip()
      current_state = response.decode()
      if current_state == "0": 
        print("X =", text)
        print()
        print("Congratulations!")
        print("You Win!")
        break
      elif current_state == "1":
        print("X <", text)
        print()
      elif current_state == "2":
        print("X >", text)
        print()

main()