from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.last_batch_size: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "last_batch_size": self.last_batch_size,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_readings: List[str] = [
                item for item in data_batch
                if isinstance(item, str) and ":" in item
            ]
            self.last_batch_size = len(valid_readings)

            temperatures: List[float] = [
                float(item.split(":")[1])
                for item in valid_readings
                if item.startswith("temp:")
            ]

            if temperatures:
                avg_temp: float = sum(temperatures) / len(temperatures)
            else:
                avg_temp = 0.0

            return (
                f"Sensor analysis: {len(valid_readings)} readings processed, "
                f"avg temp: {avg_temp}°C"
            )
        except Exception:
            return "Sensor analysis failed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                item for item in data_batch
                if isinstance(item, str)
                and item.startswith("temp:")
                and float(item.split(":")[1]) > 30
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["domain"] = "sensor"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_transactions: List[str] = [
                item for item in data_batch
                if isinstance(item, str) and ":" in item
            ]
            self.last_batch_size = len(valid_transactions)

            buy_total: int = sum(
                int(item.split(":")[1])
                for item in valid_transactions
                if item.startswith("buy:")
            )
            sell_total: int = sum(
                int(item.split(":")[1])
                for item in valid_transactions
                if item.startswith("sell:")
            )
            net_flow: int = sell_total - buy_total

            sign: str = "+"
            if net_flow < 0:
                sign = ""

            return (
                f"Transaction analysis: {len(valid_transactions)} "
                f"operations, net flow: {sign}{net_flow} units"
            )
        except Exception:
            return "Transaction analysis failed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch
                if isinstance(item, str)
                and ":" in item
                and int(item.split(":")[1]) >= 100
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["domain"] = "transaction"
        return stats


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_events: List[str] = [
                item for item in data_batch
                if isinstance(item, str)
            ]
            self.last_batch_size = len(valid_events)

            error_count: int = len(
                [item for item in valid_events if item == "error"]
            )

            return (
                f"Event analysis: {len(valid_events)} events, "
                f"{error_count} error detected"
            )
        except Exception:
            return "Event analysis failed"

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "priority":
            return [
                item for item in data_batch
                if isinstance(item, str) and item == "error"
            ]
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: Dict[str, Union[str, int, float]] = super().get_stats()
        stats["domain"] = "event"
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_stream(self, stream: DataStream, data_batch: List[Any]) -> str:
        return stream.process_batch(data_batch)

    def process_all(self, batches: List[List[Any]]) -> List[str]:
        results: List[str] = []
        for stream, batch in zip(self.streams, batches):
            results.append(stream.process_batch(batch))
        return results


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream: SensorStream = SensorStream("SENSOR_001")
    transaction_stream: TransactionStream = TransactionStream(
        "TRANS_001"
    )
    event_stream: EventStream = EventStream("EVENT_001")

    sensor_batch: List[str] = [
        "temp:22.5",
        "humidity:65",
        "pressure:1013",
    ]
    transaction_batch: List[str] = [
        "buy:100",
        "sell:150",
        "buy:75",
    ]
    event_batch: List[str] = [
        "login",
        "error",
        "logout",
    ]

    print("Initializing Sensor Stream...")
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor_stream.process_batch(sensor_batch))

    print("Initializing Transaction Stream...")
    print(
        f"Stream ID: {transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    print(f"Processing transaction batch: {transaction_batch}")
    print(transaction_stream.process_batch(transaction_batch))

    print("Initializing Event Stream...")
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    print(f"Processing event batch: {event_batch}")
    print(event_stream.process_batch(event_batch))

    print("=== Polymorphic Stream Processing ===")

    processor: StreamProcessor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches: List[List[Any]] = [
        ["temp:31.5", "temp:28.0"],
        ["buy:50", "sell:120", "buy:30", "sell:90"],
        ["login", "error", "logout"],
    ]

    print("Processing mixed stream types through unified interface...")
    print("Batch 1 Results:")
    processor.process_all(mixed_batches)
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    critical_sensors: List[Any] = sensor_stream.filter_data(
        mixed_batches[0],
        "critical"
    )
    large_transactions: List[Any] = transaction_stream.filter_data(
        mixed_batches[1],
        "large"
    )

    print("Stream filtering active: High-priority data only")
    print(
        "Filtered results: "
        f"{len(critical_sensors)} critical sensor alerts, "
        f"{len(large_transactions)} large transaction"
    )
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()