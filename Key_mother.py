import random,string,time,datetime
def crypt(source,key):
    from itertools import cycle
    result=''
    temp=cycle(key)
    for ch in source:
        result=result+chr(ord(ch)^ord(next(temp)))
    return result
src_digits = string.digits
src_uppercase = string.ascii_uppercase
src_lowercase = string.ascii_lowercase
src_symbol = ['!', '@', '#', '$', '%', '^', '&', '*']
name=input("PassWord for:")
key=input("encode_keys:")

while True:
    symbol_num  = random.randint(1,2)
    digits_num = random.randint(1,8-symbol_num-2)
    lowercase_num = random.randint(1,8-symbol_num-digits_num-1)
    uppercase_num = 8 - (symbol_num + digits_num+lowercase_num)
    password = random.sample(src_digits,digits_num) + random.sample(src_uppercase,uppercase_num) + random.sample(src_lowercase,lowercase_num)+random.sample(src_symbol,symbol_num)
    random.shuffle(password)
    new_password = ''.join(password)
    #密码文件备份
    encrypted=crypt(new_password,key)
    print("Tool：" +name)
    print('Key：' + new_password)
    print('Time：'+str(datetime.datetime.now()))
    bo=input("Are you willing to use this key?(y/n)")
    if bo=='y':
        print("password is in your file!")
        with open("D:/Files/key/key_his.txt",'a',encoding= 'UTF-8') as file:
            file.write("Tool：" +name+ '\n')
            file.write('Key：' + encrypted+'\n')
            file.write('Time：'+str(datetime.datetime.now()))
            file.write('\n')
            file.write('\n')
            file.close()
        t=10
        while t>=1:
            print('\r'+"window will close in "+str(t)+" seconds!",end='',flush=True)
            time.sleep(1)
            t -= 1
        break
    else:
        continue
