from typing import Generator

print("=== Game Data Stream Processor ===")


def game_event_stream(n: int) -> Generator[str, None, None]:
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


def fibonacci_stream() -> Generator[int, None, None]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_stream() -> Generator[int, None, None]:
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


total = 1000
print(f"Processing {total} game events...")

events = game_event_stream(total)
it = iter(events)

first_event = next(it)
second_event = next(it)
third_event = next(it)

print("Event 1:", first_event)
print("Event 2:", second_event)
print("Event 3:", third_event)
print("...")

total_processed = 3
high_level = 0
treasure_events = 0
level_up_events = 0

first_three = (first_event, second_event, third_event)

for event in first_three:
    if "(level 12)" in event:
        high_level += 1
    if "found treasure" in event:
        treasure_events += 1
    if "leveled up" in event:
        level_up_events += 1

for event in it:
    total_processed += 1
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

fib = fibonacci_stream()
fib_first_10 = []
i = 0
while i < 10:
    fib_first_10.append(str(next(fib)))
    i += 1
print("Fibonacci sequence (first 10): " + ", ".join(fib_first_10))

primes = prime_stream()
prime_first_5 = []
i = 0
while i < 5:
    prime_first_5.append(str(next(primes)))
    i += 1
print("Prime numbers (first 5): " + ", ".join(prime_first_5))
