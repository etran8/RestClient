import httplib2
from urllib.parse import urlencode
import json
import jsonpickle
import pickle
from datetime import date
from sample.models import Customer, Account, Transaction

#from rest_framework_simplejwt.tokens import RefreshToken


def create_token():
    h = httplib2.Http()

    url = "http://localhost:8000/auth-jwt/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))


def createCustomer():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    url = "http://127.0.0.1:8000/listCustomerJSON/"

    # customer = Customer(first_name='Eric222', last_name='Tran222', ssn='999-99-9999',
    #                     preferred_customer='Y', street='123 Main Street',
    #                     city='Falls Church', state='Virginia', zip='22043')

    dict1 = {"first_name": "Eric", "last_name": "Tran", "ssn": "999-99-9999", "customer_since": "2024-04-25",
             "preferred_customer": "Y", "street": "123 Main Street",  "city": "Falls Church",
             "state": "Virginia", "zip": "22043"}

    customer = Customer(dict1)
    customer_json = customer.toJSON()
    print('This is customer JSON: ', customer_json)
    body = customer_json

    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method="POST", body=body, headers=headers)
    print('createCustomer Status:', resp.status)
    print('createCustomer Content:', content.decode('utf-8'))


def getCustomers():
    h = httplib2.Http(".cache")

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}
    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)

    url = "http://127.0.0.1:8000/listCustomerJSON/"
    resp, content = h.request(uri=url, method="GET", headers=headers)

    print('This is getCustomers response status', resp.status)
    str_content = content.decode('utf-8')
    print('This is getCustomers String content', str_content)
    customer_list = json.loads(str_content)
    print('This is customer list: ', customer_list)


def createAccount():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}
    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))

    mytoken = content.decode('utf-8')
    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    dict1 = {"account_number": "999", "account_type": "S", "paper_statement": "N",
             "password": "Test999", "balance": "1000.00", "agreement": "Testing999", "customer": "22"}

    account = Account(dict1)
    account_json = account.toJSON()
    print('This is Account JSON', account_json)
    body = account_json

    print('This is the customer account created for:', account.customer)

    url = "http://localhost:8000/listAccountJSON/22"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method='POST', body=body, headers=headers)
    print('This is createAccount Status:', resp.status)
    print('This is createAccount Content:', content.decode('utf-8'))
    json_object = json.loads(content.decode('utf-8'))
    print('This is the Account created for customer 23: ', json_object)


