import threading
data= []
def consumir_cpu():
    while True:
        pass
def consumir_ram():
    while True:
        data.append("X" * 1000000)
for i in range (4):
    threading.Thread(target=consumir_cpu).start()
consumir_ram()
