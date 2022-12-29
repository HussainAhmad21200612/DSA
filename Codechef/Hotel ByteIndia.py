for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    dep = list(map(int,input().split()))
    times = [(arr[i], 1) for i in range(n)] + [(dep[i], -1) for i in range(n)]
    times.sort()
    
    maxGuests = 0
    guests = 0
    for time, change in times:
        guests += change
        maxGuests = max(maxGuests, guests)
    print(maxGuests)
