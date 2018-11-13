def solution(a):
    l=len(a)
    for i in range(l,0,-1):
        print(i)
        for j in range(0,l-i+1):
            sa = (a[j:j+i])
            # if len(set(sa))==2:
            #     return i
    return 1



print(solution([5, 4, 4, 5, 0, 12]))