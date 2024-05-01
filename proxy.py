import zmq

def broker():
  context = zmq.Context()
  frontend = context.socket(zmq.XSUB)
  backend = context.socket(zmq.XPUB)
  
  #frontend.subscribe("")

  frontend.bind("tcp://*:10000")
  backend.bind("tcp://*:10100")

  try:
    print("Proxy activado")
    zmq.proxy(frontend=frontend, backend=backend)
  except KeyboardInterrupt:
    pass
  finally:
    frontend.close()
    backend.close()
    context.term()

if __name__ == "__main__":
    broker()