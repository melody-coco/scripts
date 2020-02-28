import sys

def encode(ss):
    answer = ''
    for x in range(len(ss)):
        zc = ss[x:(x+1)]
        c = ord(zc)
        c = '%'+hex(c)[2:]
        answer = answer+c

    return answer

def decode(ss):
    list1 = ss.split('%')[1:]
    # print(list1)
    answer = ''
    for x in range(len(list1)):
        x = list1[x]
        x = int(x,16)
        # print(x)
        x = chr(x)
        # print(x)
        answer = answer+x
    
    return answer

if __name__ == "__main__":
    while True:
        try:
            action = int(input("url解码或编码脚本：1：编码。2：解码。3：退出"))
        except expression as identifier:
            pass

        if action == 1:
            number = input("输入你要进行解码的字符串")
            try:
                print("解码结果为：%s"%(encode(number)))
            except expression as identifier:
                print("程序出错清退出")
        
        elif action == 2:
            number = input("输入你要进行解码的字符串")
            try:
                print("解码结果为：%s"%(decode(number)))
            except expression as identifier:
                print("程序出错清退出")
        elif action == 3:
            sys.exit()