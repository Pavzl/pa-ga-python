from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

# create a new route (/hello)
# return "Hello There"
@app.route("/hello")
def say_hello():
    return "Hello there!"

app.route("/classmates")
def get_classmates():
    return {"response_code": 200, "data": ["Dan", "Pavel", "Enzo", "Son", "Priscilla", "Sanjiev"]}

# use a route parameter
@app.route("/<name>")
def say_hello_with_name(name):
    return f"Hello there ${name}"

if __name__ == '__main__':
    app.run()

# impliment a route that returns the classmate that matches an id
# create a list of dictionaries, with each name having an id
names = [{"id"}]

@app.route("classmates/<id>")
def get_classmates(id):
    names = [{"id": 1, "name": "Dan"},  
    {"id": 1, "name": "Pavel"}, 
    {"id": 1, "name": "Enzo"},   
    {"id": 1, "name": "Son"},   
    {"id": 1, "name": "Priscilla"},   
    {"id": 1, "name": "Samjiev"}]

    for item in names:
        if item["id"] == int(id):
            return item
    
    return {"responce_code": 404}
