filename = "/Users/nick/project/replaceTXT/83178333_05-06.txt"
text = open(filename, 'r')
linesNew = []

for x, line in enumerate(text):
    s = "%07d" % (x+1)
    replaceStr = line[11:18]
    linesNew.append(line.replace(replaceStr, s, 1))
    # DEBUGGING THE CODE
    # print('newss:',linesNew[x])

text.close()

print('linesNew:',linesNew)

path = '/Users/nick/project/replaceTXT/output.txt'
f = open(path, 'w')
f.writelines(linesNew)
f.close()

