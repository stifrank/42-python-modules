print("=== Game Data Stream Processor ===")


def game_event_stream(n):
    players = ("alice", "bob", "charlie")
    levels = (5, 12, 8)
    actions = ("killed monster", "found treasure", "leveled up")

    i = 0
    while i < n:
        idx = i % 3
        player = players[idx]
        level = levels[idx]
        action = actions[idx]
        yield f"Player {player} (level {level}) {action}"
        i += 1


def fibonacci_stream():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream():
    n = 2
    while True:
        is_prime = True
        d = 2
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            yield n
        n += 1


# 1) Procesar eventos en streaming
total = 1000
print(f"Processing {total} game events...")

events = game_event_stream(total)

# demo rápida de next()/iter()
it = iter(events)
print("Event 1:", next(it))
print("Event 2:", next(it))
print("Event 3:", next(it))
print("...")

# contadores (ya hemos consumido 3 eventos)
total_processed = 3
high_level = 0
treasure_events = 0
level_up_events = 0

# contar los 3 primeros impresos
first_three = (
    "Player alice (level 5) killed monster",
    "Player bob (level 12) found treasure",
    "Player charlie (level 8) leveled up",
)
for e in first_three:
    if "(level 12)" in e:
        high_level += 1
    if "found treasure" in e:
        treasure_events += 1
    if "leveled up" in e:
        level_up_events += 1

# seguir con el resto del stream (it sigue desde el 4º)
for event in it:
    total_processed += 1

    # nivel alto (10+). Como no usamos parseos avanzados, chequeamos los casos del patrón.
    if "(level 12)" in event:
        high_level += 1

    if "found treasure" in event:
        treasure_events += 1

    if "leveled up" in event:
        level_up_events += 1

print("=== Stream Analytics ===")
print(f"Total events processed: {total_processed}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}")
print("Memory usage: Constant (streaming)")

print("=== Generator Demonstration ===")

# 2) Fibonacci (primeros 10)
fib = fibonacci_stream()
fib_first_10 = []
i = 0
while i < 10:
    fib_first_10.append(str(next(fib)))
    i += 1
print("Fibonacci sequence (first 10): " + ", ".join(fib_first_10))

# 3) Primos (primeros 5)
pr = prime_stream()
prime_first_5 = []
i = 0
while i < 5:
    prime_first_5.append(str(next(pr)))
    i += 1
print("Prime numbers (first 5): " + ", ".join(prime_first_5))
