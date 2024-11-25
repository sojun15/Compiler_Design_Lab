import re
file1 = open('input.txt','r')
file2 = open('out.txt','w')
value = 1

symbols = [',',';','(',')','{']
variables = ['n1','n2','num1','max']
constant = ['15','31.17','0']

for single_line in file1.readlines():
    if '//' in single_line:
        continue
    elif '/*' in single_line:
        value = 0
    elif '*/' in single_line:
        value = 1
    else:
        file2.write(single_line)
file2.write('\nThe symbol,variable,number are given below:\n')
file2.close()

file3 = open('out.txt','r+')

for single_line in file3.readlines():
    for symbol in symbols:
        if symbol in single_line:
            if symbol == ';':
                file3.write(symbol+' -> semi colon\n')
            elif symbol == ',':
                file3.write(symbol+' -> comma\n')
            elif symbol == '(':
                file3.write(symbol+' -> parenthesis\n')
            elif symbol == '{':
                file3.write(symbol+' -> curly blace\n')
    
    for varable in variables:
        if varable in single_line:
            file3.write(varable+'-> id\n')

    for const in constant:
        if const in single_line:
            file3.write(const+'-> number\n')

    