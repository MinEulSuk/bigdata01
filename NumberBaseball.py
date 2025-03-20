import random

ran_save = []
while len(ran_save) < 4:  # 4자리 숫자를 생성하여 k라는 리스트에 삽입함
    rannum = random.randrange(1, 10)
    if rannum not in ran_save:
        ran_save.append(rannum)
# print(f'{ran_save}')
ball_save, strike_save, try_save = 0, 0, 0  # 볼, 스트라이크, 횟수 선언

while True:
    getnum = input('숫자야구 게임입니다. 4자리 숫자를 입력해주세요. ')

    # 받은 숫자가 4자리이고 숫자인지, 중복이 없는지 확인
    if len(getnum) == 4 and getnum.isdigit() and len(set(getnum)) == 4:
        num_list = list(map(int, getnum))  # 각 문자를 정수로 변환 후 리스트로 저장

        # 스트라이크, 볼 개수 세기
        for f in range(0, 4):
            if num_list[f] == ran_save[f]:  # 위치와 숫자가 일치하면 스트라이크 값 올리기
                strike_save += 1
            elif num_list.count(ran_save[f]) == 1:  # 숫자만 일치하면 볼 값 올리기
                ball_save += 1

        try_save += 1

        if strike_save == 4: #승리기준
            print(f'축하드립니다. {try_save}번 도전하여 승리하셨습니다.')
            break
        if try_save > 20: #패배기준
            print('패배하셨습니다.')
            break



        print(f'스트라이크는 {strike_save}개, 볼은 {ball_save}개 입니다.')
        if try_save % 5 == 0:
            while True:
                hint = input('힌트를 보시려면 "힌트"라고 입력해주세요.')
                if hint == '힌트':
                    num_save = try_save // 5
                    print(f'{num_save}번째 값은 {ran_save[num_save-1]}입니다.')
                    break
                else:
                    print('잘못된 입력입니다.다시 입력해주세요.')
        ball_save, strike_save = 0, 0  # 볼과 스트라이크 초기화
    else:
        print("4자리 숫자를 정확히 입력하세요.")




        