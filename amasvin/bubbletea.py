from drink import Drink


class BubbleTea(Drink):
    _PEARLS = ('타피오카', '곤약', '코코넛', '알로에')

    def __init__(self,name, price):
        super().__init__(name, price) #시험 부모의 생성자를 호추라기
        self.set_pearl = 0;
    def __str__(self):
        return f'\n펄 : {BubbleTea._PEARLS[self.pearl()]}'

    def set_pearl(self):
        for index, pearl_label in enumerate(BubbleTea._PEARLS):
            print(f'{index + 1} : {pearl_label}펄')
        pearl = input('펄을 선택하세요 : ')
        # if pearl == '':  # 그냥 엔터치면 기본값 넣기
        #     self.pearl = 0
        # else:
        #     self.pearl = int(pearl) - 1
        self.pearl = 0 if pearl == '' else int(pearl) - 1

    def order(self):
        super().order()
        self.set_pearl()


bubbletea1 = BubbleTea("순수우유 쉐이크", 3900)
bubbletea1.order()
print(bubbletea1)