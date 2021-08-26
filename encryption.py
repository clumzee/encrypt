import math

def encryption(s):
    # Write your code here
    s = s.replace(" ","_")
    #print(s)
    
    size = len(s)
    
    size_sqrt = math.sqrt(size)
    
    size_flr = math.floor(size_sqrt)
    size_ceil = math.ceil(size_sqrt)
    
    
    #print(size_sqrt)
    
    encrpt_mtrx = []
    
    for i in range(0,len(s),size_ceil):
        encrpt_mtrx.append(s[i:size_ceil +i])
        
    #print(encrpt_mtrx)
    
    encrpt_mssg = ""
    for i in range(size_ceil):
        for j in range(len(encrpt_mtrx)):
            try:
                encrpt_mssg += encrpt_mtrx[j][i]
            except IndexError:
                pass
            
        encrpt_mssg += " "
        
    return encrpt_mssg