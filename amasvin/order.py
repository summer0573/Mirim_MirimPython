from coffee import Coffee  # coffee모듈(.py), Coffee (클래스)
from bubbletea import BubbleTea


class Order:
    def __init__(self):
        pass
        self.menu = []  # 메뉴판
        self.init_menu() #메뉴판 초기화

        self.order_menu = []  # 주문한 음료 리스트

    def __str__(self):
        pass

    def init_menu(self):  # 메뉴판 초기화
        new_menu = BubbleTea("하농녹차오레오", 4500)
        self.menu.append(new_menu)
        new_menu = Coffee("카페 모카", 3000)
        self.menu.append(new_menu)
        new_menu = Coffee("라즈베리소다", 2900)
        self.menu.append(new_menu)

    def order(self):
        # 반복
        self.show_menu()  # 메뉴판 보이기

    # 음료수 고르기(사용자 입력받기)
    # 새로운 음료수로 생성하고, 옵션들 주문받기
    # 주문한 음료수 리스트에 새로운 음료수 추가하기

    # 주문한 음료수 리스트 출력하기pass
    def show_menu(self):
        for index, drink in enumerate(self.menu):
            print(f'{index + 1}. {drink.name}\t{drink.price}')

if __name__ == '__main__':
    order = Order()
    order.show_menu()