def updateCustomer():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')

    print('This is updateCustomer Getting token response status', resp.status)
    print('This is updateCustomer Getting token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    url = "http://localhost:8000/updateCustomerJSON/22"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method="GET", headers=headers)
    print('This is before update GET response status', resp.status)
    str_content = content.decode('utf-8')
    print('This is before update customer:', str_content)
    customer = json.loads(str_content)
    print('This is customer: ', customer)

    # dict1 = {'id': '24', 'first_name': 'Eric', 'last_name': 'Tran', 'ssn': '999-99-9999', 'customer_since': '2024-04-25',
    #          'preferred_customer': 'Y', 'street': '123 Main Street', 'city': 'Falls Church', 'state': 'VA', 'zip': '22043'}
    # customer_obj = Customer(dict1)

    customer_obj = Customer(customer)
    print('Customer Last Name before update: ', customer_obj.last_name)

    customer_obj.last_name = 'Sir ' + customer_obj.last_name
    print('This is updated customer last name: ', customer_obj.last_name)

    customer_json = customer_obj.toJSON()
    print('This is customer JSON', customer_json)
    body = customer_json

    # Run an update.
    url = "http://localhost:8000/updateCustomerJSON/22"
    print('This is the updating Header: ', headers)
    print('This is the updating body: ', body)
    resp, content = h.request(uri=url, method='PUT', body=body, headers=headers)
    print('This is updated response status:', resp.status)
    print('This is updated customer:', content.decode('utf-8'))


def updateAccount():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')

    print('This is updateAccount Getting token response status', resp.status)
    print('This is updateAccount Getting token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method="GET", headers=headers)
    print('This is before update GET response status', resp.status)
    str_content = content.decode('utf-8')
    print('This is before update Account:', str_content)
    account = json.loads(str_content)
    print('This is Account: ', account)

    account_obj = Account(account)
    print('Account balance before update: ', account_obj.balance)

    account_obj.balance = 1000000.00
    print('This is updated Account balance: ', account_obj.balance)

    account_json = account_obj.toJSON()
    print('This is Account JSON', account_json)
    body = account_json

    # Run an update.
    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    print('This is the updating Header: ', headers)
    print('This is the updating body: ', body)
    resp, content = h.request(uri=url, method='PUT', body=body, headers=headers)
    print('This is updated response status:', resp.status)
    print('This is updated Account:', content.decode('utf-8'))


def createCrTransaction():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    # transaction = Transaction(transaction_type='C', transaction_amount='100.00', initiated_date='04/25/2024',
    #                           posted_date='04/25/2024', status='C', account_id='26')
    #transaction_obj = Transaction(transaction)

    dict1 = {"transaction_type": "C", "transaction_amount": 200.00, "initiated_date": "2024-04-25",
             "posted_date": "2024-04-25", "status": "C", "account": 26}
    transaction_obj = Transaction(dict1)

    transaction_json = transaction_obj.toJSON()
    print('This is Transaction JSON', transaction_json)
    body = transaction_json

    url = "http://127.0.0.1:8000/CreateCrTransactionJSON/26"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method='POST', body=body, headers=headers)
    print('This is createCrTransaction Status:', resp.status)
    print('This is createCrTransaction Content:', content.decode('utf-8'))

    #Updating account Balance
    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    resp, content = h.request(uri=url, method="GET", headers=headers)
    str_content = content.decode('utf-8')
    account = json.loads(str_content)
    account_obj = Account(account)
    print('Account balance before update: ', account_obj.balance)
    account_obj.balance = account_obj.balance + 200.00
    print('This is updated Account balance: ', account_obj.balance)

    account_json = account_obj.toJSON()
    print('This is Account JSON', account_json)
    body = account_json

    # Run an update.
    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    resp, content = h.request(uri=url, method='PUT', body=body, headers=headers)
    print('This is updated Account:', content.decode('utf-8'))


def createDbTransaction():
    h = httplib2.Http()

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}

    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')
    print('This is create_token response status', resp.status)
    print('This is create_token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    dict1 = {"transaction_type": "D", "transaction_amount": 300.00, "initiated_date": "2024-04-25",
             "posted_date": "2024-04-25", "status": "C", "account": 26}
    transaction_obj = Transaction(dict1)

    transaction_json = transaction_obj.toJSON()
    print('This is Transaction JSON', transaction_json)
    body = transaction_json

    url = "http://127.0.0.1:8000/CreateDbTransactionJSON/26"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)
    resp, content = h.request(uri=url, method='POST', body=body, headers=headers)
    print('This is createCrTransaction Status:', resp.status)
    print('This is createCrTransaction Content:', content.decode('utf-8'))

    #Updating account Balance
    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    resp, content = h.request(uri=url, method="GET", headers=headers)
    str_content = content.decode('utf-8')
    account = json.loads(str_content)

    account_obj = Account(account)
    print('Account balance before update: ', account_obj.balance)
    account_obj.balance = account_obj.balance - 300.00
    print('This is updated Account balance: ', account_obj.balance)

    account_json = account_obj.toJSON()
    print('This is Account JSON', account_json)
    body = account_json

    # Run an update.
    url = "http://127.0.0.1:8000/updateAccountJSON/26"
    resp, content = h.request(uri=url, method='PUT', body=body, headers=headers)
    print('This is updated Account:', content.decode('utf-8'))

def retrieveTransaction():
    h = httplib2.Http(".cache")

    url = "http://localhost:8000/api/token/"
    headers = {"content-type": "application/json"}
    body = {"username": "eric", "password": "eric"}
    resp, content = h.request(uri=url, method="POST", body=json.dumps(body), headers=headers)
    mytoken = content.decode('utf-8')
    print('This is access token response status', resp.status)
    print('This is access token content', content.decode('utf-8'))

    temp = mytoken.partition("access")[2]
    temp = temp[3:]
    mytoken = temp[:-2]
    print('This is my access token: ', mytoken)

    headers = {"content-type": "application/json", 'Authorization': 'Bearer ' + mytoken}
    print('This is the Header: ', headers)

    url = "http://127.0.0.1:8000/listTransactionJSON/26"
    resp, content = h.request(uri=url, method="GET", headers=headers)
    print('This is Transaction response status', resp.status)
    str_content = content.decode('utf-8')
    print('This is Transaction String content', str_content)
    transaction_list = json.loads(str_content)
    acct_id = transaction_list[0]['account']
    print('Transactions for the Account ID: ', acct_id)
    print(transaction_list)


if __name__ == '__main__':
    create_token()
    createCustomer()
    getCustomers()
    createAccount()
    updateCustomer()
    updateAccount()
    createCrTransaction()
    createDbTransaction()
    retrieveTransaction()

