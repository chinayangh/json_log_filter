import random,string
src = string.printable
count = 3
list_passwds = []
for i in range(int(count)):
    list_passwd_all = random.sample(src, 10) #从字母和数字中随机取10位
    random.shuffle(list_passwd_all) #打乱列表顺序
    str_passwd = ''.join(list_passwd_all) #将列表转化为字符串
    if str_passwd not in list_passwds: #判断是否生成重复密码
        list_passwds.append(str_passwd)
print(list_passwds)
