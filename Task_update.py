file1 = open("file1.txt","r")
file2 = open("code.txt","w")
file3 = open("variable.txt","w")
file4 = open("symbol.txt","w")
file5 = open("keyword.txt","w")

value = 1
words = ["for","if","else if","else","while","do","int","float",'double','char','string']
symbols = [',',';','<','>']
data_type = ['int','double','float','char','string']
allthing = ["for","if","else if","else","while","do","int","float",',',';','<','>','double','float','main()','char','string']

for single_line in file1.readlines():
    if "//" in single_line:
        continue
    elif "/*" in single_line:
        value = 0
    elif "*/" in single_line:
        value = 1
    elif value:
        file2.write(single_line)

file1 = open("file1.txt","r")

file5.write("determine keywords in the file1:\n")
file4.write("Symbols are given below:\n")
file3.write("Variables are given below:\n")
for single_line in file1.readlines():
    for word in words:
        if word in single_line:
            file5.write(word)
            file5.write('\n')

    for symbol in symbols:
        if symbol in single_line:
            if symbol=='<':
                file4.write('< less than') 
                file4.write('\n')       
            if symbol=='>':
                file4.write('> greater than')
                file4.write('\n')
            if symbol==',':
                file4.write(', comma')
                file4.write('\n')        
            if symbol==';':
                file4.write('; semi-colon')
                file4.write('\n')

    for data in data_type:
        if data in single_line:
            for x in single_line.split():
                if x not in allthing:
                    file3.write(x)
                    file3.write('\n')