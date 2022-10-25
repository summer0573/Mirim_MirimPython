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
        self.cup_size = '레귤러'
        self.sugar = '50%'
        self.ice = '기본'

    def __str__(self):
        return f'이름 : {name}\t가격 : {price}원\t컵사이즈 : {self.cup_size}\t \
        당도 : {self.sugar}\t얼음량 : {self.ice}'


drink1 = Drink('아메리카노', 1800)
print(drink1)
