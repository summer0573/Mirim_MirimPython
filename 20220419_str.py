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
# #역행은 출력되지 않음