products = [ 
{'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True}, 
{'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': 
False} 
]

instock = list(filter(lambda i: i['instock']==True, products))
print(instock)