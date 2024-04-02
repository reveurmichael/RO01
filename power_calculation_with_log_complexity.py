def power(base, N):
    if N == 0:
        return 1
    elif N % 2 == 0:
        # If N is even, reduce the problem size by halving the N
        half_power = power(base, N // 2)
        return half_power * half_power
    else:
        # If N is odd, reduce the problem size by subtracting one from N
        reduced_power = power(base, N - 1)
        return base * reduced_power

def run_1():
    base_num = 3
    exp_num = 3
    result = power(base_num, exp_num)
    print(f"{base_num} raised to the power of {exp_num} is {result}")


def run_2():
    import time
    start = time.time()
    result = power(1, 999999999)
    end = time.time()
    print("The calculation took ", end - start, " seconds")


run_2()
