import socket
import sctp
from matplotlib import pyplot as plt

protocol = ''
while True:
    protocol = input('Digite o protocolo desejado (TCP, UDP ou SCTP): ')
    if protocol in ('TCP','UDP','SCTP'):
        break

host = socket.gethostname()
port = 8000
address = (host,port)
buffer = 1024

if protocol == 'TCP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(address)
        sock.listen()
elif protocol == 'UDP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(address)
elif protocol == 'SCTP':
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.bind(address)
        sock.listen(1)

data = ''

x = [] 
y = []
counter = 0

if protocol == 'UDP':
    # Aguarda mensagens
    print ('Aguardando mensagens...')

while True:
    if protocol in ('TCP','SCTP'):
        # Aguarda uma conexão
        print ('Aguardando uma conexão...')
        connection, client_address = sock.accept()
        # Mostra quem conectou
        print ('Cliente conectado: ', client_address)

    while True:
        if protocol in ('TCP','SCTP'):
            data = connection.recv(buffer).decode('UTF-8')
        elif protocol == 'UDP':
            bytesAddressPair = sock.recvfrom(buffer)
            data = bytesAddressPair[0].decode('UTF-8')
            client_address = bytesAddressPair[1]

        if data == 'dcs':
            print('Servidor desconectado.')
            break
        elif data == '2':
            plt.plot(x,y)
            plt.show()
        elif data:
            # Exibe os dados recebidos
            if protocol in ('TCP','SCTP'):
                print ("Mensagem recebida: ", data)
            elif protocol == 'UDP':
                print ("Mensagem recebida: ", data, " Cliente: ", client_address)
            
            # Armazena os pacotes recebidos para exibir no gráfico
            try:
                y.append(int(data))
                counter+=1
                x.append(counter)
            except:
                False
        elif protocol in ('TCP','SCTP'):
            # Quando cliente desconecta
            print ("Cliente desconectado.")
            break

    if data == 'dcs':
        if protocol in ('TCP','SCTP'):
            # Clean up the connection
            connection.close()
        break