def CreateTable(path):
    table = dict()
    fh = open(path, "r")
    # We create a dictionary based on a given file describing the symbols and addresses separated by ";"
    for line in fh:
        split = line.split(";")
        table[split[0]] = int(split[1])
    fh.close()
    return table


class SymbolTable:
    def __init__(self, path: str):
        self.table = CreateTable(path)

    def addEntry(self, symbol: str, address: int):
        self.table[symbol] = address

    def Contains(self, symbol: str) -> bool:
        return symbol in self.table

    def GetAddress(self, symbol: str) -> int:
        return self.table.get(symbol)
