import math
limit = 1000000
num = 0
maxlength = 0


def inpower(num):
    n = 2
    pow = 1
    while n < num:
        pow += 1
        n = math.pow(n , pow)
    if n == num:
        return True
    return False


def power(num):
    n = 2
    return math.log(num, n)


def collatzlength(num):
    count = 1
    while (num != 1.0):
        if num % 2 == 0:
            if inpower(num):
                num = power(num)
                count += num
                break
            num /= 2
        else:
            num *= 3
            num += 1
        count += 1
    return count


for i in range(1, limit):
    len = collatzlength(i)
    if len > maxlength:
        maxlength = len
        num = i
        print(num,maxlength)
