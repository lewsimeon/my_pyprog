#求出数列第n位的值
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)
print(fib(10))

#输出数列前n位
#v1-普通函数
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(a,end=' ')
        a, b = b, a + b     #c=a;a=b;b=c+b
        n = n + 1
    exit(0) #return 'done'

#v2-生成器
def fib2(max):
    n,a,b = 0,0,1
    while (n < max):
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

g2 = fib2(10)
for i in g2:
    print(i,end=' ')