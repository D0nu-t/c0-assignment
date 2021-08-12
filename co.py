A=["add","sub",'mul','xor','or','and']
B=['mov','rs','ls']#all type b commands have $ in them
C=['movr','div','not','cmp']
D=['ld','st']
E=['jmp','jlt','jgt']
F=['hlt']
oc={'add':'00000','sub':'00001','mov':'00010','movr':'00011','ld':'00100','st':'00101','mul':'00110','div':'00111','rs':'01000','ls':'01001','xor':'01010','or':'01011','and':'01100','not':'01101','cmp':'01110','jmp':'01111','jlt':'10000','jgt':'10001','hlt':"10011"}
addrs={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}
type=''
data=[]
file = open('test.txt', 'r')
for i in file:
    k=i.split()
    if len(k)==0:
        continue                        #ignores empty lines
    data.append(k)

#print(data)
for i in (data):
    for j in i:
        #print(i[0])
        if '$' in i:
            type='b'
        if(i[0]  not in oc.keys()):
            print("error: invalid instruction")
            break
            
    if "hlt" not in data[-1] or "hlt" not in data:
        print('error: hlt not found')
        break
    else:
        pass

else:
    print(type)
    type=''
#print(data[0])
print(type)
k=data[-1]

print(oc.keys())
print("mul" in oc.keys())
out=''
if "hlt" not in data[-1]:
    print('error: hlt not found')
""" for i in  range(0,len(k)+1):
    if i ==0:

        if i not in A or i not in B or i not in C or i not in D or i not in E or i not in F:
            print('error: invalid instruction ')
    else:
        pass """

for i in range(len(k)):
    print(k[i])
    if i == 0:                          #type A stuf
        out=out+oc.get(k[i])
        out=out+'00'
    elif(k[i][0]=="R"):
        out=out+addrs.get(k[i])
    else:
        pass

else:
    print(out)
    #print(len(out))

