import zmq
import json
import time

context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:10100")
print("Suscribiendo")
socket.subscribe("NumerosOperar")
print("Suscrito, esperando mensajes")

socketOp1 = context.socket(zmq.PUB)
socketOp1.connect("tcp://127.0.0.1:10000")

socketOp2 = context.socket(zmq.PUB)
socketOp2.connect("tcp://127.0.0.1:10000")

suscriOp1 = context.socket(zmq.SUB)
suscriOp1.connect("tcp://127.0.0.1:10100")
suscriOp1.subscribe("ResOp1")

suscriOp2 = context.socket(zmq.SUB)
suscriOp2.connect("tcp://127.0.0.1:10100")
suscriOp2.subscribe("ResOp2")

def conectOp1(num):
    socketOp1.send_string("numOp1", flags=zmq.SNDMORE)
    socketOp1.send_json(num)
    resultadoOp1 = suscriOp1.recv_multipart()
    print("El resultado de la suma es: ", resultadoOp1)    

def conectOp2(num):
    socketOp2.send_string("numOp2", flags=zmq.SNDMORE)
    socketOp2.send_json(num)
    resultadoOp2 = suscriOp2.recv_multipart()
    print("Eol resultado de la suma es: ". resultadoOp2)

while True: 
    resultado = socket.recv_multipart() 
    #valor de resultado:[b'NumerosOperar', b'{"A": 1, "B": 2, "C": 3, "D": 4}']
    print("Recibi el mensaje")
    elementoLista = resultado[1]
    #elementoLista:b'{"A": 1, "B": 2, "C": 3, "D": 4}'
    elementoLista.decode("utf-8")
    #elementoLista: '{"A": 1, "B": 2, "C": 3, "D": 4}'
    decodificado = elementoLista
    #decodificado: '{"A": 1, "B": 2, "C": 3, "D": 4}'
    objeto = json.loads(decodificado)
    #objeto: {"A": 1, "B": 2, "C": 3, "D": 4}
    print("Enviando mensajes a los operadores")
    dicOp1 = {
        "A": objeto["A"],
        "B": objeto["B"]
    }
    resulOp1 = conectOp1(dicOp1)
    dicOp2 = {
        "C": objeto["C"],
        "D": objeto["D"]
    }
    resulOp2 = conectOp2(dicOp2)
    resulF = resulOp1 * resulOp2
    socketDos = context.socket(zmq.PUB)
    print("Conectando")
    socketDos.connect("tcp://127.0.0.1:10000")
    print("Conectado!")
    time.sleep(0.1)
    socketDos.send_string("Resulf", flags=zmq.SNDMORE)
    socketDos.send_json(resulF)






