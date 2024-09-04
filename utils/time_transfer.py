"""
time transfer module
make a util to transfer time format
"""
from datetime import datetime


class TimeTransfer:
    
    @classmethod
    def str_to_datetime(cls, str_time: str, format: str) -> datetime:
        """str time to datetime"""
        try:
            return datetime.strptime(str_time, format)
        except ValueError as e:
            raise ValueError(f"incorrect data format, {e}")
