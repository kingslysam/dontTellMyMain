import urllib.request, json
companyCode = input("Enter the company:")
urlString = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'+companyCode+'?modules=price'
resp = urllib.request.urlopen(urlString)
data = json.loads(resp.read())
price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(price)