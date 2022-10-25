# Drink
# name
# price
# cup_size
# sugar
# ice
# Drink <- Coffee
# Drink <- Bubbletea
# 옵션들
# 컵사이즈 : 기본, 점보
# 펄 : 타피오카, 알로에, 코코넛, 곤약
# 당도 : 30%, 50%, 70%, 100%
# 얼음량 : 없음, 적게, 기본, 많게
class Drink:
    # 클래스 변수
    _CUP_SIZES = ('레귤러', '점보')  # 0: 레귤러, 1 : 점보
    _SUGARS = ('30%', '50%', '70%', '100%')
    _ICES = ('없음', '적게', '기본', '많게')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup_size = 0
        self.sugar = 1
        self.ice = 2

    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}원\t컵사이즈 : {Drink._CUP_SIZES[self.cup_size]}\t \
        당도 : {Drink._SUGARS[self.sugar]}\t얼음량 : {Drink._ICES[self.ice]}'

    def set_cup_size(self):
        #사용자에게 숫자를 묻자 1 : 레귤러, 2 : 점보
        for index, cup_size_label in enumerate(Drink._CUP_SIZES):
            print(f'{index + 1} : {cup_size_label}')
        cup_size = input('컵사이즈를 선택하세요 : ')
        if cup_size == '':#그냥 엔터치면 기본값 넣기
            self.cup_size = 0
        else:
            self.cup_size = int(cup_size) - 1
        #self.cup_size가 점보일때, self.price += 500원
        if self.cup_size == 1:
            self.price += 500



drink1 = Drink('아메리카노', 1800)
drink1.set_cup_size()
print(drink1)
