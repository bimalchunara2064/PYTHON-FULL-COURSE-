#Extract from Souces
import requests,json
data=requests.get('https://dummyjson.com/products')
product_data=data.json()
print(type(product_data))  #<class,dict>
products=product_data['products']
print(type(products)) #<class,list>
print(len(products))  #30

#Transform

#Load into json file