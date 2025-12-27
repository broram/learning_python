def is_prime(dprim):
    prima = True
    for i in range(2, dprim):
        if (dprim % i == 0):
            prima = False
            break
    return prima

def result_prim(dprim):
    if is_prime(dprim):
        return f"{dprim} adalah bilangan prima"
    else:
        return f"{dprim} adalah bukan bilangan prima"   