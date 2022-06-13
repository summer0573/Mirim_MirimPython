
#-, / 없애기
phone_number = "010-7240-4658"
for n in phone_number:
    if n == '-' or n == '/' or n == ' ':
        continue
    print(n, end='')
print()

phone_number = phone_number.replace('-','')
phone_number = phone_number.replace('/','')
phone_number = phone_number.replace(' ','')
print((phone_number))


print("="*20)

#학번 -> 학년 반 번호 출력하기
student_number = '2101'
# if student_number[1] == '1' or student_number[1] == '2':
#     g = '뉴미디어소프트웨어과'
# elif student_number[1] == '3' or student_number[1] == '4':
#     g = '뉴미디어웹솔루션과'
# elif student_number[1] == '5' or student_number[1] == '6':
#     g = '뉴미디어디자인과'
majors = ['뉴미디어소프트웨어과', '뉴미디어소프트웨어과',
          '뉴미디어웹솔루션과', '뉴미디어웹솔루션과',
         '뉴미디어디자인과','뉴미디어디자인과' ]
index= int(student_number[1])
g = majors[index-1]
print(f'{student_number[0]}학년 {student_number[1]}반')
print(f'{g} {int(student_number[2:])}번')

print("="*20)

#3. N-sum
number = 331
n1 = number % 1000 // 100
n2 = number % 100 // 10
n3 = number % 10
print(n1+n2+n3)

number = 523523
sum_value = 0
while True:
    if number == 0:
        break
    sum_value += number % 10
    number = number // 10
print(sum_value)

number_s = str(number) # '523523'
sum_val2 = 0
for n in number_s:
    sum_val2 += int(n)
print(sum_val2)

#나머지 = number % 10            3
#number = number // 10          52352
# 나머지 = number % 10           2
# number = number // 10         5235
# 나머지 = number % 10           5
# number = number // 10        523
# 나머지 = number % 10           3
# number = number // 10         52
# 나머지 = number % 10           2
# number = number // 10         5

print("="*20)


for i in range(1, 100+1):
    number_s = str(i)
    count = 0
    for ch in number_s:
        if ch == '3' or ch == '6' or ch =='9':
            count += 1
    if count == 0:
        print(i)
    else:
        print("짝"*count)