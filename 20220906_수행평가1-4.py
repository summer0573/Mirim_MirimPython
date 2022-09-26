import abbreviate as abbreviate


def abbreviate(name):
    name = name.strip()
    #한글자씩 꺼내기 -> 대문자로 바꾸고 > 저장
    for index, sp in enumerate(name):
    #띄어쓰기 파악 -> 한칸 뒤에 있는 글자를 저장
        if index == 0:
            result = sp.upper() + '. '
        if sp == ' ':
            result += name[index + 1].upper() + '. '
        return result.strip()

def abbreviate2(name):
    result = '. '.join([word[0].upper() for word in name.split()])
    return result + '.'

print(abbreviate('dong ju son'))
print(abbreviate('yeo hwan woong'))
print(abbreviate('lee geon hwi'))

print(abbreviate2('dong ju son'))
print(abbreviate2('yeo hwan woong'))
print(abbreviate2('lee geon hwi'))