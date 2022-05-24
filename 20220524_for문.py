# #문자열
# for ch in "SORI":
#     print(ch, end = ' ')
#
# print()
#
# #리스트
# for item in ["힙합", "발라드"]:
#     print(item)
#
# for a,b in ((12,33),(2,35)):
#     print(a,b)
#
# #튜플
# for item in (2999, 39393):
#     print(item)
#
# #셋
# for item in {"WSM", "JAVA", "Python"}:
#     print(item)
#
# #딕셔너리
# pl = {"C":1972, "JAVA":2341, "Python":1487}
# for item in pl:
#     print(item)
# for key in pl.keys(): #key에 문자 저장
#     print(key)
# for val in pl.values(): #val에 숫자 저장
#     print(val)
# for key, val in pl.items(): #문자와 숫자 각각 저장
#     print(key, val)

# #num_list 문제
# for num_list in [-5, 127, -13, 9, -21, 100]:
#     if num_list > 0:
#         print(num_list)

#짝수, 홀수
# num_list = [13, 8, 7, 55, 100, 2, 12, 10, 17]
# for num in num_list:
#     if num % 2 == 0:
#         print(f'{num}은 짝수이다')
#     else:
#         print(f'{num}은 홀수이다.')
#
# print('------------------------------------')
# holzzak = ["짝수", "홀수"]
# for num in num_list:
#     print('{}은 {}이다.'.format(num, holzzak[num%2]))
#
# #자리수
# for num in num_list:
#     print('{}은 {}자리수이다.'.format(num,len(str(num))))

# skz = {"한":90, "창빈":30, "아이엔":95, "승민": 50, "현진":100, "방찬":10, "리노":60, "용복":100}
# for name, score in skz.items():
#     if score >= 60 :
#         print('{}은/는 합격입니다.'.format(name))
#     else :
#         print('{}은/는 불합격입니다.'.format(name))

#range()함수
#range(시작값, 종료값, 단계)
#range(기본값 0, 종료값, 기본값 1)
# print(list(range(0, 10, -1)))
# print(list(range(10, 0, -1))) #단계값이 음수면 역순
# print(list(range(0, 10, 5)))
#
# print(list(range(0, 10)))
# print(list(range(10)))
# #
# #리스트
# nctdream = ['런쥔', '제노', '해찬', '마크', '재민', '지성', '천러']
# for member in nctdream:
#     print(member)
#
# print("================================")
#
# for i in range(0,len(nctdream)):
#     print(i+1, nctdream[i])
#
# print("================================")
#
# for i, member in enumerate(nctdream):
#     print(i+1, member)

#1번 문제
ssuumm = 0
for num in range(0, 200, 3):
    ssuumm += num

print(f'{ssuumm}')

#2번 문제
ssuumm = 0
for num in range (500 , 1000, 5):
    ssuumm+=num

print(f'{ssuumm}')

l = [1,2,3,4,5]
print(sum(l))
print(max(l))
print(min(l))
