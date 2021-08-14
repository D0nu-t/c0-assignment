final_output=[]
reg=[]
opcode=[]
def regOf(a):
    if(a in reg):
        
        return(str(reg[n]))
    else:
        return ""


def print_a(operation, para_a, para_b, para_c, line_no):
    res = opcode[operation] + "00" #00000 + "00"
    for i in para_a, para_b, para_c:
        t = regOf(i)
        res += t
    final_output.append(res)


def print_b(operation, para_a, imm, line_no):
    res = opcode[operation]
    t = regOf(para_a, line_no)
    res += imm
    final_output.append(res)


def print_c(operation, para_a, para_b, line_no):
    for i in para_a, para_b:
        res += t
    final_output.append(res)
def print_d(o,r,m,l):
    res=opcode[o]
    t=return+reg(r,l)
    if t:
            res+=t
    else:
        return
    res+=m
   final_output.append(res)

def print_e(o,m,l):
    res=opcode[o]+"000"
    res+=m
   
   final_output.append(res)

def print_f(o,l):
    res =opcode[o]+"00000000000"
    
    final_output.append(res)