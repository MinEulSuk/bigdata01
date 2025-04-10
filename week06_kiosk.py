# 1) 아아 : 2000 2) 라떼 : 2500
prices = [2000,2500,4000]
drinks = ['아이스 아메리카노','카페 라떼','수박 주스']
amounts = [0,0,0]
total_price = 0
#order_list = ""

def order_process(idx):
    """
    주문 처리 함수 1) 주문 디스플레이 기능 2)총 주문 금액 누산 3) 수량 업데이트
    :return:
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다.")
    total_price += prices[idx]
    amounts[idx] += 1

menu_text = ""
for j in range(len(drinks)):
    menu_text += f'{j + 1}) {drinks[j]} {prices[j]}원 '
menu_text += f'{len(drinks) + 1}) 주문 종료 : '
while True:
    menu = input(menu_text)
    if menu == "1":
        order_process(int(menu)-1)
    elif menu == "2":
        order_process(int(menu)-1)
    elif menu == "3":
        order_process(int(menu)-1)
    elif menu == "4":
        print("주문을 종료합니다.")
        break
    else:
        print(f'{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.')

#print(f'{order_list}')
print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i]>0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")
print(f'총 금액은 {total_price}원')

