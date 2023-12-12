class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, type, location):
        self.symbols[name] = {'type': type, 'location': location}

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        else:
            return None

    def display(self):
        print("Symbol Table:")
        for name, info in self.symbols.items():
            print(f"Attribute: {name}, Type: {info['type']}, Location: {info['location']}")


# Sample usage
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
inp = '\n'.join(lines)

if __name__ == "__main__":
    sym_table = SymbolTable()
    loc = 100
    for line in lines:
        a = []
        words = line.split()
        for word in words:
            if word=='int' or word=='float' or word=='double' or word=='void':
                attr = ""
                for i in range(len(word)+1,len(line)):
                    if(line[i]==' ' or line[i]=='=' or line[i]==';'):
                       sym_table.insert(attr, word, loc)
                       attr = ""
                       loc += 1
                       break
                    else:
                       attr += line[i]
        # sym_table.insert('x', 'int', 100)
    sym_table.display()
    # print("Lookup result for 'x':", sym_table.lookup('x'))
    # print("Lookup result for 'z':", sym_table.lookup('z'))
    while True:
        s = input("Enter attribute name to search: ")
        if s==" ":
            break
        print("Search result for ",s," ",sym_table.lookup(s))
    

#input sample
# int t1=10;
# float f1 = 10.6
# double d1 = 1.124
