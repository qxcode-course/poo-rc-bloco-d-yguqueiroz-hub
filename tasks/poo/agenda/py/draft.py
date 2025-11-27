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
    
print("teste")
f1 = Fone("casa", "1234")
f2 = Fone("errado", "12a4")

print(f1.isValid())
print(f2.isValid())
print(f1)