class human:
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

hyunjin = human('정현진')
hyunjin.set_birth('050703')
hyunjin.set_age(18)
print(hyunjin)

yejin = human('이예진')
yejin.set_birth('050715')
yejin.set_age(18)
print(yejin)