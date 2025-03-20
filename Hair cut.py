
#함수
def show_price(customer,sex):
    print(f'{customer} 고객님')
    price = 0
    if sex == '남자':
        price = 10000
        print(f'{sex}는 {price}원 입니다.')
    elif sex == '여자':
        price = 15000
        print(f'{sex}는 {price}원 입니다.')
    else:
        print('잘못된 입력입니다.')

    return



customer1 = '홍길동'
sex1 = '남자'
show_price(customer1,sex1) #함수호출

customer2 = '김복희'
sex2 = '여자'
show_price(customer2,sex2)

customer = input('이름을 입력하세요.')
sex = input('성별을 입력하세요.')
show_price(customer, sex)


