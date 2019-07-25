from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect
from VSOAI_c_project import app
from VSOAI_c_project.InitClass import Init
from VSOAI_c_project.ConvertClass import Convert

import os
import pprint as pp

# Main route: will load all text files & initialize main data structure.
@app.route('/')
@app.route('/home')
def home():

    # Main data structre
    home.all_units = {}

    # Directories
    root_directory = os.getcwd()
    sub_directory = "\\VSOAI_c_project\\static\\txt files\\"

    # Text files
    main_file = root_directory + sub_directory + "units.txt"
    sub_files = [
        "time_units.txt",
        "length_units.txt",
        "mass_units.txt",
        "electric_current_units.txt",
        "temperature_units.txt",
        "luminous_intensity_units.txt"
    ]
    currency_file = root_directory + sub_directory + "currencies.txt"
    sub_files = [root_directory + sub_directory + item for item in sub_files]

    # Read data & add it to the data structure.
    Init.InitMainFile(home.all_units, main_file)
    Init.InitConvertableUnits(home.all_units, sub_files)
    Init.InitCurrencies(home.all_units, currency_file)
    

    # Categories to initialize 1st dropdown.
    categories = [key for key in home.all_units.keys()]

    # Render the template(GUI).
    return render_template(
        'index.html',
        title='Unit Co',
        categories=categories
    )

# Units update: will update unit dropdowns on user selection.
@app.route("/units-update")
def index_update():
    userCategory = str(request.args.get('userCategory', 0))

    units = []
    for item in home.all_units[userCategory]["units"]:
        units.append(item)

    return jsonify({"subUnits": units})

# Convert: will convert from unit A to unit B.
@app.route("/convert")
def convert():
    # Url parameters from AJAX call.
    unitCategory = str(request.args.get('userCategory', 0))
    unitFrom = str(request.args.get('unitFrom', 0))
    amount = float(str(request.args.get('unitFromAmount', 0)))
    unitTo = str(request.args.get('unitTo', 0))

    result = Convert.convert_unit(home.all_units, unitCategory, unitFrom, unitTo, amount)
    result = '{:,}'.format(result) + " " + unitTo + "(s)"

    return jsonify({"result": result})