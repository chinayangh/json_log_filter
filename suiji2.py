import re, random, string

count1 = int(3)
i = 0
passwds = []
while i < count1:
    tmp = random.sample(string.printable, 10)
    passwd = ''.join(tmp)
    if re.search('[0-9]', passwd) and re.search('[A-Z]', passwd) and re.search('[a-z]', passwd):
        passwds.append(passwd)
        i += 1
print(passwds)