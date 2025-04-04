# RestClient
This application implements a REST client to test REST Service end points.

This application creates RESTFul APIs using the same model objects indicated in the CustAcctMgmtProject project. These APIs will allow user to list and create a Customer, an Account, and a Transaction. Be able to load a customer, an Account and update it as needed.

This application also includes a REST client to test REST Service end points.

To run or test this application, do the following: 

	1. Load both the CustAcctMgmtProject project that includes the RESTFul Web Service and the RestClient project to PyCharm. 
 
	2. In PyCharm's Terminal, type "python manage.py runserver" at the root of the CustAcctMgmtProject project. If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/home
 
	3. Now Right click on the RestClient.py and select "Run RestClient".
 
	4. The output below will show that each of the RestFul Web Service APIs are successfully executed and the output for each API is displayed.
 
	
This creates a Customer.  
This is customer JSON:  {
    "first_name": "Eric",
    "last_name": "Tran",
    "ssn": "999-99-9999",
    "customer_since": "2024-04-25",
    "preferred_customer": "Y",
    "street": "123 Main Street",
    "city": "Falls Church",
    "state": "Virginia",
    "zip": "22043"
}
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
createCustomer Status: 200
createCustomer Content: {"Success":"Customer '{'id': 24, 'first_name': 'Eric', 'last_name': 'Tran', 'ssn': '999-99-9999', 'customer_since': '2024-04-25', 'preferred_customer': 'Y', 'street': '123 Main Street', 'city': 'Falls Church', 'state': 'Virginia', 'zip': '22043'}' created successfully"}
This is create_token response status 404

---

This gets all Customers.  
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is getCustomers response status 200
This is getCustomers String content [{"id":24,"first_name":"Eric","last_name":"Tran","ssn":"999-99-9999","customer_since":"2024-04-25","preferred_customer":"Y","street":"123 Main Street","city":"Falls Church","state":"Virginia","zip":"22043"},{"id":23,"first_name":"Janes","last_name":"Williams","ssn":"222-22-2222","customer_since":"2024-02-01","preferred_customer":"Y","street":"222 Second Street","city":"Arlington","state":"PA","zip":"22222"},{"id":22,"first_name":"Joe","last_name":"Smith","ssn":"111-11-1111","customer_since":"2024-01-01","preferred_customer":"Y","street":"111 First Street","city":"Falls Church","state":"VA","zip":"22043"}]
This is customer list:  [{'id': 24, 'first_name': 'Eric', 'last_name': 'Tran', 'ssn': '999-99-9999', 'customer_since': '2024-04-25', 'preferred_customer': 'Y', 'street': '123 Main Street', 'city': 'Falls Church', 'state': 'Virginia', 'zip': '22043'}, {'id': 23, 'first_name': 'Janes', 'last_name': 'Williams', 'ssn': '222-22-2222', 'customer_since': '2024-02-01', 'preferred_customer': 'Y', 'street': '222 Second Street', 'city': 'Arlington', 'state': 'PA', 'zip': '22222'}, {'id': 22, 'first_name': 'Joe', 'last_name': 'Smith', 'ssn': '111-11-1111', 'customer_since': '2024-01-01', 'preferred_customer': 'Y', 'street': '111 First Street', 'city': 'Falls Church', 'state': 'VA', 'zip': '22043'}]
This is create_token response status 404

---

This creates an account for a customer.  
This is Account JSON {
    "account_number": "999",
    "account_type": "S",
    "paper_statement": "N",
    "password": "Test999",
    "balance": "1000.00",
    "agreement": "Testing999",
    "customer": "22"
}
This is the customer account created for: 22
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is createAccount Status: 200
This is createAccount Content: {"Success":"Account '{'id': 32, 'account_number': 999, 'account_type': 'S', 'paper_statement': False, 'password': 'Test999', 'balance': 1000.0, 'agreement': 'Testing999', 'customer': 22}' created successfully"}
This is the Account created for customer 23:  {'Success': "Account '{'id': 32, 'account_number': 999, 'account_type': 'S', 'paper_statement': False, 'password': 'Test999', 'balance': 1000.0, 'agreement': 'Testing999', 'customer': 22}' created successfully"}
This is updateCustomer Getting token response status 404

----------

This updates a customer. 
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is before update GET response status 200
This is before update customer: {"id":22,"first_name":"Joe","last_name":"Smith","ssn":"111-11-1111","customer_since":"2024-01-01","preferred_customer":"Y","street":"111 First Street","city":"Falls Church","state":"VA","zip":"22043"}
This is customer:  {'id': 22, 'first_name': 'Joe', 'last_name': 'Smith', 'ssn': '111-11-1111', 'customer_since': '2024-01-01', 'preferred_customer': 'Y', 'street': '111 First Street', 'city': 'Falls Church', 'state': 'VA', 'zip': '22043'}
Customer Last Name before update:  Smith
This is updated customer last name:  Sir Smith
This is customer JSON {
    "id": 22,
    "first_name": "Joe",
    "last_name": "Sir Smith",
    "ssn": "111-11-1111",
    "customer_since": "2024-01-01",
    "preferred_customer": "Y",
    "street": "111 First Street",
    "city": "Falls Church",
    "state": "VA",
    "zip": "22043"
}
This is the updating Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is the updating body:  {
    "id": 22,
    "first_name": "Joe",
    "last_name": "Sir Smith",
    "ssn": "111-11-1111",
    "customer_since": "2024-01-01",
    "preferred_customer": "Y",
    "street": "111 First Street",
    "city": "Falls Church",
    "state": "VA",
    "zip": "22043"
}
This is updated response status: 200
This is updated customer: {"Success":"Customer '{'id': 22, 'first_name': 'Joe', 'last_name': 'Sir Smith', 'ssn': '111-11-1111', 'customer_since': '2024-01-01', 'preferred_customer': 'Y', 'street': '111 First Street', 'city': 'Falls Church', 'state': 'VA', 'zip': '22043'}' updated successfully"}
This is updateAccount Getting token response status 404

