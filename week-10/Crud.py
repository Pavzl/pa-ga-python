# CRUD

# Create
# Read
# Update
# Delete



# - templates
# - storage (database | files(csv)

# - route parameter

# crud application for product in a store

# what are we storing about products
# inventory_level * (we may want to store this separately)
# name
# description
# id
# id,name,description,file (products.csv)

# read product data
# update product
# delete product
from crypt import methods
import pandas as pd
from flask import Flask, render_template, request, redirrect, url_for
import json

app = Flask(__name__)

# create route to display all products

@app.route("/")
def index():
    return render_template("base.html")


@app.route('/products')
def get_products():
    product_list = pd.read_scv("products.csv")
    

    return render_template("proucts.html", products = product_list.to_sict("records"))

# route to add a new product
@app.route("products/new", methods=["GET", "POST"])
def add_new_product():
    if request.method == "GET":
        return render_template("new_product.html")
    else:
        # get the current products from file
        product = pd.read_csv("product.csv")
        product_list = product.to_dict("records")

        # add new product to list
        product_name = request.form["name"]
        product_desc = request.form["description"]
        product_price = request.form["price"]
        new_product = {}
        
        new_product_id = product_list[len(product_list) - 1]["id"] + 1
        
        new_product["id"] = new_product_id
        new_product["name"] = product_name
        new_product["desc"] = product_desc
        new_product["price"] = product_price

        product_list.append(new_product)
        # write updated list to file
        
        indexes = []
        #for p in product_list:
           # indexes.append(p["id"])
        df = pd.DataFrame(product_list).set_index(indexes)

        df.to_csv("products.csv")

        return render_template("products.html")

# route to edit each product
@app.route("/products/<id>")
def edit_product(id):
    #1 get the list of products from the csv file

    #2 find the product that matches the given id
    #for loop like in classes

    #3 print the product
    pass

if __name__ == "__main__":
    app.run(debug = True)