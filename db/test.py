import requests # type: ignore

request = requests.get(url="https://ecounter.bank-maskan.ir/do-transaction")

print(request.status_code)