class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        validos = "0123456789().-"
        for char in self.number:
            if char not in validos:
                return False
            
            
        return True
        
    def __str__(self) -> str:
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name):
        self.name = name
         self.fones = []
        self.favorited = False

    def addFone(self, id, number):
        f = Fone(id, number)
        if f.isValid():
            self.fones.append(f)
        else:
            print("Fone Ruim")

    def rmFone(self, index): 
        if index >= 0 and index < len(self.fones):
            self.fones.pop(index)
        else:
            print("Indice não existe")

    def toggleFavorited(self):
        self.favorited = not self.favorited

    def isFavorited(self):
        return self.favorited
    
    def __str__(self):
        saida_fones = []
        for f in self.fones:
            saida_fones.append(str(f))
        prefixo = "@" if self.favorited else "-"

        return f"{prefixo} {self.name} [{', '.join(saida_fones)}]"
class Agenda:
    def __init__(self):
        self.contacts = []

    def findPosByName(self, name):
        for i in range(len(self.contacts)):
            if self.contacts[i].name == name:
                return i
        return -1
    def addContact(self, name, fones):
        pos = self.findPosByName(name)

        if pos != -1:
            contato = self.contacts[pos]
        else:
            contato = Contact(name)
            self.contacts.append(contato)
            self.contacts.sort(key=lambda c: c.name)

        for f in fones:
            contato.addFone(f.id, f.number)

    def search(self, pa
            ttern):
        res = []
        for c in self.contacts:
            if pattern in str(c):
                res.append(c)
        return res
    
    def getContacts(self):
        return self.contacts
    
    def __str__(self):
        saida = ""
        for c in self.contacts:
            saida += str(c) + "\n"
        return saida
    
print("teste")
try:
    a = Agenda()
    fones_teste = [Fone("oi", "123")]

    a.addContact("bia", fones_teste)
    a.addContact("ana", fones_teste)

    print(a)
except Exception as e:
    print("deu erro na agenda: ", e)

agenda = Agenda()

while True:
    line = input("$")