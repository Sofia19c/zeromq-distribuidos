import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)

socketDos = context.socket(zmq.SUB)
socketDos.connect("tcp://127.0.0.1:10100")
socketDos.subscribe("Resulf")

print("Conectando")
socket.connect("tcp://127.0.0.1:10000")
print("Conectado!")

A = input("Por favor ingrese  el primer digito: ")
A = int (A)
B = input("Por favor ingrese  el segundo digito: ")
B = int(B)
C = input("Por favor ingrese  el tercer digito: ")
C = int(C)
D= input("Por favor ingrese  el cuarto digito: ")
D = int(D)
d1 = {
  "A": A,
  "B": B,
  "C": C,
  "D": D 
} 
print("Enviando Msg")
time.sleep(0.1)
socket.send_string("NumerosOperar", flags=zmq.SNDMORE)
socket.send_json(d1)
socket.close()

resultado = socketDos.recv_multipart()

resultado = resultado[1]
resultado.decode()
resultado = int(resultado)
print("El resultado final es: ", resultado)
context.term()


