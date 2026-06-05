from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")

        if not self.has_commanding_officer():
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365 and not self.has_experienced_crew():
            raise ValueError(
                "Long missions need 50% experienced crew"
            )

        if not self.all_crew_active():
            raise ValueError("All crew members must be active")

        return self

    def has_commanding_officer(self) -> bool:
        for member in self.crew:
            if member.rank in (Rank.commander, Rank.captain):
                return True

        return False

    def has_experienced_crew(self) -> bool:
        experienced_count = 0

        for member in self.crew:
            if member.years_experience >= 5:
                experienced_count += 1

        return experienced_count * 2 >= len(self.crew)

    def all_crew_active(self) -> bool:
        for member in self.crew:
            if not member.is_active:
                return False

        return True


def show_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")

    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )


def clean_error_message(error: ValidationError) -> str:
    message = error.errors()[0]["msg"]

    if message.startswith("Value error, "):
        message = message.removeprefix("Value error, ")

    return message


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat(
            "2024-10-01T09:00:00"
        ),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.commander,
                age=42,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=29,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
    )

    print("Valid mission created:")
    show_mission(mission)

    print("\n=========================================")
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Invalid Mission",
            destination="Moon",
            launch_date=datetime.fromisoformat(
                "2024-01-15T10:30:00"
            ),
            duration_days=30,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Junior Cadet",
                    rank=Rank.cadet,
                    age=22,
                    specialization="Support",
                    years_experience=1,
                )
            ],
        )
    except ValidationError as error:
        print(clean_error_message(error))


if __name__ == "__main__":
    main()
