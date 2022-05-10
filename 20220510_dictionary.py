#dictionary: 사전: '단어': '뜻': key: value
d = {}
urls={'goole':'goole.com', 18:'unesco.org'}
print(d)
print(urls)

#요소 추가
urls['유튜브'] = 'youtube.com' #{'goole': 'goole.com', 18: 'unesco.org', '유튜브': 'youtube.com'}
print(urls)

#요소 수정
urls['goole'] = 'goole.co.kr'
print(urls) #{'goole': 'goole.co.kr', 18: 'unesco.org', '유튜브': 'youtube.com'}

#요소 출력
print(urls['goole'])
print(urls[18]) #18:키 인덱스의 18과 딕셔너리의 18은 다르다.

#요소 제거
del urls['유튜브']
print(urls)
#urls.pop()
urls.pop(18) #key 값을 안주면 에러남
print(urls) #{'goole': 'goole.co.kr'}

birthdays = {'다연': 5, '자윤' : 11}
birthdays_list = [5, 11]
print(birthdays['다연'])
print(birthdays.get('다연'))
print('goole.co.kr' in urls) #False
print('goole' in urls) #True
print('goole.co.kr' in urls.values()) #True
urls['유튜브'] = 'youtube.com'
print(urls.values()) #값들 dict_values 객체
print(urls.keys()) #키들 리스트 dict_keys 객체
print(urls.items()) #(키, 값) 튜플들 dict_items 객체
