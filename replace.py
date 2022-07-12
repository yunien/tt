filename = "/Users/nick/project/replaceTXT/83178333_05-06.txt"
text = open(filename, 'r')
linesNew = []

for x, line in enumerate(text):
    # 產生序號，固定7位數，不足前方補0
    s = "%07d" % (x+1)
    # 準備取代第12~19格的序號
    replaceStr = line[11:18]
    # 先取代 -> 去除換行 -> 去除每行最後的空白 -> 最後補滿固定82(由0開始算)位數的空白 -> 補回換行
    linesNew.append(line.replace(replaceStr, s, 1).strip('\n').strip().ljust(81, ' ')+'\n')
    # DEBUGGING THE CODE
    # print('newss:',linesNew[x])

text.close()

# print('linesNew:',linesNew)

path = '/Users/nick/project/replaceTXT/output.txt'
f = open(path, 'w')
f.writelines(linesNew)
f.close()
