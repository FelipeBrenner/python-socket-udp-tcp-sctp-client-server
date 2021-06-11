import socket
import sctp
import time
from time import sleep

protocol = ''
while True:
    protocol = input('Digite o protocolo desejado (TCP, UDP ou SCTP): ')
    if protocol in ('TCP','UDP','SCTP'):
        break

hostServer = input('Digite o IP do servidor: ')
port = 8000
address = (hostServer,port)

if protocol == 'TCP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)  
elif protocol == 'UDP':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     
elif protocol == 'SCTP':
        sock = sctp.sctpsocket_tcp(socket.AF_INET)
        sock.connect(address)

print('\n1 - Envia em sequência uma contagem de 1 a 10000')
print('grafico - Exibir no servidor o gráfico dos dados recebidos')
print('dc - Desligar o cliente')
print('dcs - Desligar o cliente e o servidor\n')

while True:
    i = input('Digite uma mensagem ou um comando: ')

    if i == '1':
        ini = time.time()
        for j in range(1,10000):
            if protocol == 'TCP':
                sock.send(str.encode(str(j)))
                # sleep(0.001)
            elif protocol == 'UDP':
                sock.sendto(str.encode(str(j)), address)
            elif protocol == 'SCTP':
                sock.sctp_send(str(j))
                sock.shutdown(0)
        fim = time.time()
        print('Envio levou %.2f segundos' % (fim - ini))
    elif i == 'dc':
        break
    else:
        if protocol == 'TCP':
            sock.send(str.encode(i))
        elif protocol == 'UDP':
            sock.sendto(str.encode(i), address)
        elif protocol == 'SCTP':
            sock.sctp_send(i)
            sock.shutdown(0)

        if i == 'dcs':
            break

sock.close()
