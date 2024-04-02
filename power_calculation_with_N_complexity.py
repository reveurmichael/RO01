def power(base, N):
    result = 1
    for i in range(N):
        result *= base
    return result

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