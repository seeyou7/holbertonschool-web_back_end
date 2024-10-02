#!/usr/bin/env python3
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns the obfuscated log message."""
    pattern = f'({"|".join(fields)})=([^${separator}]+)'
    return re.sub(pattern, rf'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list):
        """Constructor that accepts fields to be redacted."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filter sensitive information from log records."""
        original_message = super().format(record)
        # Get the original log message
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
