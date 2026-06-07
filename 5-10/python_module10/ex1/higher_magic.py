from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heals {target} with {power} power"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} with {power} defense"


def spell_combiner(
    spell1: Callable,
    spell2: Callable,
) -> Callable:
    def combined_spell(
        target: str,
        power: int,
    ) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power),
        )

    return combined_spell


def power_amplifier(
    base_spell: Callable,
    multiplier: int,
) -> Callable:
    def amplified_spell(
        target: str,
        power: int,
    ) -> str:
        return base_spell(
            target,
            power * multiplier,
        )

    return amplified_spell


def strong_enough(target: str, power: int) -> bool:
    return power >= 20


def conditional_caster(
    condition: Callable,
    spell: Callable,
) -> Callable:
    def conditional_spell(
        target: str,
        power: int,
    ) -> str:
        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return conditional_spell


def spell_sequence(
    spells: list[Callable],
) -> Callable:
    def sequence_spell(
        target: str,
        power: int,
    ) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence_spell


def main() -> None:
    target = "Dragon"
    power = 10
    mega_fireball = power_amplifier(
        fireball,
        3,
    )

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined(target, power)
    print(
        f"Combined spell result: "
        f"{combined_result[0]}, {combined_result[1]}"
    )

    print("\nTesting power amplifier...")
    print(
        f"Original: {power}, "
        f"Amplified: {power * 3}"
    )
    print(mega_fireball(target, power))

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(strong_enough, fireball)
    print(f"Strong fireball result: {safe_fireball(target, 25)}")
    print(f"Weak fireball result: {safe_fireball(target, 5)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    for result in sequence(target, power):
        print(result)


if __name__ == "__main__":
    main()
