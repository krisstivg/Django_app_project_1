# n=int(input())
# count=0
# a=[0]*(n+1)
# s_1=input()
# s_1=s_1.replace(" ",'')
# for i in reversed(s_1):
#     a[count]=(int(i))
#     count+=1
# m=int(input())
# count=0
# b=[0]*(m+1)
# s_2=input()
# s_2=s_2.replace(" ",'')
# for i in reversed(s_2):
#     b[count]=(int(i))
#     count+=1
# if __name__=='__main__':
#     if n>=m:
#         print(n)
#         for i in range(len(b)):
#             a[i]+=b[i]
#
#         for i in reversed(range(n+1)):
#             print(a[i], end=" ")
#     else:
#         print(m)
#         for i in range(len(a)):
#             b[i]+=a[i]
#         for i in reversed(range(m+1)):
#             print(b[i], end=" ")


import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await fun1(x)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))