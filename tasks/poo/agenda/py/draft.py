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
        if index >= 0 or index < len(self.fones):
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
print("\nteste")
try:
    c = Contact("ana")
    c.addFone("oi", "123")
    c.addFone("tim", "99a")
    print(c)
except Exception as e:
         print("deu erro")