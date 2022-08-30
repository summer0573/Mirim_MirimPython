def encrypt(word) :
    #영단어를 한글자씩 꺼냄
    for char in word:
        result = ''
        # print(char)
        if char == 'a' or char == 'e' or char == 'i' or char =='o' or char == 'u':
            char = '*'
            result += char
        else:
            result += char
    return result

print(encrypt('ive'))
# string = ' '
# for 하나 in 덩어리:
#     string += 하나