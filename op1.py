import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:10100")
print("Suscribiendo")
socket.subscribe("numOp1")
print("Suscrito, esperando mensajes")

socketDos = context.socket(zmq.PUB)
socketDos.connect("tcp://127.0.0.1:10000")

while True: 
    resultado = socket.recv_multipart() 
    print("Recibí: ", resultado)
    print("Recibi el mensaje")
    elementoLista = resultado[1]
    elementoLista.decode("utf-8")
    decodificado = elementoLista
    objeto = json.loads(decodificado)
    sum = objeto["A"] + objeto["B"]
    sum = str(sum)
    print("El resultado de la suma es:", sum)
    socketDos.send_string("ResOp1", flags= zmq.SNDMORE)
    socketDos.send_string(sum)
