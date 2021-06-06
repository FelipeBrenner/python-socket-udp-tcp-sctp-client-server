import socket
import sctp

hostnameServer = "172.17.0.3"
port = 8000
buffer = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print('\n1 - Envia em sequência os números de 1 a 10000')
print('2 - Exibir no servidor o gráfico dos dados recebidos')
print('dc - Desligar o cliente')
print('dcs - Desligar o cliente e o servidor\n')

while True:
    i = input('Digite uma mensagem ou um comando: ')

    if i == '1':
        for j in range(1,10000):
            UDPClientSocket.sendto(str.encode(str(j)), (hostnameServer,port))
    elif i == 'dc':
        break
    else:
        UDPClientSocket.sendto(str.encode(i), (hostnameServer,port))

        if i == 'dcs':
            break
