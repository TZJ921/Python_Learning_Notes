# grep命令的简单实现
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

logfile = open("access-log")
loglines = follow(logfile)
pylines = grep("python", loglines)

for line in pylines:
    print(line)
