"""
time transfer module
make a util to transfer time format
"""

import json
from datetime import datetime


class TimeTransfer:

    @classmethod
    def str_to_datetime(cls, str_time: str, format: str) -> datetime:
        """str time to datetime

        :param str_time: string time, example: "2021-01-01 12:00:00"
        :param format: string format, example: "%Y-%m-%d %H:%M:%S"
        :return: datetime object, example: datetime(2021, 1, 1, 12, 0, 0)
        """
        try:
            return datetime.strptime(str_time, format)
        except ValueError as e:
            raise ValueError(f"incorrect data format, {e}")

    @classmethod
    def datetime_to_str(cls, date_time: datetime, format: str) -> str:
        """datetime to str time

        :param date_time: datetime object, example: datetime(2021, 1, 1, 12, 0, 0)
        :param format: string format, example: "%Y-%m-%d %H:%M:%S"
        :return: string time, example: "2021-01-01 12:00:00"
        """
        try:
            return date_time.strftime(format)
        except ValueError as e:
            raise ValueError(f"incorrect data format, {e}")
        except TypeError as e:
            raise TypeError(f"incorrect data type, {e}")

    @classmethod
    def str_to_timestamp(cls, str_time: str) -> int:
        """str time to timestamp

        :param str_time: string time, example: "2021-01-01 12:00:00"
        :return: timestamp
        """
        supported_formats = [
            "%Y-%m-%d",
            "%Y-%m-%d %H",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M:%S.%f",
            "%Y/%m/%d",
            "%Y/%m/%d %H",
            "%Y/%m/%d %H:%M",
            "%Y/%m/%d %H:%M:%S",
            "%Y/%m/%d %H:%M:%S.%f",
        ]
        for format in supported_formats:
            try:
                time_obj = cls.str_to_datetime(str_time, format)
            except ValueError:
                continue
            else:
                return int(time_obj.timestamp())
        # 如果不符合预期格式，抛出异常
        raise ValueError(f"incorrect data format, supported formats: {json.dumps(supported_formats)}")
