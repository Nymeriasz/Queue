class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Fila vazia")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Fila vazia")
            return None
        
queue = Queue()

queue.enqueue(15)
queue.enqueue(24)
queue.enqueue(25)

print("Início da fila:", queue.peek())
print("Elemento desenfileirado:", queue.dequeue())  
print("Elemento desenfileirado:", queue.dequeue()) 

print("Início da fila:", queue.peek())
print("Elemento desenfileirado:", queue.dequeue())
print("Elemento desenfileirado:", queue.dequeue())