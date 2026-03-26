import random
import typing

print("=== Game Data Stream Processor ===")


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use",
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event


stream = gen_event()

i = 0
while i < 1000:
    event = next(stream)
    print(f"Event {i}: Player {event[0]} did action {event[1]}")
    i += 1

event_list = []
i = 0
while i < 10:
    event_list.append(next(stream))
    i += 1

print(f"Built list of 10 events: {event_list}")

for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
