def solution(t):
    l = len(t)
    for i in range(1, l):
        w = t[:i]
        s = t[i:]
        print(i, w, s)
        if max(w) < min(s):
            print(i,w,s)


(solution([-5, -5, -5, -42, 6, 12]))
