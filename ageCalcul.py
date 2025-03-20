def solution(n):
    answer = 0
    for k in range(1,int(n)+1):
        if k % 2 == 0:
            answer += k
    return answer

print(f'{solution(6)}')