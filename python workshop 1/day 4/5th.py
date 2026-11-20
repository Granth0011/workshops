accounts=bank_accounts = [
    {
        "account_id": 1001,
        "account_holder_name": "Aarav Sharma",
        "balance": 50000,
        "email": "aarav@gmail.com"
    },
    {
        "account_id": 1002,
        "account_holder_name": "Priya Verma",
        "balance": 75000,
        "email": "priya@gmail.com"
    },
    {
        "account_id": 1003,
        "account_holder_name": "Rahul Singh",
        "balance": 32000,
        "email": "rahul@gmail.com"
    },
    {
        "account_id": 1004,
        "account_holder_name": "Sneha Gupta",
        "balance": 95000,
        "email": "sneha@gmail.com"
    },
    {
        "account_id": 1005,
        "account_holder_name": "Amit Kumar",
        "balance": 120000,
        "email": "amit@gmail.com"
    },
    {
        "account_id": 1006,
        "account_holder_name": "Neha Mishra",
        "balance": 45000,
        "email": "neha@gmail.com"
    },
    {
        "account_id": 1007,
        "account_holder_name": "Vikram Yadav",
        "balance": 68000,
        "email": "vikram@gmail.com"
    },
    {
        "account_id": 1008,
        "account_holder_name": "Pooja Agarwal",
        "balance": 85000,
        "email": "pooja@gmail.com"
    },
    {
        "account_id": 1009,
        "account_holder_name": "Rohit Jain",
        "balance": 60000,
        "email": "rohit@gmail.com"
    },
    {
        "account_id": 1010,
        "account_holder_name": "Kavita Joshi",
        "balance": 110000,
        "email": "kavita@gmail.com"
    }
]

#Exceptions
class InvalidAccountIdException(Exception):
    pass
class InsufficientBalanceException(Exception):
    pass
class InvalidAmountException(Exception):
    pass
#Business Methods
def get_account_details(account_id):
    for account in accounts:
        if account["account_id"] == account_id:
            return account
    raise InvalidAccountIdException("account with the given id does not exists")
def deposit(account_id,amount):
    if amount < 0:
        raise InvalidAmountException("amount cannot be negative")
    account=get_account_details(account_id)
    account["balance"]=account["balance"]+amount
    print("Amount deposited successfully")

def withdraw(account_id,amount):
    if amount < 0:
        raise InvalidAmountException("amount cannot be negative")
    account = get_account_details(account_id)
    if amount > account["balance"]:
        raise InsufficientBalanceException("amount exceeds balance")
    account["balance"] = account["balance"] - amount
    print("Amount withdrawn successfully")

#caller code
print(get_account_details(10101111))