s = '1A 2F 1C'
s = '1A 3C 2B 40G 5A 1F 1C'
seat = '40G'


def seat2vector(s):
    s = s.upper()
    l = (s[-1])
    c = ord(l) - 65
    if l > 'H':
        c = c - 1
    r = int(s[:-1])
    return [r, c]


def s2array(s):
    a = []
    seats = s.split()
    for seat in seats:
        a.append(seat2vector(seat))
    return a


def busySeatsInRow(r, s):
    rez = []
    a = s2array(s)
    for busy in a:
        if busy[0] == r:
            rez.append(busy[1])
    return sorted(rez)


def solution(n, s):
    res = 0
    for i in range(1,n+1):
        busy = busySeatsInRow(i,s)
        c=1
        for i in range(0,3):
            if i in busy:
                c=0
                break
        res+=c
        c=1
        if (3 in busy) and (6 in busy):
            c=0
        if (4 in busy) or (5 in busy):
            c=0
        res+=c
        c=1
        for i in range(7,10):
            if i in busy:
                c=0
                break
        res+=c
    return res




print(solution(4,s))

# print(busySeatsInRow(1, s))