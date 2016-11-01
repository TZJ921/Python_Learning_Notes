def coroutine(func):
    def start(*args, *kwargs):
        cr = func(*args, *kwargs)
        next(cr)
        return cr
    return start

@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)

f = open("access-log")
follow(f,
       broadcast([
           grep('python', printer()),
           grep('ply', printer()),
           grep('swig', printer())])
    )

# 上面的例子是将item发到了不同的printer()
# 下面这个例子先将printer()实例化，然后将所有的打印发送给同一个printer
f = open("access-log")
p = printer()
follow(f,
       broadcast([grep('python', p),grep('ply', p), grep('swig', p)]))

