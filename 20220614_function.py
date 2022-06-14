#예약어X
#snake_case
#내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#sum = 0 TypeError: 'int' object is not callable
#def sum(x) : 내장함수와 이름이 같으면 에러는 안나지만, 내장함수를 호출할 수 없음
#print(x)


a = sum(10, 20, 3)
print(a)