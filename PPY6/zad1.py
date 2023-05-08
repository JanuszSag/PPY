class Element:
    def __init__(self, data=None, nextE = None):
        self.data = data
        self.nextE = nextE
    def __str__(self):
        return str(self.data)

class MyLinkedList:
    head = None
    tail = None
    size = 0
    lista = list()

    def __init__(self):
        pass

    def __str__(self):
        result = ""
        for x in self.lista:
            result+=str(x)+", "
        return result[:-2]
    
    def __repr__(self):
        return self.__str__()
    
    #TODO uzupelnic func
    def push(self, e, func = None):
        if func is None:
            if self.head == None:
                self.head = Element(e)
            self.tail = Element(e)
            self.lista.append(self.tail)
            self.lista[self.size].nextE = self.tail
            self.size+=1
            

temp = MyLinkedList()
temp.push(5)
temp.push(3)
temp.push(2)
print(str(temp))
