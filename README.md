# LogicRaysPracticle
LogicRaysPracticle
# how to run project
  
 step 1: create virtualenv by this command
 ```
 python3 -m venv venv
 ```
 step 2:activate virtualev
 ```
 source venv/bin/activat
 ```
 
 step 3: install all requeirenments
 ```
 pip install -r req.txt
 ```
 step 4: run server
 ```
 python manage.py runserver
 ```
#Note:
 ```
    I have pushed all migration, sqlite3 databse and also gives you req.txt file
 ```
 
Graphql Query Example
 
# Get all orders
```
{
  allOrders{
    id
    name
  	timestamp
    placed
   	totalPrice
    totalQty
    products{
      id
      category{name}
    	brand{name}
      name
      price
      qty
      image
      
    }
  }
}
```

# get orders by ID
```
{
  orderById(id: 12){
    id
    name
  	timestamp
    placed
   	totalPrice
    totalQty
    products{
      id
      category{name}
    	brand{name}
      name
      price
      qty
      image
      
    }
  }
}
```
