"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, jsonify, render_template, request
from VSOAI_c_project import app

from VSOAI_c_project.InitClass import Init
import os
import pprint as pp

from twilio.rest import Client



@app.route('/')
@app.route('/home')
def home():
    home.all_units = {}
    root_directory = os.getcwd()
    sub_directory = "\\VSOAI_c_project\\"
    
    main_file = root_directory + "\\VSOAI_c_project\\units.txt"
    sub_files = [
        "time_units.txt", 
        "length_units.txt", 
        "weight_units.txt", 
        "electric_current_units.txt", 
        "temperature_units.txt", 
        "luminous_intensity_units.txt" 
    ]

    # Your Account SID from twilio.com/console
    account_sid = "AC45c52f320a98bc90abb4fbf632edabd5"
    # Your Auth Token from twilio.com/console
    auth_token  = "896603752b6d9afb6260159b3b82e563"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+37068532799", 
        from_="+37066802970",
        body="IVAN GOES TO IVANYLAND!")

    print(message.sid)


    sub_files = [ root_directory + sub_directory + item for item in sub_files]

    Init.InitMainFile(home.all_units, main_file)
    Init.InitConvertableUnits(home.all_units, sub_files)

    pp.pprint(home.all_units)

    categories = [key for key in home.all_units.keys()]

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Unit Co',
        categories = categories,
        year=datetime.now().year,
    )

# Update dropdowns with sub units.
@app.route("/units-update")
def index_update():
    userCategory = str(request.args.get('userCategory', 0))

    units = []
    for item in home.all_units[userCategory]["units"]:
        units.append(item)

    return jsonify({"subUnits": units})

# Converts from unit A to unit B.
@app.route("/convert")
def convert():
    userCategory = str(request.args.get('userCategory', 0))
    unitFrom = str(request.args.get('unitFrom', 0))
    unitFromAmount = float(str(request.args.get('unitFromAmount', 0)))
    unitTo = str(request.args.get('unitTo', 0)) 

    pair = {"from_value": "","to_value": ""}
    for item in home.all_units[userCategory]["units"]:
        if item["unit"] == unitFrom:
            pair["from_value"] = float(eval(item["value"]))
        elif item["unit"] == unitTo:
            pair["to_value"] = float(eval(item["value"]))
             
    result = float(pair["from_value"] * unitFromAmount / pair["to_value"])
    result = '{:,}'.format(result)
    return jsonify({"result": result})

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
