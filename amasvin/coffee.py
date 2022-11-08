from drink import Drink


class Coffee(Drink):
    pass

coffee1 = Coffee('카페모카', 3500)
coffee1.order()
print(coffee1)