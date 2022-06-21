#예약어X
#snake_case
#내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#sum = 0 TypeError: 'int' object is not callable
#def sum(x) : 내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#print(x)

# a = sum([10, 20, 3])
# print(a)
#
# print('='*20)
'''
java 함수
접근제어자 반환형 함수명(파리미터1, 파라미터2...){
    return 값;
}

c 함수
반환형 함수명(파리미터1, 파라미터2...){
    return 값;
}

python 함수
def 함수명(파라미터1, 파라미터2...){
    return 값
}
'''
# def my_print(age):
#     print('정현진은 '+ str(age)+'살입니다.') #정현진은 18살입니다.
#     print('정현진은',age,'살입니다.') #정현진은 18살입니다.
#     print(f'정현진은 {age}살입니다.') #정현진은 18살입니다.
# my_print(18) #my_print()실행, my_print()의 리턴값 출력
#
# print('='*20)
#
# def my_print2(name, age):
#     print(name + '은 '+ str(age)+'살입니다.')
#     print(name,'은',age,'살입니다.')
#     print(f'{name}은 {age}살입니다.')
# my_print2('정현진', 20)
# my_print2(age=80, name='정가을') #아규먼트 순서와 관계없이 값을 넣을 수 있음
#
# print('='*20)
#
# def my_print3(name, age, group):
#     print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
#     print(name,'은',age,'살입니다.',group,'소속입니다.')
#     print(f'{name}은 {age}살입니다. {group} 소속입니다.')
# my_print3(age = 30, name = '정현진', group = '미림여정')
# #my_print3(30, name = '정현진', '미림여정') 키워드 인자 뒤에는 계속 키워드 인자로 해야함
# my_print3('정현진', group = '미림여정', age = 30) #위치 인자는 무조건 키워드 인자 앞에 있어야 함
#
# print('='*20)
#
# def my_print4(name, age, group='스트레이키즈'):
#     print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
#     print(name,'은',age,'살입니다.',group,'소속입니다.')
#     print(f'{name}은 {age}살입니다. {group} 소속입니다.')
# my_print4(age=22, name='이용복')
# my_print4(age = 22, name = '이용복', group='댄스라차')
#
# print('='*20)
#
# def my_print5(name, *args): #args 자료형은 tuple
#     print(f'{name} 정보: ')
#     print('정보 : ')
#     for arg in args:
#         print(arg)
# my_print5('이용복', 22, '스트레이키즈', '매니악')
# my_print5('황현진', 22, '스트레이키즈', '매니악')

# print('='*20)

# def my_print4(name, age=20, group): #기본값 있는 파라미터 뒤에는 무조건 기본값있는 파라미터
#     print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
#     print(name,'은',age,'살입니다.',group,'소속입니다.')
#     print(f'{name}은 {age}살입니다. {group} 소속입니다.')

# print('='*20)

def say(name, msg = '안녕하세요', feeling='❤‍🔥'):
    print(f'{name}, {msg}, {feeling}')
say('가현')
say('가현', '🤬')
say('가현', feeling='🤬')

print('='*20)

def fn(a, b=[]):
    b.append(a)
    print(b)
fn(3)
fn(5)
fn(10, [1])
fn(7)
print('='*20)
say('현진', '미안해')

def plus20(age):
    print(age+20)
a = plus20(18)
print(a) #None: plus20() return 값이 없어서 None 리턴
print('='*20)
def plus20(age):
    return age+20
a = plus20(18)
print(a)


print('='*20)


#전화번호 앞자리, 맨 뒤 자리 네자리 출력
def tel(number):
    index = number.find('-')
    f=number[:index]
    b=number[-4:]
    return f, b
# front = '010'
# end = '4658'
front, back = tel('010-7240-4658')
print(f'앞 : {front} \t 뒤 : {back}')

print('='*20)

#min_max([3, 31, 1, 6, 5, -6])

def min_max(리스트):
    mmax = 0
    for i in 리스트:
        if i > mmax:    #리스트[1:]: 0번째는 비교하지 않아도 됨
            mmax = i
        else:
            mmin = i
    return mmin, mmax
min_value, max_value = min_max([3, 31, 1, 6, 5, -6])
print(f'최소 : {min_value}\t최대 : {max_value}')