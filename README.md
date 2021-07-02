# wh_API
An API written using:
1. Python 3.9,
2. Flask,
3. Flask-JWT,
4. Flask-RESTful,
5. Flask-SQLAlchemy

The project contains the Postman collection to simplify testing and investigating the API

Available endpoints:
1) Register an user - /register (POST)
2) Signing in - /login (POST)
3) Create a store - /store/<name> (POST)
4) Create an item in the store - /item/<name> (POST)
5) Retrieve all stores - /stores (GET)
6) Retrieve a store - /store/<name> (GET)
7) Retrieve all items - /items (GET) 
8) Retrieve an item - /item/<name> (GET) 
9) Update an item - /item/<name> (PUT)
10) Delete an item - /item/<name> (DEL) 
11) Delete a store - /store/<name> (DEL) 

It the postman folder is provided a file with examples of usage the API 