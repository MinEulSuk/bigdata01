#리스트는 대괄호[] 특징 : 수정 가능, 순서 존재, 중복 있음
    #요소의 순서가 중요하고, 수정이 필요한 경우에 사용

#튜플은 소괄호()  특징 : 수정 불가능, 순서 존재, 중복 있음
    #요소의 순서가 중요하지만, 수정이 필요하지 않은 경우에 사용

#세트는 중괄호{}  특징 : 수정 가능, 순서 없음, 중복 없음
    # 요소의 순서가 중요하지 않고, 중복된 요소를 제거해야 할 때 사용

#딕셔너리는 중괄호{} 특징 : 수정 가능, 순서 없음,키와 밸류값 존재,
# 키값은 중복 없음 , 밸류값 중복 가능
    #키와 값의 쌍을 저장하고, 특정 키를 사용하여 값을 검색해야 할 때 사용


products = ['JOA-2021','JOA-2022','nemo-2021','nemo-2022']
#대괄호 리스트형태, 4개의 값, 중복이 되지만 중복값은 없고 순서가 있음
recall = []
#recall이라는 리스트형 자료에 값을 넣기위해 선언
for p in products:
# for x in y y값의 개수만큼 x번째에 해당하는 y의 값 쓰기
# 4개 값이므로 0부터 3까지 0 1 2 3
    if p.startswith('nemo'):
    #첫글자가 nemo라면
        recall.append(p)
        #recall에 p값을 추가해라

print(recall)

products = ['2021-nemo','nemo-2021','JOA-2022','nemo-2022']
#대괄호 리스트형태, 4개의 값, 중복이 되지만 중복값은 없고 순서가 있음
recall = []
#recall이라는 리스트형 자료에 값을 넣기위해 선언
for p in products:
# for x in y y값의 개수만큼 x번째에 해당하는 y의 값 쓰기
# 4개 값이므로 0부터 3까지 0 1 2 3
    if 'nemo' in p:
    #nemo가 p값 안에 존재한다면
    #find는 문자의 인덱스를 반환 , 문자의 위치 반환
        recall.append(p)
        #recall에 p값을 추가해라

print(recall)

products = ['JOA-2021','JOA-2022','nemo-2021','nemo-2022']
new_list = [x for x in products if 'nemo' in x]
#리스트 = [변수 활용 for 변수 in 반복대상 if 조건문]
#리스트컴프리헨션으로 압축한것
print(new_list)

