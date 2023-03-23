distance = int(input())
oc, of, od = map(int, input().split())
cs, cb, cm, cd = map(int, input().split())


online_taxi_fare = oc + (distance - of) * od
classic_taxi_fare = cb + (distance / cs) * cm + distance * cd

if online_taxi_fare > classic_taxi_fare:
    print("Classic Taxi")
else:
    print("Online Taxi")