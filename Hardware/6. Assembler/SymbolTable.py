def CreateTable(path):
    table = dict()
    fh = open(path, "r")
    for line in fh:
        split = line.split(";")
        table[split[0]] = int(split[1])
    return table


class SymbolTable:
    def __init__(self, path: str):
        self.table = CreateTable(path)

    def addEntry(self, symbol: str, address: int):
        self.table[symbol] = address

    def Contains(self, symbol: str):
        return symbol in self.table

    def GetAddress(self, symbol: str):
        return self.table.get(symbol)
