#!/usr/bin/env python3
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """
     Replaces the values of specified fields in a
     log message with a redaction string.
    """
    for field in fields:
        message = re.sub(
            f'{field}=[^ {separator}]+', f'{field}={redaction}', message
        )
    return message


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
