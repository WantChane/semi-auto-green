import time
time_str = time.strftime("%Y年%m月%d日%H时%M分%S秒")
with open('count.txt','r+') as f1:
    count = f1.read()
    new_count = int(count) + 1
    f1.seek(0)
    f1.truncate(0)
    f1.write(str(new_count))
with open('test.txt','a+',encoding='utf-8') as f:
    str = "当前时间:{},已执行{}次".format(time_str,new_count)
    f.write(str)
    f.write('\n')