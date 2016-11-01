def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)

(i for i in (1,2,3)) #也是生成器的一种产生方式

# 生成器需要用next()来启动
x = countdown(10)
next(x)
