
symbols = ['[', ']', '(', ')', '{', '}']
total = len(symbols) // 2 * [0]



def check_ecpression(expression):
    last_index = 0
    for char in expression:
        for i, symbol in enumerate(symbols):
            if symbol == char:
                if i % 2 == 0:
                    total[i//2] -= 1
                    last_index = i//2
                else:    
                    for tot in total:
                        if tot !=0 and last_index != i//2 :
                            return False
                    total[i//2] += 1
                    

    for tot in total:
        if tot != 0:
            return False
    return True

expression = '"(5+6)∗(7+8)/(4+3)"'

print('Input: exp = "', expression, '"')
print('Output: ', check_ecpression(expression))