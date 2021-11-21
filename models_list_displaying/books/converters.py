from datetime import datetime


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value.__str__()