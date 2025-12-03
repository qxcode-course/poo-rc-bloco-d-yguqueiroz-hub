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
        f =    Fone(id, number)
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

    def rmContact(self, name):
        pos = self.findPosByName(name)
        if pos != -1:
            self.contacts.pop(pos)

    def getFavorited(self):
        favs = []
        for c in self.contacts:
            if c.isFavorited():
                favs.append(c)
        return favs


    def search(self, pattern):
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
        return saida.strip()

def main():
    agenda = Agenda()
    while True:
        try:
            line = input()
            if not line:
                break
            if not line.strip():
                continue

            print(f"${line}" if not line.startswith("$") else line)
                
            if line.startswith("$"):
                line = line[1:]

            parts = line.split()
            if not parts:
                continue

            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "add":
                name = parts[1]
                fones_args = parts[2:]
                lista_fones = []
                for token in fones_args:
                    dados = token.split(":")
                    if len(dados) == 2:
                        lista_fones.append(Fone(dados[0], dados[1]))

                agenda.addContact(name, lista_fones)

            elif cmd == "rmFone":
                name = parts[1]
                index =  int(parts[2])
                pos = agenda.findPosByName(name)
                if pos != -1:
                    agenda.contacts[pos].rmFone(index)

            elif cmd == "show":
                print(agenda)
            
            elif cmd == "rm":
                name = parts[1]
                agenda.rmContact(name)

            elif cmd == "search":
                pattern = parts[1]
                res = agenda.search(pattern)
                for c in res:
                    print(c)

            elif cmd == "tfav":
                name = parts[1]
                pos = agenda.findPosByName(name)
                if pos != -1:
                    agenda.contacts[pos].toggleFavorited()

            elif cmd == "favs":
                res = agenda.getFavorited()
                for c in res:
                    print(c)

        except EOFError:
                break
        except Exception as e:
            print("Deu erro no loop:", e)

if __name__ == "__main__":
    main()

    