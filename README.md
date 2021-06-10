## Comandos

```bash
# subir docker container
docker run --rm -it \
   --workdir=/app \
   --volume="$PWD":/app \
   gcc
```

```bash
# instalar as dependências
apt-get update
apt-get upgrade
apt-get install python3-dev
apt-get install libsctp-dev
apt-get install python3-setuptools
python3 setup.py install
apt-get install python3-matplotlib
```

```bash
# consultar o IP
hostname -i
```

```bash
# executar o código do servidor
python3 server.py
# executar o código do cliente
python3 client.py
```

```bash
# se quiser testar gerando tráfego para interferência para analisar os comportamentos

# instalar o iperf
apt-get install iperf3
# rodar o iperf no servidor
# <port> qualquer porta disponível
iperf3 -s -p <port>
# rodar o iperf no cliente
# <host_server> é o IP do servidor
# <port> é a porta que aparecerá no prompt do servidor ao rodar o comando anterior, exemplo:
# Server listening on 9000
iperf3 -f m -i 1 -t 10 -c <host_server> -p <port>
```

## Referências

- [pysctp](https://github.com/P1sec/pysctp)
- [SCTP in Python](https://nickvsnetworking.com/sctp-in-python/)
- [UDP - Client And Server Example Programs In Python](https://pythontic.com/modules/socket/udp-client-server-example)
- [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
- [Matplotlib - Usage Guide](https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py)
- [Using GUI's with Docker](http://wiki.ros.org/docker/Tutorials/GUI)
- [Running GUI Applications inside Docker Containers](https://medium.com/@SaravSun/running-gui-applications-inside-docker-containers-83d65c0db110)
- [How can I use matplotlib.pyplot in a docker container?](https://stackoverflow.com/questions/46018102/how-can-i-use-matplotlib-pyplot-in-a-docker-container)