#전화번호를 인자로 받아, 각 숫자 중 홀수만 더해서 합계를 리턴하는

def sum_odd(phone_number):
    pass
# 수학 합계 주하기
    sum_value = 0
#전화번호에서 하나씩 꺼내자ㄴ
    for number in phone_number:
        number = int(number)
        if number % 2 != 0:
            print(number)
            sum_value += number
    return sum_value

result = sum_odd('01072404658')
print((result))

def sum_odd2(phone_number) :
    return sum([int(number) for number in phone_number if int(number) % 2 != 0])