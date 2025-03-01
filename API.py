import requests

#response = requests.get("https://fakestoreapi.com/products")
product = {'title': 'New Product', 'price': 29.99, 'descrition': 'this is a new product', 'category': 'unknown'}
response = requests.post('https://fakestoreapi.com/products', json=product)

print(response.json())
