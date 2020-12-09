import time
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result

while True:
    source=input("Decrypted：")
    key=input('key:')
    encrypted=crypt(source,key)
    print('After Decrypted:'+encrypted)
    status=input('continue?(y/n)')
    if status=='y' or status=='Y' or status=='YES' or status=='yes':
        continue
    else:
        break
t=15
while t>=1:
    print('\r'+"window will close in "+str(t)+" seconds!",end='',flush=True)
    time.sleep(1)
    t -= 1