-------------

This updates an account. 
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is before update GET response status 200
This is before update Account: {"id":26,"account_number":111,"account_type":"C","paper_statement":true,"password":"test111","balance":600.0,"agreement":"test111 agreement","customer":22}
This is Account:  {'id': 26, 'account_number': 111, 'account_type': 'C', 'paper_statement': True, 'password': 'test111', 'balance': 600.0, 'agreement': 'test111 agreement', 'customer': 22}
Account balance before update:  600.0
This is updated Account balance:  1000000.0
This is Account JSON {
    "id": 26,
    "account_number": 111,
    "account_type": "C",
    "paper_statement": true,
    "password": "test111",
    "balance": 1000000.0,
    "agreement": "test111 agreement",
    "customer": 22
}
This is the updating Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is the updating body:  {
    "id": 26,
    "account_number": 111,
    "account_type": "C",
    "paper_statement": true,
    "password": "test111",
    "balance": 1000000.0,
    "agreement": "test111 agreement",
    "customer": 22
}
This is updated response status: 200
This is updated Account: {"Success":"Account '{'id': 26, 'account_number': 111, 'account_type': 'C', 'paper_statement': True, 'password': 'test111', 'balance': 1000000.0, 'agreement': 'test111 agreement', 'customer': 22}' updated successfully"}
This is create_token response status 404

-------------

This creates a Credit Transaction for an account.
This is Transaction JSON {
    "transaction_type": "C",
    "transaction_amount": 200.0,
    "initiated_date": "2024-04-25",
    "posted_date": "2024-04-25",
    "status": "C",
    "account": 26
}
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is createCrTransaction Status: 404

Account balance before update:  1000000.0
This is updated Account balance:  1000200.0
This is Account JSON {
    "id": 26,
    "account_number": 111,
    "account_type": "C",
    "paper_statement": true,
    "password": "test111",
    "balance": 1000200.0,
    "agreement": "test111 agreement",
    "customer": 22
}
This is updated Account: {"Success":"Account '{'id': 26, 'account_number': 111, 'account_type': 'C', 'paper_statement': True, 'password': 'test111', 'balance': 1000200.0, 'agreement': 'test111 agreement', 'customer': 22}' updated successfully"}
This is create_token response status 404

-------------

This creates another Credit Transaction. 
This is Transaction JSON {
    "transaction_type": "D",
    "transaction_amount": 300.0,
    "initiated_date": "2024-04-25",
    "posted_date": "2024-04-25",
    "status": "C",
    "account": 26
}
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is createCrTransaction Status: 404

Account balance before update:  1000200.0
This is updated Account balance:  999900.0
This is Account JSON {
    "id": 26,
    "account_number": 111,
    "account_type": "C",
    "paper_statement": true,
    "password": "test111",
    "balance": 999900.0,
    "agreement": "test111 agreement",
    "customer": 22
}
This is updated Account: {"Success":"Account '{'id': 26, 'account_number': 111, 'account_type': 'C', 'paper_statement': True, 'password': 'test111', 'balance': 999900.0, 'agreement': 'test111 agreement', 'customer': 22}' updated successfully"}
This is access token response status 404

-----------------

This retrieves transactions for an account. 
This is the Header:  {'content-type': 'application/json', 'Authorization': 'Bearer '}
This is Transaction response status 200
This is Transaction String content [{"id":97,"transaction_type":"c","transaction_amount":100.0,"initiated_date":"2024-04-04","posted_date":"2024-04-04","status":"C","account":26},{"id":98,"transaction_type":"D","transaction_amount":200.0,"initiated_date":"2024-04-04","posted_date":"2024-04-04","status":"p","account":26},{"id":99,"transaction_type":"C","transaction_amount":600.0,"initiated_date":"2024-04-04","posted_date":"2024-04-04","status":"C","account":26},{"id":100,"transaction_type":"D","transaction_amount":300.0,"initiated_date":"2025-03-25","posted_date":"2025-03-25","status":"C","account":26}]
Transactions for the Account ID:  26
[{'id': 97, 'transaction_type': 'c', 'transaction_amount': 100.0, 'initiated_date': '2024-04-04', 'posted_date': '2024-04-04', 'status': 'C', 'account': 26}, {'id': 98, 'transaction_type': 'D', 'transaction_amount': 200.0, 'initiated_date': '2024-04-04', 'posted_date': '2024-04-04', 'status': 'p', 'account': 26}, {'id': 99, 'transaction_type': 'C', 'transaction_amount': 600.0, 'initiated_date': '2024-04-04', 'posted_date': '2024-04-04', 'status': 'C', 'account': 26}, {'id': 100, 'transaction_type': 'D', 'transaction_amount': 300.0, 'initiated_date': '2025-03-25', 'posted_date': '2025-03-25', 'status': 'C', 'account': 26}]

Process finished with exit code 0
![image](https://github.com/user-attachments/assets/ce481889-7cf2-4a3d-87ad-0f1594db0df1)
