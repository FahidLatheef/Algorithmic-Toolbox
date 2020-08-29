def compute_min_refills(distance, tank, stops):
    refill = 0
    distance_covered = 0
    while distance_covered < distance - tank:
        #print("1")
        temp_max = max(list(filter(lambda x: x <= tank, stops))+[-1])
        #print("tm: ",temp_max)
        if temp_max == -1:
            #print("2")
            return -1
        else:
            #print("3")
            distance_covered += temp_max
            #print(distance_covered)
            refill += 1
            stops = [x - temp_max for x in stops]
            stops = list(filter(lambda x: x > 0,stops))
            #print(stops)
    return refill

d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(d, m, stops))

