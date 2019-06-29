""" 1.把字符串123456789打印成：321654987
str_temp="123456789"
list=[int(i)-1 for i in str_temp if int(i)%3==0]
print(list)
str_result=""
for index in list:
    start=int(index)
    end=start-3
    if end <=0:
        str_result+=str_temp[start::-1]
    else:
        str_result+=str_temp[start:end:-1]
print(str_result)
"""

"""
2.生成字母和数字混合的验证码
import string
import random
caninput=3 #验证码运行错误的次数
pwd="123"  #锁屏的解锁密码
errorinput=0; #已经错误的次数

#获取随机数,这里让随机数的长度可以自定义
def getRandom():
    inputlength = int(input("请输入随机数长度：\n "))
    numcnt = random.randrange(1, 4)
    lettercnt = inputlength - numcnt
    result = []

    while (numcnt>0 and numcnt<inputlength):
       temp_num=lambda :random.choice(string.digits)
       result.append(temp_num())
       numcnt+=1
       pass

    while lettercnt>0 and lettercnt<inputlength:
        temp_letter=lambda :random.choice(string.ascii_letters)
        result.append(temp_letter())
        lettercnt+=1
        pass

    random.shuffle(result) #随机打乱列表的元素
    resultstr=""
    for i in result:resultstr+=i
    return resultstr

#程序运行的主方法
def check():
    rdm = getRandom()
    LockFlag=True
    global errorinput
    global caninput
    while errorinput<caninput:
        input_str = input("请输入验证码：%s \n" % rdm)
        if  input_str==rdm:
            errorinput=0
            goon=input("输入验证码正确,是否重新生成并验证，输入y继续,其他字符退出：\n")
            if goon=="y":
                check()
            else:
                print("你选择了退出程序！")
                LockFlag=False
                break;
        else:
            errorinput+=1
            continue
            pass

    while LockFlag:
        _goon=input("错误次数过多，请输入密码进行验证,密码是：123,输入错误密码退出程序\n")
        global pwd
        if _goon==pwd:
            errorinput=0
            check()
        else:
            print("你选择了退出程序！")
            break;


if __name__=="__main__":
    check()
"""

