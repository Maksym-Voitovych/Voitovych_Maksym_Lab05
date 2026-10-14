from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
import logging

from bank_system.exceptions import RecordValidationError
from bank_system.models import BankAccount
from bank_system.readers import read_csv_rows
from bank_system.validators import parse_bank_account

logger = logging.getLogger(__name__)

@dataclass
class ImportStatistics:
    total: int = 0
    valid: int = 0
    invalid: int = 0

def import_accounts(
    path: Path,
    *,
    skip_invalid: bool,
    statistics: ImportStatistics,
) -> Iterator[BankAccount]:
    for line_number, row in read_csv_rows(path):
        statistics.total += 1
        try:
            account = parse_bank_account(row, line_number=line_number)
        except RecordValidationError as error:
            statistics.invalid += 1
            logger.warning("Invalid record at line %s: %s", error.line_number, error)
            if skip_invalid:
                continue
            raise
        statistics.valid += 1
        yield account