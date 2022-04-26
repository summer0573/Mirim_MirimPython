empty_list = []
player = ['Faker', 10, True]
print(len(empty_list)) #0
print(len(player)) #3

print(type(empty_list), type(player))
empty_list2 = list()
print(len(empty_list2)) #0

message = list('miracle')
print(message) #['m', 'i', 'r', 'a', 'c', 'l', 'e']
# numbers = list(56) #TypeError: 'int' object is not iterable
# print(numbers)
print(player)
#리스트 추가
player = player + [10, 11] #player += [10, 11] 리스트 풀려서 하나씩 추가 #['Faker', 10, True, 10, 11]
print(player)
player.append([20, 21]) #리스트 통째로 추가 #['Faker', 10, True, 10, 11, [20, 21]]
print(player)
player.append(56)
print(player)
player.insert(2, 'SKT T1') #index, 값 #2번 자리에 넣음 #['Faker', 10, 'SKT T1', True, 10, 11, [20, 21], 56]
print(player)
player.extend([30,31]) #+=랑 같음, 즉 풀려서 하나씩 추가 #['Faker', 10, 'SKT T1', True, 10, 11, [20, 21], 56, 30, 31]
print(player)

# append() = 리스트 통째로 추가
# insert() = index에 값 추가
# +=, extend() = 리스트 풀어서 하나씩 추가

print(player)
player.append(40)
print(player)
#맨 끝에 50추가 insert()
player.insert(11, 50)
#player.insert(-1, 50) #실패, 맨마지막 두번째에 추가, 마지막거 뒤로 밀림
print(player)
player.insert(len(player),51) #append()와 같음
print(player)
#수정
print(player[0:4])
print(player[0])
player[0]= '스티치'
print(player[0])
print(player)
print(player[6])
player[6]=16
print(player)
#삭제거
del player[2] #인덱싱으로 지우기
print(player)
player.remove(30) #값으로 지우기
print(player)
player.pop() #맨 뒤에서 지우기
print(player)
player.pop(2) #인덱스로 지우기
print(player)
# player.clear() #리스트 초기화
# print(player)
#remove(): 값으로 지우기
#pop(index), del 리스트명[index]: 인덱스로 지우기
#pop(): 맨 뒤에서 지우기
print(100 in player) #False
print(10 in player) #True
print('아이유' in player) #False
# print(player)
# player.sort() #TypeError: '<' not supported between instances of 'int' and 'str' #int와 string은 정렬을 못함
print(player)
player[0]=1
print(player)
player.sort() #정렬
print(player)
player.reverse() #뒤집기, 내림차순 정렬은 아님
print(player)

#**range
a=range(14)
print(a)
a2=list(a)
print(a2)
print(list(range(14)))
b = range(1,14+1) #시작숫자와 끝숫자
print(list(b))
c=range(1, 14+1, 2)
print(list(c))
#range(stop):range(0,stop):0,1,2,...,stop-1
#range(start, stop):start, start+1, start+2, ..., stop-1
#range(start, stop, step): start, start+step, start+step+step, ..., stop-1
class1 = list(range(1, 14+1))
class2=list(range(1,14+1))
class3=list(range(1,14+1))
class3.remove(10)
#두자리 숫자 홀수 출력
number=range(11, 99+1, 2)
print(list(number))

#한자리 숫자 중 짝수 숫자 거꾸로
print(1, 9+1, 2)ㅏ