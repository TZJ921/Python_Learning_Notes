# yield作为一个表达式
def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

'''
>>> g = grep("python")
>>> next(g) # 激活生成器
Looking for python
>>> g.send("Yeah, but no, but yeah, but no")
>>> g.send("A series of tubes")
>>>g.send("python generators rock!")
python generators rock!

'''
