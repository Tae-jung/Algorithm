# 1은 가위 2는 바위 3은 보
def tournament(S, E, match):
    if S == E:
        return S
    else:
        c1 = tournament(S, (S + E)//2, match)
        c2 = tournament((S + E)//2 + 1, E, match)
        return win(c1, c2, match)

def win(x, y, match):
    if match[x] == match[y]:
        return x
    elif match[x] > match[y]:
        x, y = y, x
    
    if match[y] - match[x] == 1:
        return y
    elif match[y] - match[x] == 2:
        return x



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    match = [0] + list(map(int,input().split()))
    print('#{} {}'.format(tc, tournament(1, N, match)))