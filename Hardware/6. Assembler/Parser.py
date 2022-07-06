class Parser:
    def __init__(self, path):
        fh = open(path, "r")
        self.current = ""
        self.address = 0
        self.lines = list()

        for line in fh:
            line = line.partition("//")[0]
            line = line.strip()
            line = line.replace(" ", "")
            self.lines.append(line)

    def HasMoreLines(self):
        return len(self.lines) > self.address + 1

    def Advance(self):
        self.current = self.lines[self.address]
        self.address += 1

    def InstructionType(self):
        if self.current[0] == "@":
            return "A"
        elif self.current[0] == "(":
            return "L"
        else:
            return "C"
        