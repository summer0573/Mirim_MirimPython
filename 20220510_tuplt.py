t = () #빈 튜플 / 튜플 = 여러 개의 값을 담고 있지만 그걸 한 덩어리로 본다.
xy = (2560,1440)
color = 129, 247, 216
print(t)
print(xy)
print(color)
print(xy+color) #(2560, 1440, 129, 247, 216)
print(xy*2) #(2560, 1440, 2560, 1440)
(2560, 1440, 129, 247, 216)
#패킹, 언패킹 : 자동
color = 129, 247, 216 # = 패킹
red, green, blue = color # = 언패킹
print(red)
x, y =(1920, 1080)
print(y) #1080
print(color[1]) #인덱싱
print(color[0:2]) #슬라이싱
# color[1] = 255 에러남 값을 넣으면 다시 넣거나 바꾸는 기능을 지원하지 않은다.
new_tuple = xy+color+(1440, 1080)
print(new_tuple) #(2560, 1440, 129, 247, 216, 1440, 1080)
print(new_tuple.index(1440)) #1
print(new_tuple.count(1440)) #2
임채영, 이예진 = 10, 8
print(임채영)
print(이예진)
이예진, 임채영 = 임채영, 이예진
print(임채영)
print(이예진)