from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from VSOAI_c_project import app
from VSOAI_c_project.InitClass import Init


import os
import pprint as pp

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
        "mass_units.txt", 
        "electric_current_units.txt", 
        "temperature_units.txt", 
        "luminous_intensity_units.txt" 
    ]
    currency_file = root_directory + sub_directory + "currencies.txt"
    print(currency_file)
    sub_files = [ root_directory + sub_directory + item for item in sub_files]

    Init.InitMainFile(home.all_units, main_file)
    Init.InitConvertableUnits(home.all_units, sub_files)
    Init.InitCurrencies(home.all_units, currency_file)


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

    print(units)
    return jsonify({"subUnits": units})

# Converts from unit A to unit B.
@app.route("/convert")
def convert():
    userCategory = str(request.args.get('userCategory', 0))
    unitFrom = str(request.args.get('unitFrom', 0))
    unitFromAmount = float(str(request.args.get('unitFromAmount', 0)))
    unitTo = str(request.args.get('unitTo', 0)) 

    if userCategory == "currencies":
        c = CurrencyRates()
        result = c.convert(unitFrom, unitTo, unitFromAmount)
    else:
        pair = {"from_value": "","to_value": ""}
        for item in home.all_units[userCategory]["units"]:
            if item["unit"] == unitFrom:
                pair["from_value"] = float(eval(item["value"]))
            elif item["unit"] == unitTo:
                pair["to_value"] = float(eval(item["value"]))
             
        result = float(pair["from_value"] * unitFromAmount / pair["to_value"])

    result = '{:,}'.format(result)
    return jsonify({"result": result})