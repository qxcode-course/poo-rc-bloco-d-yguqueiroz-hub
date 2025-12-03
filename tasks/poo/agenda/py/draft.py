class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self):
        validos = "0123456789().-"
        return all(c in validos for c in self.number)

    def __str__(self):
        return f"{self.id}:{self.number}"


class Contact:
    def __init__(self, name: str):
        self.name = name
        self.favorited = False
        self.fones: list[Fone] = []

    def addFone(self, id: str, number: str):
        f = Fone(id, number)
        if f.isValid():
            self.fones.append(f)
        else:
            print(f"fail: invalid number {number}")

    def rmFone(self, index: int):
        if 0 <= index < len(self.fones):
            self.fones.pop(index)
        else:
            print("fail: invalid index")

    def toggleFavorited(self):
        self.favorited = not self.favorited

    def isFavorited(self):
        return self.favorited

    def getFones(self):
        return self.fones

    def getName(self):
        return self.name

    def setName(self, name: str):
        self.name = name

    def __str__(self):
        prefix = "@" if self.favorited else "-"
        fones_str = ", ".join(str(f) for f in self.fones)  # COM espaço depois da vírgula
        return f"{prefix} {self.name} [{fones_str}]"        # espaço após prefixo


class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []

    def findPosByName(self, name: str):
        for i, c in enumerate(self.contacts):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)

        if pos != -1:
            contact = self.contacts[pos]
        else:
            contact = Contact(name)
            self.contacts.append(contact)

        for f in fones:
            if f.isValid():
                contact.fones.append(f)
            else:
                print(f"fail: invalid number {f.number}")

        self.contacts.sort(key=lambda c: c.getName())

    def getContact(self, name: str):
        pos = self.findPosByName(name)
        if pos != -1:
            return self.contacts[pos]
        return None

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos != -1:
            self.contacts.pop(pos)

    def search(self, pattern: str):
        result = []
        for c in self.contacts:
            if pattern in str(c):
                result.append(c)
        return result

    def getFavorited(self):
        return [c for c in self.contacts if c.isFavorited()]

    def __str__(self):
        return "\n".join(str(c) for c in self.contacts)


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
                index = int(parts[2])
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

    
