import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:10100")
print("Suscribiendo")
socket.subscribe("")
print("Suscrito, esperando mensajes")

while True: 
    resultado = socket.recv_multipart() 
    print("El resultado es: ", resultado)
    print("Recibi el mensaje")
    elementoLista = resultado[1]
    elementoLista.decode("utf-8")
    decodificado = elementoLista
    objeto = json.loads(decodificado)
    