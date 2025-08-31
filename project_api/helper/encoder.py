from datetime import date, datetime
from typing import Any

from flask.json.provider import DefaultJSONProvider
from sqlalchemy.orm.dynamic import AppenderQuery


class CustomJSONProvider(DefaultJSONProvider):
    def default(self, obj: Any) -> Any:
        if hasattr(obj, "to_dict") and callable(obj.to_dict):
            return obj.to_dict()
        if isinstance(obj, AppenderQuery):
            return [o.to_dict() for o in obj]
        if isinstance(obj, datetime | date):
            return str(obj)
        return super().default(obj)
