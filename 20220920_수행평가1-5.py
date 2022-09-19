def fare_pc(minutes):
    share = minutes // 10 #몫 구하기
    fare = share * 1000
    if minutes % 10 != 0 :
        fare += 1000
    return fare

print(fare_pc(10))
print(fare_pc(30))
print(fare_pc(62))
