from collections.abc import Callable
from functools import wraps
import time


def spell_timer(
    func: Callable[[], str],
) -> Callable[[], str]:
    @wraps(func)
    def wrapper() -> str:
        print(f"Casting {func.__name__}...")

        start_time = time.time()
        result = func()
        end_time = time.time()

        print(f"Spell completed in {end_time - start_time:.3f} seconds")

        return result

    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.1)

    return "Fireball cast!"


def power_validator(
    min_power: int,
) -> Callable:
    def decorator(
        func: Callable,
    ) -> Callable:
        @wraps(func)
        def wrapper(
            *args: object,
            **kwargs: object,
        ) -> str:
            power = args[-1]

            if not isinstance(power, int):
                return "Insufficient power for this spell"

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


@power_validator(10)
def lightning(
    spell_name: str,
    power: int,
) -> str:
    return (
        f"Successfully cast {spell_name} "
        f"with {power} power"
    )


def retry_spell(
    max_attempts: int,
) -> Callable:
    def decorator(
        func: Callable[[], str],
    ) -> Callable[[], str]:
        @wraps(func)
        def wrapper() -> str:
            for attempt in range(
                1,
                max_attempts + 1,
            ):
                try:
                    return func()

                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return (
                f"Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


@retry_spell(3)
def failed_spell() -> str:
    raise ValueError("Spell failed")


@retry_spell(3)
def waaaagh() -> str:
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(
                char.isalpha() or char == " "
                for char in name
            )
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int,
    ) -> str:
        return (
            f"Successfully cast {spell_name} "
            f"with {power} power"
        )


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")
    print(lightning("Fireball", 15))
    print(lightning("Fireball", 5))

    print("\nTesting retrying spell...")
    print(failed_spell())
    print(waaaagh())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("X1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
