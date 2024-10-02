#!/usr/bin/python3
import re


def filter_datum(fields, redaction, meassage, separator):
    """Returns the obfuscated log message."""
    pattern = r'(' + '|'.join(fields) + r')=([^' + separator + r']*)'
    return re.sub(pattern, r'\1=' + redaction, meassage)
