def is_prime(number):
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


n = int(input())


if is_prime(n):
    print(f'{n}는 소수입니다.')
else:
    print(f'{n}는 소수가 아닙니다.')