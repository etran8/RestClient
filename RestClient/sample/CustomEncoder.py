import json
import inspect
from models import Customer, Account, Transaction


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Customer) or isinstance(obj, Account) or isinstance(obj, Transaction):
            return obj.toJSON()
        else:
            return json.JSONEncoder.default(self, obj)
