import json


#open and read JSON file
with open('products.json' ,'r')as file:
    products = json.load(file) #Parse JSON data


#display header
print("{:<15} {:<10} {:<10}".format("Name" , "price" , "Quantity"))
print("-" * 40)

# display each product in products:
for product in products:
    print("{:<15} {:<10} {:<10}".format(
        product['name'] , product['price'] , product['quantity']))
    
   
   