#숫자
student_number = 3419
age = 18
height = 160.2

#문자
name = '정현진'

print(f'학번: {student_number}\n이름: {name}\n나이: {age}\n키: {height}')

# print(type(student_number)) #<class 'int'>
# print(type(name)) #<class 'str'>
# print(type(age)) #<class 'int'>
# print(type(height)) #c<lass 'float'>
# print(type(10.27)) #c<lass 'float'>
# print(type(1027)) #<class 'int'>
# print(type('1027')) #<class 'str'>
# print(10/27) #java: 0, python:0.37037037037037035
# print(27/10) #java: 2, python:2.7
# print(27//10) #python: 나눈 몫: 2
# print(27%10) #python: 나머지: 7
# print(type(27/10)) #c<lass 'float'>

#변수 이름 규칙, 자료형변환
#my_mbti, my_funtion(), MyClass  #myMbti: camel-case, my_mbti: snake-case
my_mbti = 'INFP'
print(f'My MBTI: {my_mbti}')

print('MY MBTI:'+my_mbti+', age'+str(age)) # age를 string으로 바꿔줘야 한다. #java: String.toString(age); python: str(age)
height = '160.2'
print(float(height)+10) #java: Float.parseFloat(height) python: float(height)

#str() int() float()
#+연산자: 숫자+숫자=덧셈, 문자+문자=문자문자
#* 연산자: 숫자*숫자 => 곱셈, 문자*문자 => 문자를 숫자만큼 반복
print(18+2) #20
print("18"+"2") #'182'
print(18*2) #36
print('2'* 4) #2222
#짝을 10번 출력
print('짝'*10)
print(18**3) #거듭제곱
