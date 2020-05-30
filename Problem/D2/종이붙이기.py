# 작은 경우부터 조금씩 늘려서 법칙을 찾아내보자 -> 피보나치 참고
def function(N):
    if N < 2:
        return 1
    else:
        return 2*function(N - 2) + function(N - 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())//10
    print('#{} {}'.format(tc, function(N)))


## 맨 처음의 코드: 완전탐색으로 가능한 모든 경우의 수를 대입 -> 시간이 너무 오래걸림
# def DFS(N, P, hap):
#     global cnt
#     if hap == N:
#         cnt += 1
#     elif hap > N:
#         return
#     else:
#         for key, value in P.items():
#             for v in value:
#                 DFS(N, P, hap + key)
    

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     P = {10: [10], 20: [10, 20]}
#     cnt = 0
#     DFS(N, P, 0)
#     print('#{} {}'.format(tc, cnt))
