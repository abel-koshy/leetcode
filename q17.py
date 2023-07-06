digits="23"
baseguide = {"2": 97, "3": 100, "4": 103, "5": 106, "6": 109, "7": 112, "8": 116, "9": 119}
op = []
nop=[]
digits = str(digits)
if (digits != ''):
    for i in digits:
        if (i == "7" or i == "9"):
            if (op == []):
                for a in range(4):
                    nop.append(chr(baseguide[i]+a))

            else:
                for k in op:
                    for a in range(4):
                        nop.append(k+chr(baseguide[i]+a))

        else:
            
            if (op == []):
                for a in range(3):
                    
                    nop.append(chr(baseguide[i]+a))
                    
            else:
                for g in op:
                    for a in range(3):
                        nop.append(g+chr(baseguide[i]+a))
        op=nop
        nop=[]
print(op)
