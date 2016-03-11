f = open('8.txt')

line = f.readline()
line.rstrip("/n")
number_list = list(line)    #line into list
number_list.pop()   #cut a last char(/n)

while line:
    line = f.readline()
    line.rstrip("/n")
    number_list.extend(list(line))  #extend line into list
    number_list.pop()   #cut a last char(/n)

f.close()


i = 0
k = 0
num = 1
nmax = 1


while i+13 <= len(number_list): #while length of number_list > i+13
    k = 0
    num = 1
    while k < 13:
        num *= int(number_list[i+k])
        k+=1
    if nmax < num:
        nmax = num
    i+=1
print nmax
