greeting = 'Hello'
to = 'world'
say_hello = greeting + ', ' + to
print(say_hello)
print(greeting * 5)
print(greeting + '\n' + to )
print("\"" + greeting + "\"")
print('\'' + greeting + '\'')
names = '''양다연
인소리
이예진
'''

print(names)

#*****시험 백퍼 나옴
#indexing, slicing
names = '양다연인소리이예진'
print(names[2]) #연 출력
print(names[4]) #소 출력
print(names[8]) #진 출력
print(names[-1]) #진 출력
print(names[-2]) #진 출력
print(names[-9]) #양 출력
student_number = '2112'
print(student_number[0] + '학년')
print(f'{student_number[0]}학년')
print(f'{student_number[1]}반')
#'양다연인소리이예진'
print(names[2:5]) #[2]~[4]까지 출력 [5]는 포함이 되지 않음
print(names[2:4]) #연인
print(names[4:7]) #소리이
print(names[7:9]) #예진
print(f'{student_number[2:4]}번')
print(f'{student_number[-2:4]}번')
print(f'{student_number[-2:]}번') #start: end-1 [start:] 뒤에 숫자가 없으면 끝까지 출력함
print(f'{student_number[0:-2]}학년반')
print(f'{student_number[:-2]}학년반') #start : end-1 [:end - 1] = 앞까지 출력
print(f'{student_number[:]}학년반') #start : end-1 [:] = 앞~끝 전부다 출력
#역행으로는 출력되지 않음

#문자열 함수
print(f'길이: {len(student_number)}') #길이를 알 수 있음
print(f'2 개수: {student_number.count("2")}') #count 특정 문자열이 몇개가 있는지 알 수 있음
print(f'{"nct dream darling".upper()}') #대문자로 바꿈
print(f'{"NCT DREAM DARLING".lower()}') #소문자로 바꿈

s = "    NCT dream buffering    "
print(f'{s.strip()}') #양 옆에 띄어쓰기를 없앰
print(f'{s.lstrip()}') #왼쪽 띄어쓰기를 없앰
print(f'{s.rstrip()}') #오른쪽 ``

print(f'{s.find("e")}') #[8]
print(f'{s.find("z")}') #없으면 -1
# print(f'{s.rfind("e")}')
# print(f'{s.lfind("e")}')

print(f'{s.index("d")}') # 8
# print(f'{s.index("z")}') #없으면 ValueError

print(f'{s.replace("bufferuing", "Hello Future")}') #replace하면 바뀐 문자열 리턴하지만 원본은 바뀌지 않음

print('e' in s) #true
print('z' in s) #False

#split, join
ip = '10.253.123.119'
ip_list = ip.split('.')
print(ip_list)

names = '양다연, 최자윤, 임채영, 이예진, 인소리'
name_list = names.split(',')
print(name_list)
print(name_list[2])
print(name_list[2:4])
ip_list_str = '::'.join(ip_list)
print(ip_list_str)
name_list_str = '|'.join(name_list)
print(name_list_str)
print(",".join(name_list))

#format
s='name: {}, number: {}, soccer: {}'
print(s.format('손흥민', 7, True))

a='name: {1}, number: {2}, soccer: {0}'
print(s.format('손흥민', 7, True))

b='name: {me}, number: {n}, soccer: {s}'
print(s.format(m='손흥민', n=7, s=True))

