#!/usr/bin/env python3
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the obfuscated log message."""
    pattern = f'({"|".join(fields)})=([^${separator}]+)'
    return re.sub(pattern, rf'\1={redaction}', message)
