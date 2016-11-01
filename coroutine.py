def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)

g = grep("python")
g.send("python")
g.close() # 关闭协程，同时gc

@coroutine
def grep_close(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye.")

g = grep("python")
g.send("python")
g.close()
g.throw(RuntimeError, "You're hosed") # 如何在生成器中抛出一个自定义的异常。
