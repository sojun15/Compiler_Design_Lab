import re
file = open('practice.txt', 'r')
file1 = open("whole.txt","r")
file2 = open("another.txt","w")
special = [',',';','(',')','{','}']
variable = ['num1','num2','sum']
file2.write("Symbol Table:\n")
for line in file.readlines():

    for word_or_separator in re.findall(r'\w+|[, ;(){}]', line):

        if word_or_separator==' ':
            continue
        elif word_or_separator in special:
            for x in file1.readlines():
                if x[0] in special:
                    file2.write(x)
                    file2.write('\n')
        elif word_or_separator in variable:
            file2.write(word_or_separator+' -> id')
            file2.write('\n')
        elif word_or_separator.isdigit():
            file2.write(word_or_separator+' -> number -> constant')
            file2.write('\n')
        else:
            file2.write(word_or_separator+' -> '+word_or_separator)
            file2.write('\n')
