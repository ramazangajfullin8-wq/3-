def parity(n):
    return "Чётное" if n % 2 == 0 else "Нечётное"

cases = [(-3, "Нечётное"), (0, "Чётное"), (7, "Нечётное"), (12, "Чётное")]
for n, expected in cases:
    actual = parity(n)
    assert actual == expected
    print(f"n = {n:3}: {actual} — верно")
print("Проверки: 4 из 4 выполнены успешно")
