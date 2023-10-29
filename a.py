import requests
import json

# -------------------------------
# |          SETTINGS           |
# -------------------------------
sandbox_url = "https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data"
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJuYmYiOjE2OTYwMzIwMDAsImFwaV9zdWIiOiJlZTQxMmU1Y2E3ODVhZDY2NDk1MDMyMzM0ZmRkMDdjMDhjOTI5OThjOWQwNWNmZDZiMDk1NmU2NjU1NmM3N2NjMTcxNzIwMDAwMDAwMCIsInBsYyI6IjVkY2VjNzRhZTk3NzAxMGUwM2FkNjQ5NSIsImV4cCI6MTcxNzIwMDAwMCwiZGV2ZWxvcGVyX2lkIjoiZWU0MTJlNWNhNzg1YWQ2NjQ5NTAzMjMzNGZkZDA3YzA4YzkyOTk4YzlkMDVjZmQ2YjA5NTZlNjY1NTZjNzdjYyJ9.Q4w0WxpEG-pmRx3cvINVtdc5HiMWu2hHekGDcLC1v6RlIYM3iJNSTDGoVCilFfYvyQBigbDwgbNmoAAdxKXaL6M-gBsbc17PcagSfgjR11Rp_7V5mW5YxG3RSIAv12yUT6EOMtLI36yPcFmejFmA_2cqPerVvd3Lg2W-aJKUnBVwiFdeSbHyNPrjoupfbcAvabrtxjRdBi2rGlvSyj5CykAPmVvq3O2hbgdhaOrJySZ0e1eO5FYfn4UXzVTMPyKXQcI2angF4EIWX9gUqqUzfnYNfTsvJFe4leCP-zzQRunIYQDTeBEASlkTYeXTJboR42vZDm_AbEisTtzcnIiMAA"

# -------------------------
# |      POST METHOD      |
# -------------------------
def CreateRandomAccounts(quantity):
  url = f"{sandbox_url}/accounts/create"

  payload = json.dumps({
    "quantity": f"{quantity}",
    "state": "open"
  })
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)


def CreateTransactions(id):
  url = f"{sandbox_url}/transactions/accounts/{id}/create"

  payload = json.dumps({
    "quantity": "1"
  })
  
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)



# -------------------------
# |      GET METHOD       |
# -------------------------
def getAllAccounts():
  url = f"{sandbox_url}/accounts"

  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
  }

  params = {}

  response = requests.request("GET", url, headers=headers, params=params)
  print(response.text)

def getAllAccountsWithFilters():
  url = f"{sandbox_url}/accounts?state=eq:closed"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
    'Cookie': 'AWSALB=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF; AWSALBCORS=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

def getSpecificAccount(id):
  url = f"{sandbox_url}/accounts/{id}"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
    'Cookie': 'AWSALB=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF; AWSALBCORS=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response

def getAllTransactions(id):
  url = f"{sandbox_url}/transactions/accounts/{id}/transactions"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
    'Cookie': 'AWSALB=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF; AWSALBCORS=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

def getAllTransactionsWithFilter(id):
  url = f"{sandbox_url}/transactions/accounts/{id}/transactions?currency=eq:GBP"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
    'Cookie': 'AWSALB=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF; AWSALBCORS=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)

def getTransactionsbyID(id):
  url = f"{sandbox_url}/transactions/accounts/{id}/transactions/97cf63e5-9e2e-4990-9535-fefbafc052c1"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'Version': '1.0',
    'Authorization': f'Bearer {api_key}',
    'Cookie': 'AWSALB=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF; AWSALBCORS=i+JVhzdbzKTVld42IXPrc6YyJwYAhuMHZ8OjaspNi1prOFxcK6O+01qYkppXplGsM1KmOvRyZ/TxSDO0g6mZ9rFgE2pqmDxdXrgBu45fTOo3G2JhpsrttbZkNvMF'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)



# "YourFirstName", "YourLastName", "+1234567890", 1000.0, 750, 5000.0, "123456", 3, "open", "USD", "your.email@example.com", "CreditCard", "123 Main St, Your City, Your Country"
# CreateCustomAccounts("YourFirstName", "YourLastName", "+1234567890", 1000.0, 750, 5000.0, "123456", 3, "open", "USD", "your.email@example.com", "CreditCard", "123 Main St, Your City, Your Country")
# CreateCustomAccounts()
#getAllAccounts()