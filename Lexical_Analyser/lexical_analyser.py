import re

keywords=["int","void","char","main()","print","return","float","double"]

operators = { '=': 'Assignment Operator','+': 'Additon Operator', '-' : 'Substraction Operator', '/' : 'Division Operator', '*': 'Multiplication Operator'}
optr_keys = operators.keys()

blocks = {'{' : 'Blocked Statement Body Open', '}':'Blocked Statement Body Closed'}
block_keys = blocks.keys()

f = open("input.txt", "r")
i = f.read()

#Calculating number of lines in program
num_lines = 0
with open('input.txt', 'r') as f:
    for line in f:
        num_lines += 1

#Caluculating number of comment lines
comments = re.findall("(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)",i)
no_of_comments = len(comments)

#Removing comment lines
x = re.sub('//.*?\n|/\*.*?\*/', '', i, flags=re.S)

program =  x.split('\n')
L=[]
for line in program:
    tokens = line.split(' ')
    for i in tokens:
        if i not in L:
            if i in block_keys:
                print(i,blocks[i])
                L.append(i)
            if i in keywords:
                print(i,"Keyword")
                L.append(i)
            if i in optr_keys:
                print(i,operators[i])
                L.append(i)
            x = re.findall('[_a-zA-Z][_a-zA-Z0-9]*',i)
            if i in x and i not in L:
                print(i,"identifier")
                L.append(i)
            y = re.findall('[-+]?[0-9]+[.]?[0-9]*',i)
            if i in y and i not in L:
                print(i,"number")
                L.append(i)

print("There are total",num_lines,"lines in program")
print("There are total",no_of_comments,"comments in program")