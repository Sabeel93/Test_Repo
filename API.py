#import requests

#response = requests.get("https://fakestoreapi.com/products")

#print(response.json())

fetch('https://fakestoreapi.com/products/1')
            .then(res=>res.json())
            .then(json=>console.log(json))
