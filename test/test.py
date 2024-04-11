def check_code_meli(code):
    code1 = str(code)
    L = len(code1)
    
    if L < 8 or int(code) == 0:
        return False
    
    code1 = ('0000' + code1)[-10:]
    
    if int(code1[3:9]) == 0:
        return False
    
    c = int(code1[9])
    s = 0
    for i in range(9):
        s += int(code1[i]) * (10 - i)
    
    s = s % 11
    
    return (s < 2 and c == s) or (s >= 2 and c == (11 - s))

print(check_code_meli(5929451850))