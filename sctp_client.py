import socket
import sctp

hostnameServer = "172.17.0.3"
port = 8000

sock = sctp.sctpsocket_tcp(socket.AF_INET)
sock.connect((hostnameServer, port))

print('\n1 - Envia em sequência os números de 1 a 10000')
print('2 - Exibir no servidor o gráfico dos dados recebidos')
print('dc - Desligar o cliente')
print('dcs - Desligar o cliente e o servidor\n')

while True:
    i = input('Digite uma mensagem ou um comando: ')

    if i == '1':
        for j in range(1,10000):
            sock.sctp_send(str(j))
            sock.shutdown(0)
    elif i == 'dc':
        break
    else:
        sock.sctp_send(i)
        sock.shutdown(0)

        if i == 'dcs':
            break

sock.close()
