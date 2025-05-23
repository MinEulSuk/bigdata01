import datetime,sqlite3
prices = [2000,2500,4000,4200]
drinks = ['아이스 아메리카노','카페 라떼','수박 주스','딸기 주스']
amounts = [0] * len(drinks)
total_price = 0

#할인 적용 정책
DISCOUNT_THRESHOLD = 10000 # 할인이 적용되는 임계값
DISCOUNT_RATE = 0.05 #할인율

#cafe.db에 menu 테이블 insert
conn = sqlite3.connect('cafe.db')
cur = conn.cursor()
cur.execute('''
    create table if not exists menu (
    id integer primary key autoincrement,
    drinks string unique,
    prices integer not null,
    amounts integer)
''')
cur.executemany('insert or ignore into menu(drinks,prices) values(?,?)', zip(drinks, prices))
#unique or ignore은 sqlite3에만 있는 방법
conn.commit()
# run함수랑 연동해서 amounts양 늘려보기

def run() -> None:
    """
    키오스크 실행(구동)함수


    :return: None
    """

    while True:
        try:
            menu = int(input(display_menu()))
            if 1 <= menu <= len(drinks):
                order_process(menu-1)
            elif menu == len(drinks)+1:
                print("주문을 종료합니다.")
                break
            else:
                print(f'{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.')
        except ValueError:
            print(f"문자를 입력할 수 없습니다.. 숫자를 입력해주세요.")

def apply_discount(price : int) -> float:
    """
    총 금액이 특정 금액(임계값)을 넘어서면 할인율 적용 함수
    :param price: 총 금액
    :return: 할인된 금액 또는 할인이 적용되지 않은 금액
    """

    if price >= DISCOUNT_THRESHOLD:
        return price * (1-DISCOUNT_RATE)
    return price

def print_ticket_number() -> None:
    """
    주문 번호표 출력 기능 함수
    :return: None
    """

    cur.execute('''
        create table if not exists ticket (
        id integer primary key autoincrement,
        number integer not null,
        ordertime string)
    ''')

    cur.execute('select number from ticket order by number desc')
    result = cur.fetchone()
    if result is None:
        number = 1
    else:
        number = result[0]+1
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 시간 변수 생성
    cur.execute('insert into ticket(number,ordertime) values(?,?)',(number,current_time))
    conn.commit()  # 확정하는 것
    print(f'번호표 : {number} {current_time}')
    conn.close()  # free db instance 인스턴스 해제
    # datetime을 db에 넣는 방식으로 해결하는 거 , 브랜치를 활용해서 교수님 버전, db 버전으로 나누기

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

    discounted_price = apply_discount(total_price)
    discount = total_price - discounted_price



    if discount > 0:
        print(f'할인 금액 : {discount}원 ({DISCOUNT_RATE*100}% 할인)\n'
              f'할인 적용 후 지불하실 총 금액 : {discounted_price}원 입니다.')
    else:
        print(f'할인이 적용되지 않았습니다.\n지불하실 총 금액은 {total_price}원 입니다.')


def test() -> None:
    """
    앞으로 키오스크에 추가할 기능
    :return:
    """
    pass

