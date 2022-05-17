
#교통수단 문제
# money = int(input('돈을 입력하시오 : '))
# if money >= 10000:
#     print('택시를 타라')
# elif money >= 720:
#     print('버스를 타라')
# else:
#     print('걸어가라')

# num = int(input('숫자를 입력하시오 : '))
# if num % 4 == 0:
#     print('4의 배수')
# elif num % 3 == 0:
#     print('3의 배수')
# elif num % 2 == 0:
#     print('2의 배수')

# age = int(input('나이 입력 : '))
# if age >= 10 and age < 20: #10 <= age < 20 #age // 10 * 10
#     print('10대')
# elif age >= 30 and age < 40: #30 <= age < 40
#     print('30대')
# else:
#     print('10대, 30대가 아님')
#
# print('---------------------')
# print(str(age//10*10)+'대')

#논리연산자 문제
# x = int(input('정수 입력 : '))
# if x > 10 and x % 2 == 0:
#     print('10 초과 짝수')
# else:
#     print('10 초과 짝수 아님')

# score = int(input('점수 입력 :'))
# if 90 <= score <= 100:
#     print('A')
# elif 80 <= score < 90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60 <= score < 70:
#     print('D')
# elif 0 <= score < 60:
#     print('F')

# MBTI = input("MBTI 입력 : ")
# if MBTI == 'INFP' or MBTI == 'infp': #mbti.upper() == INFP
#     print("블록체인형")
# elif MBTI == 'ESTP' or MBTI == 'estp':
#     print("IoT 개발형")
# else:
#     print("아직 개발중입니다.")

# x = int(input('정수 입력 : '))
# if x > 10:
#     if x % 2 == 0:
#         print('10초과 짝수')
#     else:
#         print('10초과 홀수')
# else :
#     print('10미만')

name = '정현진'
id = 'hyunjinID'
password = 'hyunjinPassword'
id2=input('ID 입력 : ')
password2=input('Password 입력 : ')
if id == id2:
    if password == password2:
        print(f'환영합니다. {name}님')
    else:
        print('패스워드가 틀렸습니다.')
else:
    print('알 수 없는 사용자입니다.')