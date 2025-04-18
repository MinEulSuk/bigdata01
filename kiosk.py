prices = [2000,2500,4000,4200]
drinks = ['아이스 아메리카노','카페 라떼','수박 주스','딸기 주스']
amounts = [0] * len(drinks)
total_price = 0

def order_process(idx: int) -> None:
    # : int -> (리턴타입)None 로 타입힌트를 줄 수 있음 주석같은 의미
    """
    주문 처리 함수 1) 주문 디스플레이 기능 2)총 주문 금액 누산 3) 수량 업데이트
    :param idx : 고객이 선택한 메뉴 -1
    :return: 없음
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {prices[idx]}원 입니다.")
    total_price += prices[idx]
    amounts[idx] += 1

def display_menu() -> str:
    """
    음료 선택 메뉴 디스플레이 기능
    :return: 음료 메뉴 및 주문 종료 문자열
    """
    print('='*30)
    menu_text = "".join([f'{j + 1}) {drinks[j]} {prices[j]}원\n' for j in range(len(drinks))])
    menu_text += f'{len(drinks) + 1}) 주문 종료 : '

    return menu_text

def print_receipt() -> None:
    """
    영수증 출력 기능
    :return: 없음
    """
    print(f"{'상품명':^20} {'단가': ^6} {'수량': ^6} {'금액': ^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i] : ^20} {prices[i] : ^6} {amounts[i] : ^6} {prices[i] * amounts[i] : ^6}")
    print(f'총 금액은 {total_price}원')