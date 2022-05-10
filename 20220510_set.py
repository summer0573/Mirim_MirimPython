games = {"LoL", "Overwatch", "Tetris", 1942, 2048}
print(games) #집합은 인덱스로 가져올 수 없다.
empty_set = {} #빈 딕셔너리
empty_set = set() # 빈 셋
print(set({'goole': 'goole.com', 18: 'unesco.org'}))

#요소 추가
games.add("테일즈런너")
print(games)
games.update(("카트라이더", "지렁이"))
print(games)

#셋 연산
#교집합
#합집합
#차집합
#대칭 차집합
#p56,57 실습고고
#p57 표 ***** 즁요 시험문제 백퍼
a = set()
a.add('밥')
a.add('국')
print(a)
a.add('밥')
print(a)
idol = ['세븐틴', '스트레이키즈', '악뮤', '방탄소년단', '방탄소년단']
print(idol)
print(list(set(idol))) #중복 제거: set() > list()