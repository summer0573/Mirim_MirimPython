#예약어X
#snake_case
#내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#sum = 0 TypeError: 'int' object is not callable
#def sum(x) : 내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#print(x)

a = sum([10, 20, 3])
print(a)

print('='*20)
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
def my_print(age):
    print('정현진은 '+ str(age)+'살입니다.') #정현진은 18살입니다.
    print('정현진은',age,'살입니다.') #정현진은 18살입니다.
    print(f'정현진은 {age}살입니다.') #정현진은 18살입니다.
my_print(18) #my_print()실행, my_print()의 리턴값 출력

print('='*20)

def my_print2(name, age):
    print(name + '은 '+ str(age)+'살입니다.')
    print(name,'은',age,'살입니다.')
    print(f'{name}은 {age}살입니다.')
my_print2('정현진', 20)
my_print2(age=80, name='정가을') #아규먼트 순서와 관계없이 값을 넣을 수 있음

print('='*20)

def my_print3(name, age, group):
    print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
    print(name,'은',age,'살입니다.',group,'소속입니다.')
    print(f'{name}은 {age}살입니다. {group} 소속입니다.')
my_print3(age = 30, name = '정현진', group = '미림여정')
#my_print3(30, name = '정현진', '미림여정') 키워드 인자 뒤에는 계속 키워드 인자로 해야함
my_print3('정현진', group = '미림여정', age = 30) #위치 인자는 무조건 키워드 인자 앞에 있어야 함

print('='*20)

def my_print4(name, age, group='스트레이키즈'):
    print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
    print(name,'은',age,'살입니다.',group,'소속입니다.')
    print(f'{name}은 {age}살입니다. {group} 소속입니다.')
my_print4(age=22, name='이용복')
my_print4(age = 22, name = '이용복', group='댄스라차')

print('='*20)

def my_print5(name, *args): #args 자료형은 tuple
    print(f'{name} 정보: ')
    print('정보 : ')
    for arg in args:
        print(arg)
my_print5('이용복', 22, '스트레이키즈', '매니악')
my_print5('황현진', 22, '스트레이키즈', '매니악')

print('='*20)

# def my_print4(name, age=20, group): #기본값 있는 파라미터 뒤에는 무조건 기본값있는 파라미터
#     print(name + '은 '+ str(age)+'살입니다. ' + group + ' 소속입니다.')
#     print(name,'은',age,'살입니다.',group,'소속입니다.')
#     print(f'{name}은 {age}살입니다. {group} 소속입니다.')