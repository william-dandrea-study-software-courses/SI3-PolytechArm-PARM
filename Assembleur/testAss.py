import sys

def getValue(arg):
    return arg[1:]

def arg(line, val):
    return line.split(" ")[val]

def numArgs(line):
    return(len(line.split(" "))-1)

def dec_to_bin(x, bits):
    val = str(int(bin(x)[2:]))
    i = 0
    for i in range(bits-len(val)):
        val = "0"+val
    return val

def bin_to_hex(x):
    return hex(int(x, 2))[2:]

def argIsImm(line):
    splitted = line.split(" ")
    if (splitted[1][0] == "#"):
        return True
    else:
        return False


try :
    assFile = open("test.s", "r")
except:
    sys.exit(-1)

try :
    dest = open("assembleur.txt", "w")
except:
    sys.exit(-1)

dest.write("v2.0 raw\n")

for line in assFile :
    binary_line = ""
    hex_line = ""

    instruction = line.split(" ")[0]
    line = line.replace(",", "").replace("[", "").replace("]", "").replace("  ", " ")
    

    #--------------------------La partie Data processing--------------------------
    #AND
    if (instruction == "ands"):
        binary_line = "0100000000"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #EOR
    if (instruction == "eors"):
        binary_line = "0100000001"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)

    #LSL
    if (instruction == "lsls"):
        binary_line = "0100000010"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #LSR
    if (instruction == "lsrs"):
        binary_line = "0100000011"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #ASR
    if (instruction == "asrs"):
        binary_line = "0100000100"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #ADC
    if (instruction == "adcs"):
        binary_line = "0100000101"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #SBC
    if (instruction == "sbcs"):
        binary_line = "0100000110"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #ROR
    if (instruction == "rors"):
        binary_line = "0100000111"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #TST
    if (instruction == "tst"):
        binary_line = "0100001000"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #RSB
    if (instruction == "rsbs"):
        binary_line = "0100001001"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #CMP
    if (instruction == "cmp"):
        binary_line = "0100001010"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #CMN
    if (instruction == "cmn"):
        binary_line = "0100001011"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #ORR
    if (instruction == "orrs"):
        binary_line = "0100001100"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #MUL
    if (instruction == "muls"):
        binary_line = "0100001101"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #BIC
    if (instruction == "bics"):
        binary_line = "0100001110"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)
    
    #MVN
    if (instruction == "mvns"):
        binary_line = "0100001111"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        hex_line = bin_to_hex(binary_line)

    #--------------------------La partie Shift, Add, Sub, Mov--------------------------
    #LSL
    if (instruction == "lsls"):
        binary_line = "00000"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 5)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 3))), 3)
        hex_line = bin_to_hex(binary_line)

    #LSR
    if (instruction == "lsrs"):
        binary_line = "00001"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 5)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 3))), 3)
        hex_line = bin_to_hex(binary_line)

    #ASR
    if (instruction == "asrs"):
        binary_line = "00010"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 5)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 3))), 3)
        hex_line = bin_to_hex(binary_line)

    #ADD
    if (instruction == "adds"):
        if (argIsImm(line)):
            binary_line = "0001110"   #Immediate
        else:
            binary_line = "0001100"   #Register
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 3))), 3)
        hex_line = bin_to_hex(binary_line)

    #SUB
    if (instruction == "subs"):
        if (argIsImm(line)):
            binary_line = "0001111"   #Immediate
        else:
            binary_line = "0001101"   #Register
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 3))), 3)
        hex_line = bin_to_hex(binary_line)

    #MOV
    if (instruction == "movs"):
        binary_line = "00100"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 8)
        hex_line = bin_to_hex(binary_line)

    #--------------------------La partie Load/Store--------------------------
    #STR
    if (instruction == "str"):
        binary_line = "10010"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        if (numArgs(line) == 3):
            binary_line += dec_to_bin(int(getValue(arg(line, 3))), 8)
        else:
            binary_line += "00000000"
        hex_line = bin_to_hex(binary_line)

    #LDR
    if (instruction == "ldr"):
        binary_line = "10011"
        binary_line += dec_to_bin(int(getValue(arg(line, 1))), 3)
        if (numArgs(line) == 3):
            binary_line += dec_to_bin(int(getValue(arg(line, 3))), 8)
        else:
            binary_line += "00000000"
        hex_line = bin_to_hex(binary_line)

    #------------------------------Miscellaneous--------------------------
    #ADD
    if (instruction == "add"):
        binary_line = "101100000"
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 7)
        hex_line = bin_to_hex(binary_line)

    #SUB
    if (instruction == "sub"):
        binary_line = "101100001"
        binary_line += dec_to_bin(int(getValue(arg(line, 2))), 7)
        hex_line = bin_to_hex(binary_line)

    dest.write(hex_line+" ")
    

