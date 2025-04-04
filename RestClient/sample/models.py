# Create your models here.
import json
from datetime import date
from sample import CustomEncoder
import inspect


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Customer) or isinstance(obj, Account) or isinstance(obj, Transaction):
            return obj.toJSON()
        else:
            return json.JSONEncoder.default(self, obj)


class Status():
    id = ""
    status = ""
    key = ""

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def __str__(self):
        return self.status + " - " + self.key


class Account():
    STATE_CHOICES = [
            ('VA', 'Virginia'),
            ('MD', 'Maryland'),
            ('DC', 'District of Columbia'),
            ('DE', 'Delaware'),
    ]
    account_number = ""
    account_type = ""
    paper_statement = ""
    password = ""
    balance = ""
    agreement = ""
    customer = ""

    def __init__(self, account_number, account_type, paper_statement, password, balance, agreement, customer_id):
        self.account_number = account_number
        self.account_type = account_type
        self.paper_statement = paper_statement
        self.password = password
        self.balance = balance
        self.agreement = agreement
        self.customer = customer_id

    def __str__(self):
        return self.account_number

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class Customer():
    first_name = ""
    last_name = ""
    ssn = ""
    customer_since = ""
    preferred_customer = ""
    street = ""
    city = ""
    state = ""
    zip = ""

    def __init__(self, first_name, last_name, ssn, customer_since, preferred_customer, street, city, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn
        self.customer_since = customer_since
        self.preferred_customer = preferred_customer
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return self.first_name + " - " + self.last_name

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class Transaction():
    transaction_type = ""
    transaction_amount = ""
    initiated_date = ""
    posted_date = ""
    status = ""
    account = ""

    def __init__(self, transaction_type, transaction_amount, initiated_date, posted_date, status, account):
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.initiated_date = initiated_date
        self.posted_date = posted_date
        self.status = status
        self.account = account

    def __str__(self):
        return str(self.account_id)

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


