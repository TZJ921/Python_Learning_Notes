# 实现shell里面的命令'tail -f'，跟踪文件流
import time
def follow(thefile):
    thefile.seek(0,2) # Go to the end of the file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

# 例子
logfile = open("access-log")
for line in follow(logfine):
    print(line)
