import SymbolTable as St
import Parser as Pa
import Code as Co
import os

# Grabs the file on the path and opens it
path = "Add.asm"
Parser = Pa.Parser(path)

# Creates the symbol table
table = St.SymbolTable("table.txt")

# We look through the file for labels

counter = 0
while Parser.HasMoreLines():
    Parser.Advance()
    if Parser.InstructionType() == "L":
        newEntry = Parser.symbol()
        if not table.Contains(newEntry):
            table.addEntry(newEntry, counter)

    counter += 1

# Reset then compile the file
Parser.reset()
output = list()
Code = Co.Code()

counter = 16
while Parser.HasMoreLines():
    Parser.Advance()
    if Parser.InstructionType() == "A":
        symbol = Parser.symbol()

        # symbol is the number of the memory address
        if symbol.isdecimal():
            output.append(int(symbol))
        elif table.Contains(symbol):
            # the symbol is in the table
            output.append(table.GetAddress(symbol))
        else:
            # The symbol is not in table
            output.append(counter)
            table.addEntry(symbol, counter)
            counter += 1
    elif Parser.InstructionType() == "C":
        code_out = "111"

        # parse dest
        now = Parser.dest()
        if now is not None:
            code_out += Code.dest(now)
        else:
            code_out += "000"

        # parse comp, comp is mandatory
        now = Parser.comp()
        code_out += Code.comp(now)

        # parse jump
        now = Parser.jump()
        if now is not None:
            code_out += Code.jump(now)
        else:
            code_out += "000"
    else:
        pass

# Write the output
current_name = os.path.basename(path)
filename = current_name.replace(".asm", ".hack")
fw = open(filename, "w")

for out in output:
    fw.write(format(out, "016b"))
    fw.write("\n")

fw.close()
