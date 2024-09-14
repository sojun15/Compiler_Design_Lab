file1 = open("file1.txt","r")
file2 = open("file2.txt","w")

value = 1
words = ["for","if","else if","else","while","do","int","float"]
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

file2.write("\ndetermine keywords in the file1:")
for single_line in file1.readlines():
    for word in words:
        if word in single_line:
            file2.write('\n')
            file2.write(word)
            
            
            


