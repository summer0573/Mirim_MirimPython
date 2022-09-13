'''
속성
제목
장르
플랫폼

객체
실행하다
저장하다
로그인하다
}
'''
class Game:
    def __init__(self, title):#특수메소드: 생성자
        self.title = title
        self.genre = 'MMORPG'
        self.platform = 0

    def run(self):
        print("실행합니다.")
    def login(self):
        print(f'{id}님 환영합니다')
    def save(self):
        print('저장완료')
    def __str__(self): #특수메소드: 문자열표현
        return f'{self.title} {self.genre}'
예서게임 = Game('World of Warcraft')
채영게임 = Game('Minecraft')
채영게임.genre = '샌드박스'
print(예서게임)
print(채영게임)
