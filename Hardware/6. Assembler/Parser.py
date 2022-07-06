class Parser:
    def __init__(self, path):
        fh = open(path, "r")
        self.current = ""
        self.address = 0
        self.lines = list()

        # Strip the file from all comments and white spaces
        for line in fh:
            line = line.partition("//")[0]
            line = line.strip()
            line = line.replace(" ", "")
            if line:
                self.lines.append(line)

        fh.close()

    def reset(self):
        self.address = 0

    def HasMoreLines(self) -> bool:
        return len(self.lines) > self.address + 1

    def Advance(self):
        self.current = self.lines[self.address]
        self.address += 1

    def InstructionType(self) -> str:
        if self.current[0] == "@":
            return "A"
        elif self.current[0] == "(":
            return "L"
        else:
            return "C"

    # return only the symbol at the given line
    def symbol(self) -> str:
        ins_type = self.InstructionType()
        if ins_type == "L":
            return self.current[1:-1]
        elif ins_type == "A":
            return self.current[1:]

    # the methods below get the different parts of a C-instruction and make it understandable to the Code

    def dest(self) -> str:
        if self.InstructionType() == "C" and self.current.count("=") > 0:
            return self.current.split("=")[0]

    def comp(self) -> str:
        if self.InstructionType() == "C" and self.current.count("=") > 0:
            return self.current.split("=")[1]
        elif self.InstructionType() == "C" and self.current.count(";") > 0:
            return self.current.split(";")[1]
        else:
            return self.current

    def jump(self) -> str:
        if self.InstructionType() == "C" and self.current.count(";") > 0:
            return self.current.split(";")[1]
