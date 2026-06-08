from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
import operator
from typing import Any


def enchant(
    power: int,
    element: str,
    target: str,
) -> str:
    return (
        f"{element} enchantment "
        f"of {power} power "
        f"cast on {target}"
    )


def spell_reducer(
    spells: list[int],
    operation: str,
) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(
            f"Unknown operation: {operation}"
        )

    return reduce(
        operations[operation],
        spells,
    )


def partial_enchanter(
    base_enchantment: Callable,
) -> dict[str, Callable]:
    fire = partial(
        base_enchantment,
        50,
        "Fire",
    )

    ice = partial(
        base_enchantment,
        50,
        "Ice",
    )

    lightning = partial(
        base_enchantment,
        50,
        "Lightning",
    )

    return {
        "fire": fire,
        "ice": ice,
        "lightning": lightning,
    }


@lru_cache
def memoized_fibonacci(
    n: int,
) -> int:
    if n < 2:
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


@singledispatch
def spell_dispatcher(
    spell: Any,
) -> str:
    return "Unknown spell type"


@spell_dispatcher.register
def _(
    spell: int,
) -> str:
    return (
        f"Damage spell: "
        f"{spell} damage"
    )


@spell_dispatcher.register
def _(
    spell: str,
) -> str:
    return (
        f"Enchantment: "
        f"{spell}"
    )


@spell_dispatcher.register
def _(
    spell: list,
) -> str:
    return (
        f"Multi-cast: "
        f"{len(spell)} spells"
    )


def main() -> None:

    print("Testing spell reducer...")
    spell_powers = [10, 20, 30, 40]
    print(
        f"Sum: "
        f"{spell_reducer(spell_powers, 'add')}"
    )
    print(
        f"Product: "
        f"{spell_reducer(spell_powers, 'multiply')}"
    )
    print(
        f"Max: "
        f"{spell_reducer(spell_powers, 'max')}"
    )
    print(
        f"Min: "
        f"{spell_reducer(spell_powers, 'min')}"
    )

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(
        enchant,
    )
    print(
        enchantments["fire"](
            "Dragon",
        )
    )
    print(
        enchantments["ice"](
            "Goblin",
        )
    )
    print(
        enchantments["lightning"](
            "Troll",
        )
    )

    print("\nTesting memoized fibonacci...")
    print(
        f"Fib(0): "
        f"{memoized_fibonacci(0)}"
    )
    print(
        f"Fib(1): "
        f"{memoized_fibonacci(1)}"
    )
    print(
        f"Fib(10): "
        f"{memoized_fibonacci(10)}"
    )
    print(
        f"Fib(15): "
        f"{memoized_fibonacci(15)}"
    )

    print("\nTesting spell dispatcher...")
    print(
        spell_dispatcher(42)
    )
    print(
        spell_dispatcher("fireball")
    )
    print(
        spell_dispatcher(
            ["fireball", "heal", "shield"]
        )
    )
    print(
        spell_dispatcher(
            {"fireball": 1}
        )
    )


if __name__ == "__main__":
    main()
