class Celebrity:
    def __init__(self, name):
        self.name = name
        self.debut_date = None
        self.company = None

    def set_decut_date(self, debut_date):
        self.debut_date = debut_date

    def set_company(self, company):
        self.company = company

    def __str__(self):
        return f'{self.name}\t{self.debut_date}\t{self.company}'
아이유 = Celebrity('이지은')
#아이유.decut_date = '2008-09-18' 이렇게 하지 않기
아이유.set_decut_date('2008-09-18')
아이유.set_company('이담엔터테인먼트')
print(아이유)

class Singer(Celebrity):
    def set_song(self, song):
        self.song = song
    def __str__(self):
        return f'{super().__str__()}\t대표곡 : {self.song}'

teamin = Singer('이태민')
teamin.set_company('SM 엔터테인먼트')
teamin.set_song('MOVE')
print(teamin)

class Actor(Celebrity):
    def __init__(self, name):
        super().__init__(name) #name, debut_date, company
        self.drama = None
    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return f'{super().__str__()}\t대표작 : {self.drama}'
정경호 = Actor('정경호')
정경호.set_decut_date('2003-00-00')
정경호.set_drama('슬의생')
print(정경호)

내아가들 = [teamin, 정경호]
print(내아가들)
for 내아가 in 내아가들:
    print(내아가)


