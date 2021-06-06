import socket

hostname = socket.gethostname()
port = 8000
buffer = 1024

# Create a UDP socket at client side

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((hostname, port))

# Aguarda mensagens
print ('Aguardando mensagens...')

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(buffer)

    data = bytesAddressPair[0].decode('UTF-8')
    address = bytesAddressPair[1]

    # Recebe os dados em small chunks e os exibe
    if data == 'dcs':
        print('Servidor desconectado.')
        break
    elif data:
        # Exibe o dado recebido e o cliente que mandou
        print ("Mensagem recebida: ", data, " Cliente: ", address)