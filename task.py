import re

file1 = open('input.txt','r')
file2 = open('output.txt','w')

value = 1
keyword = ['if','else','int']
symbol = [',',';','(',')']
variable = ['n1','n2','max']
const = ['0','15','31.17']

for single_line in file1.readlines():
    if '//' in single_line:
        continue
    elif '/*' in single_line:
        value = 0
    elif '*/' in single_line:
        value = 1
    else:
        file2.write(single_line)

file2.write('\n')
file2.close()

file4 = open('output.txt','r+')
file5 = open('symbol2.txt','r')

for single_line in file4.readlines():
    for key in keyword:
        if key in single_line:
            file4.write(key+'-> keyword'+'\n')

    for sym in file5.readlines():
        if sym[0] in single_line:
            file4.write(sym)
            file4.write('\n')
    file5.close()
    file5 = open('symbol2.txt','r')
    for single_word in re.findall(r'\d+\.\d+|\w+|[,;()=]',single_line):
        if single_word in variable:
            file4.write(single_word+' -> variable\n')
        elif single_word in const:
            file4.write(single_word+' -> constant\n')