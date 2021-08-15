def regOf(a):
    if(a in reg and a.lower() != "flags"):
        return(str(reg[a.lower()]))
    else:
        return 0
    


def print_a(operation, para_a, para_b, para_c, line_no):
    res = opcode[operation] + "00" #add r3 r2 r1
    for i in para_a, para_b, para_c:
        t = regOf(i)
        res += t
    final_output.append(res)


def print_b(operation, para_a, imm, line_no):
    res = opcode[operation]
    t = regOf(para_a, line_no)
    res += t
    res += convertBinary(imm)
    final_output.append(res)


def print_c(operation, para_a, para_b, line_no):
    res = opcode[operation] + "00000"
    for i in para_a, para_b:
        t= regOf(i, line_no)
        res += t
    final_output.append(res)

def print_d(operation,para_a,m,line_no):
    res=opcode[operation]
    t=regOf(para_a,line_no)
    if t:
        res+=t
    else:
        return
    res+=m
    final_output.append(res)

def print_e(operation,m,line_no):
    res=opcode[operation]+"000"
    res+=m
    final_output.append(res)

def print_f(operation,line_no):
    res =opcode[operation]+"00000000000"    
    final_output.append(res)

def convertBinary(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)