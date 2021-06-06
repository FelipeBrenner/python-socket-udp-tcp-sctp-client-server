import socket
import sctp
from matplotlib import pyplot as plt

host = socket.gethostname()
port = 8000

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.bind((host, port))
sock.listen(1)

data = ''

x = [] 
y = []
counter = 0

while True:  
    # Aguarda uma conexão
    print ('Aguardando uma conexão...')
    connection, client_address = sock.accept()

    try:
        # Mostra quem conectou
        print ('Cliente conectado: ', client_address)
        # Recebe os dados em small chunks e os exibe
        while True:
            data = connection.recv(999).decode('UTF-8')

            if data == 'dcs':
                break
            if data == '2':
                print(x)
                print(y)
                plt.plot(x,y)
                plt.show()
            elif data:
                # Exibe os dados recebidos
                print ("Mensagem recebida: %s" % data)
                # Armazena para exibir no gráfico se vier inteiro
                try:
                    y.append(int(data))
                    counter+=1
                    x.append(counter)
                except:
                    False
            else:
                # Quando cliente desconecta
                print ("Cliente desconectado.")
                break
    finally:
        # Clean up the connection
        connection.close()

    if data == 'dcs':
        print('Servidor desconectado.')
        break