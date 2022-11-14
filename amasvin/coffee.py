from drink import Drink


class Coffee(Drink):
    pass

if __name__ == '__main__':
    coffee1 = Coffee('카페모카', 3500)
    coffee1.order()
    print(coffee1)