def is_happy(n: int) -> bool:
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1

print(is_happy(19))
print(is_happy(567))
