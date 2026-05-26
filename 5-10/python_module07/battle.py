from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle(
    first_factory: CreatureFactory,
    second_factory: CreatureFactory,
) -> None:
    first_creature = first_factory.create_base()
    second_creature = second_factory.create_base()

    print("Testing battle")
    print(first_creature.describe())
    print(" vs.")
    print(second_creature.describe())
    print(" fight!")
    print(first_creature.attack())
    print(second_creature.attack())
    print()


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
