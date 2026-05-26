from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)
from ex1 import HealingCreatureFactory, TransformCreatureFactory


Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(first: Opponent, second: Opponent) -> None:
    first_factory, first_strategy = first
    second_factory, second_strategy = second

    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print("* Battle *")
    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" now fight!")

    for action in first_strategy.act(first_creature):
        print(action)

    for action in second_strategy.act(second_creature):
        print(action)
    print()


def tournament(opponents: list[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    try:
        for first_index in range(len(opponents)):
            for second_index in range(first_index + 1, len(opponents)):
                battle(opponents[first_index], opponents[second_index])
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")
        print()


def main() -> None:
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), normal),
        (HealingCreatureFactory(), defensive),
    ])

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    tournament([
        (FlameFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
    ])

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    tournament([
        (AquaFactory(), normal),
        (HealingCreatureFactory(), defensive),
        (TransformCreatureFactory(), aggressive),
    ])


if __name__ == "__main__":
    main()
