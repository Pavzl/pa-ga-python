import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("baseline.html")

@app.route("/cars")
def get_cars():
    car_list = pd.read_csv("cars.csv")
    return render_template("index(cars_list).html", cars=car_list.to_dict("records"))

@app.route("/cars/new", methods=["GET", "POST"])
def add_new_cars():
    if request.method == "GET":
        return render_template("new_cars.html") 
    else:
        cars = pd.read_csv("cars.csv")
        car_list = cars.to_dict("records")

        #car_id = request.form["id"]  probably dont need this
        car_make = request.form["make"]
        car_model = request.form["model"]
        car_year = request.form["year"]
        car_color = request.form["color"]
        car_mileage = request.form["mileage"]
        car_price = request.form["price"]
        new_car = {}

        new_car_id = car_list[len(car_list) - 1]["id"] + 1

        new_car["id"] = new_car_id
        new_car["make"] = car_make
        new_car["model"] = car_model
        new_car["year"] = car_year
        new_car["color"] = car_color
        new_car["mileage"] = car_mileage
        new_car["price"] = car_price

        car_list.append(new_car)

        df = pd.DataFrame(car_list).set_index("id") 
        df.to_csv("cars.csv")
        return redirect(url_for("get_cars"))

@app.route("/cars/<id>", methods=["GET", "PUT", "POST"])
def edit_cars(id):
    car_list = display_cars_list()
    selected_car = None
    for car in car_list:
        if car["id"] == int(id):
            selected_car = car
            break
    if request.method == "GET":
        return render_template("edit_cars.html", cars=selected_car)
    
    else:
        data = {
            'id': car['id'],
            "make": request.form["make"],
            "model": request.form["model"],
            "year": request.form["year"],
            "color": request.form["color"],
            "mileage": request.form["mileage"],
            "price": request.form["price"],
        }
        update_cars(car_list, data)
        df = pd.DataFrame(car_list).set_index("id")
        df.to_csv("cars.csv")
        return redirect(url_for("get_cars"))

@app.route("/cars/<id>/delete", methods=["POST","DELETE"])
def delete_cars(id):
   delete_cars(request.form["delete"])
   return redirect(url_for("get_cars"))


def display_cars_list():
    car = pd.read_csv("cars.csv")
    return car.to_dict("records")

def update_cars(car_list, new_car):
    for idx in range(len(car_list)):
        if new_car["id"] == car_list[idx]["id"]:
            car_list[idx] = new_car
            break

def delete_cars(id):
    car_list = display_cars_list()
    new_list = [car for car in car_list if not (car["id"] == int(id)) ]
    df = pd.DataFrame(new_list).set_index("id")
    df.to_csv("cars.csv")


if __name__ == "__main__":
    app.run(debug=True)