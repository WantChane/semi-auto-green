with open('count.txt','r+') as f1:
    f1.truncate(0)
    f1.write('0')
with open('test.txt','r+') as f1:
    f1.truncate(0)