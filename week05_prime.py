def is_prime(number : int) -> bool:
    #number : int -> bool은 권고사항이라 맞지 않아도 작동은 함
    #같은 개발자에대한 권고사항정도 넣을땐 int 나올땐 bool
    """
    function to determine whether number is prime


    :param number: 판정할 숫자
    :return: True if it is prime number else False
    """

    if number >= 2:
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                return False
            # print(i, end=" ")
    else:
        return False
    return True

n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1



for i in range(n1,n2+1):
    if is_prime(i):
        print(i,end=' ')


# n = int(input())
#
#
# if is_prime(n):
#     print(f'{n}는 소수입니다.')
# else:
#     print(f'{n}는 소수가 아닙니다.')