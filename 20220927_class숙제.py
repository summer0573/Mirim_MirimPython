class Human:
    def __init__(self, name):
        self.name = name
        self.birth = None
        self.age = None

    def set_birth(self, birth):
        self.birth = birth

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f'이름: {self.name}\t생일: {self.birth}\t나이: {self.age}'

hyunjin = Human('정현진')
hyunjin.set_birth('050703')
hyunjin.set_age(18)
print(hyunjin)

yejin = Human('이예진')
yejin.set_birth('050715')
yejin.set_age(18)
print(yejin)

'''
PYTHON  
변수, 함수 : snake_case
클래스 : CamelCase
set함수 : 웬만하면 조건 붙여서

'''

#예서가현
class Food:
    def __init__(self, name):
        self.name = name
        self.style = None
        self.money = 0
    def set_style(self, style):
        self.style = style
    def set_money(self, money):
        if money < 0 :
            self.money = 0
        else :
            self.money = money
    def __str__(self):
        return f'{self.name}\t 비용 : {self.money}\t style : {self.style}'

print('-'*20)

class Delivery(Food):
    def __init__(self, name):
        super().__init__(name)
        self.delivery_money = 0
    def set_delivery_money(self, de_m):
        self.delivery_money = de_m
    def __str__(self):
        return f'{super().__str__()}\t 배달료 : {self.delivery_money}원'

치킨 = Delivery('처갓집')
치킨.set_style('튀김')
치킨.set_money(36000)
치킨.set_delivery_money(2500)
print(치킨)

class StreetFood(Food):
    def __init__(self, name):
        super().__init__(name)
        self.shape = None
        self.season = None

    def set_shape(self, shape):
        self.shape = shape

    def set_season(self,season):
        self.season = season

    def __str__(self):
        return f'{super().__str__()}\t 매장 형태 : {self.shape}\t 계절 : {self.season}'

붕어빵 = StreetFood('황금 붕어빵')
붕어빵.set_style('빵')
붕어빵.set_money(5000)
붕어빵.set_shape('수레')
붕어빵.set_season('겨울')
print(붕어빵.__str__())

print('-'*20)

#채영소리
#옆친구와 클래스 구조 만들고
#객체화 하고
#상속하고
#출력

'''
사람 - 이름, 나이, 성별
선생님 - 과목, 담임반
'''
'''
클래스는 웬만하면 단수. 단, 여러개 담으면 복수
수치가 들어오는 값이면, 가능하면 숫자로 세팅하자.
    나이, 생년 등은 숫자, 핸드폰 번호는 문자로
    
변수, 함수, 클래스명 명확하게
이제 더 이상 내 코드는 나만 봄X
누구나 내 코드 읽을 수O
'''

class People:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.gender = None

    def set_age(self, age):#매개변수와 함수이름을 같게하지말것
        self.age = age

    def set_gender(self, gender):
        genders = ['여자','남자']
        if gender in genders:
            self.gender = gender
    def __str__(self):
        return f'{self.name}\t{self.age}\t{self.gender}'

# people에 값넣기
고나근샘 = People('고낙은')
고나근샘.set_age(34)
고나근샘.set_gender('남자')
print(고나근샘)

class Teacher(People):
    def set_subject(self, sub):
        self.sub = sub
    def HRT(self, hrt):
        self.hrt = hrt
    def __str__(self):
        return f'{super().__str__()}\t담당과목: {self.sub}\t담임반: {self.hrt}'


#Teacher에 값넣기
고낙은샘 = Teacher('고낙은')

고낙은샘.subject('체육')
고낙은샘.HRT('2-2')
print(고낙은샘)