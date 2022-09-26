#2111 정현진

# 1
# def sum_odd(num):
#     int(num)
#     ssum = 0
#     for i in num:
#         if i % 3 == 0:
#             ssum += i
#     return ssum
#
# result = sum_odd('01012345678')
# print(result)
# result = sum_odd('01022224444')
# print(result)
# result = sum_odd('01099999999')
# print(result)

# 2
def enctypt(word):
    for i in word:
        if i == 'a' and i == 'e' and i == 'i' and i == 'o' and i == 'u':
            i = '*'
    return i

print(enctypt('ive'))
print(enctypt('nct dream'))
print(enctypt('AEiou'))
print(enctypt('GOOGLE'))
print(enctypt('BTS'))

#3
def dec_to_bin(sipjinsu):
    result = bin(sipjinsu)

    return result
print(dec_to_bin(10))
print(dec_to_bin(2))
print(dec_to_bin(77))
print(dec_to_bin(1024))

#4
def abbreviate(name):
    result = name.find(' ')
    result2 = name[:1] + '.'

    return result2.upper()
print(abbreviate("Maverick"))
print(abbreviate("HAE CHAM"))
print(abbreviate("jin young park"))

#5
def fare_pc(minute):
    if minute >= 10:
        a = minute % 100 // 10
        pay = a * 1000
        if minute % 10 > 0 :
            pay += 1000

    elif minute < 10:
        pay = 1000
    return pay

print(fare_pc(minute=3))
print(fare_pc(minute=20))
print(fare_pc(minute=34))

#6
def get_bmi(height, weight):
    bmi = weight % height * height
    if bmi < 18.5:
        biman = "저체중"
    elif 18.5 <= bmi < 23:
        biman = "정상"
    elif 23 <= bmi < 25:
        biman = "과체중"
    elif 25 <= bmi:
        biman = "비만"
    return biman, bmi
print(get_bmi(height = 170, weight = 60))
print(get_bmi(height = 150, weight = 60))
print(get_bmi(height = 180, weight = 50))
print(get_bmi(height = 160, weight = 60))

# 7
# def minus_time
#








































#2111 정현진