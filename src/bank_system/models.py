from dataclasses import asdict, dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class BankAccount:
    account_number: str
    client: str
    balance: float
    operation: str
    amount: float

    def to_dict(self) -> dict[str, object]:
        return asdict(self)

@dataclass(frozen=True, slots=True)
class ProcessingConfig:
    minimum_balance: float
    skip_invalid: bool

@dataclass(frozen=True, slots=True)
class LoggingConfig:
    level: str
    path: Path

@dataclass(frozen=True, slots=True)
class AppConfig:
    input_path: Path
    output_path: Path
    processing: ProcessingConfig
    logging: LoggingConfig