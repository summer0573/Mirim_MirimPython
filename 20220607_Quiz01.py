
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
n1 = int(number % 1000 / 100)
n2 = int(number % 100 / 10)
n3 = int(number % 10)
print(n1+n2+n3)

number = 53461
n1 = int(number % 100000 / 10000)
n2 = int(number % 10000 / 1000)
n3 = int(number % 1000 / 100)
n4 = int(number % 100 / 10)
n5 = int(number % 10)
print(n1+n2+n3+n4+n5)

print("="*20)

#4. 369게임
# for i in range(1, 100+1):
#     if i == 3 or i == 6 or i == 9:
#         print(" 짝 ")
#     else:
#         print(f' {i} ')