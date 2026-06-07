def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
        map(
            lambda spell: f"* {spell} *",
            spells
        )
    )


def mage_stats(mages: list[dict]) -> dict:
    strongest_mage = max(
        mages,
        key=lambda mage: mage["power"]
    )
    weakest_mage = min(
        mages,
        key=lambda mage: mage["power"]
    )
    average_power = round(
        sum(map(lambda mage: mage["power"], mages)) / len(mages),
        2
    )

    return {
        "max_power": strongest_mage["power"],
        "min_power": weakest_mage["power"],
        "avg_power": average_power,
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "arcane"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Shadow Dagger", "power": 67, "type": "dark"},
    ]

    mages = [
        {"name": "Merlin", "power": 95, "element": "arcane"},
        {"name": "Gandalf", "power": 88, "element": "light"},
        {"name": "Rincewind", "power": 42, "element": "chaos"},
    ]

    spells = [
        "fireball",
        "heal",
        "shield",
    ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    print(power_filter(mages, 80))

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
