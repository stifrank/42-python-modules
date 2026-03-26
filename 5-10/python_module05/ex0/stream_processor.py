from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataProcessor(ABC):
    def __init__(self, processor_name: str) -> None:
        self.processor_name: str = processor_name
        self.last_result: Optional[str] = None
        self.metadata: Dict[str, Union[str, int, float]] = {}

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            total: Union[int, float] = sum(data)
            average: float = total / len(data)
            result: str = (
                f"Processed {len(data)} numeric values, "
                f"sum={total}, avg={average}"
            )
            self.last_result = result
            self.metadata = {
                "type": "numeric",
                "count": len(data),
                "sum": total,
                "avg": average,
            }
            return result
        except Exception:
            return "Invalid numeric data"

    def validate(self, data: Any) -> bool:
        return (
            isinstance(data, list)
            and len(data) > 0
            and all(isinstance(value, (int, float)) for value in data)
        )


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            characters: int = len(data)
            words: int = len(data.split())
            result: str = (
                f"Processed text: {characters} characters, {words} words"
            )
            self.last_result = result
            self.metadata = {
                "type": "text",
                "characters": characters,
                "words": words,
            }
            return result
        except Exception:
            return "Invalid text data"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Log Processor")

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            if data.startswith("ERROR:"):
                message: str = data.split("ERROR:", 1)[1].strip()
                result: str = (
                    f"[ALERT] ERROR level detected: {message}"
                )
            elif data.startswith("INFO:"):
                message = data.split("INFO:", 1)[1].strip()
                result = f"[INFO] INFO level detected: {message}"
            else:
                result = f"[LOG] Generic log entry: {data}"

            self.last_result = result
            self.metadata = {
                "type": "log",
                "length": len(data),
            }
            return result
        except Exception:
            return "Invalid log data"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0


def print_processor_demo(
    processor: DataProcessor,
    data: Any,
    validation_message: str
) -> None:
    print(f"Initializing {processor.processor_name}...")
    if isinstance(data, str):
        print(f'Processing data: "{data}"')
    else:
        print(f"Processing data: {data}")

    try:
        if processor.validate(data):
            print(f"Validation: {validation_message}")
        else:
            print("Validation: Invalid data")
    except Exception:
        print("Validation: Invalid data")

    result: str = processor.process(data)
    print(processor.format_output(result))


def polymorphic_demo(processors: List[DataProcessor]) -> None:
    sample_data: List[Any] = [
        [1, 2, 3],
        "Hello  Nexus",
        "INFO: System ready",
    ]

    print("Processing multiple data types through same interface...")
    for index, processor in enumerate(processors):
        result: str = processor.process(sample_data[index])
        print(f"Result {index + 1}: {result}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_processor: NumericProcessor = NumericProcessor()
    text_processor: TextProcessor = TextProcessor()
    log_processor: LogProcessor = LogProcessor()

    print_processor_demo(
        numeric_processor,
        [1, 2, 3, 4, 5],
        "Numeric data verified",
    )
    print_processor_demo(
        text_processor,
        "Hello Nexus World",
        "Text data verified",
    )
    print_processor_demo(
        log_processor,
        "ERROR: Connection timeout",
        "Log entry verified",
    )

    print("=== Polymorphic Processing Demo ===")
    processors: List[DataProcessor] = [
        numeric_processor,
        text_processor,
        log_processor,
    ]
    polymorphic_demo(processors)
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
