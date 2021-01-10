from socket import *

print("\n\nGhiceste cifrul \n\n")
print("Se face conexiunea cu serverul...\n")

# Set up the socket as an Internet facing streaming socket
clientsocket = socket(AF_INET, SOCK_STREAM)
# Connect to the server on port 4000
try:
    clientsocket.connect(('localhost', 4000))
except ConnectionRefusedError:
    print("Conexiunea a fost refuzata.")
    exit(0)
print("Conectat!\n")
# Send the greeting message to the server, as specified by the requirements
message = "Buna\r\n"
clientsocket.send(message.encode('ascii'))
# Wait for a response, then print said response to the console
response = clientsocket.recv(1024)
print(response.decode('ascii'))

running = 1

while running:
    # Ask for user to guess a number
    guess = input("Introduceti raspunsul: ")
    # Format the guess, ready to send to the server
    guessstring = "Raspuns: " + str(guess) + "\r\n"
    # Send the guess
    clientsocket.send(guessstring.encode('ascii'))

    # Wait for the response from the server
    response = clientsocket.recv(1024).decode('ascii')
    print(response)

    # Determine if the game is over
    if (response == "Correct\r\n"):
        running = 0

clientsocket.close()
