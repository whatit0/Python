# 반복문 while
a = 1

while a <= 5:
    print(a, end=' ')
    a += 1
    
    
print()
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print('i=' + str(i) + "/j=" + str(j))
        j = j + 1
    i += 1
    

print('1 ~ 100 사이의 정수 중 3의 배수의 합')
i = 1; hap = 0;
while i <= 100:
    if i % 3 == 0:
        hap += i
    i += 1
print('합은 ' + str(hap))


print()
colors = 'r', 'g', 'b'
print(colors[1])
a = 0
while a < len(colors):
    print(colors[a], end=' : ')
    a += 1

print('\n별 찍기')
i = 1
while i <= 10:
    j = 1
    disp = ''
    while j <= i:
        disp += '*'
        j += 1
    print(disp)
    i += 1


print('\n문1 : 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고 그 합을 출력')


print()
print('\n문2 : 2 ~ 5 단의 구구단. 단이 다르면 다음 행으로 출력')
i = 1
while i < 5:
    j = 1
    while j <= 9:
        j += 1
        hap = i * j
        print(str(i) + '*' + str(j) + '=' + str(hap), end=' ')   
    print() 
    i+=1
     


import time
# time.sleep(3)
# print('계속')

button = input('폭탄 스위치를 누를까요(y/n)')
if button == 'Y' or button == 'y':
    #pass
    count = 5
    while 1 <= count:
        print('%d초 남았군요'%count)
        time.sleep(1)
        count -= 1
    print('폭발')
elif button == 'N' or button == 'n':
    print('작업 취소')
else:
    print('y or n을 누르세요')





