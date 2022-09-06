

'''
def dec_to_bin(number):
    return bin(number).replace('0b', '')

def dec_to_bin(number):
    #share : 몫, reminder: 나머지
    #넘버를 2로 나누고, 몫이 0이면, 끝내고 결과 리턴
#아니면 넘버를 2로 나눈 나머지를 보관
#넘버는 넘버를 2로 나눈 몫으로 설정
'''

def dec_to_bin(number):
    #share : 몫, reminder: 나머지
#무한반복
    #넘버를 2로 나누고, 몫이 0이면, 끝내고 결과 리턴
    #아니면 넘버를 2로 나눈 나머지를 보관
        #넘버는 넘버를 2로 나눈 몫으로 설정
    s = ''
    while True:
        if number == 0:
            return s
        else:
            reminder = number % 2
            s = str(reminder) + s
            number = number // 2


print(dec_to_bin(10))
print(dec_to_bin(2))
print(dec_to_bin(77))
print(type(dec_to_bin(10)))

# print('0b1010'[2:1])

