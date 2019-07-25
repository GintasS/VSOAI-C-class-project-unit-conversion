class Init(object):

    """
    Initialize main file.
    Main file holds our unit categories, such as "time", "length" and etc.
    """
    @staticmethod
    def InitMainFile(all_units, main_file):
        print("------------------------")
        file = open(main_file, "r")
        file_data = file.readlines()[2:]

        # Iterate over data.
        for line in file_data:
            unit = line.split(",")
            key = unit[2].strip()

            all_units[key] = {"name": unit[0], "symbol": unit[1], "units": []}

        print("(Main Units): Main File is COMPLETE!")

    """
    Read all sub unit types
    (time -> second, hour, day; length -> metre, centimetre, kilometre and etc).
    """
    @staticmethod
    def InitConvertableUnits(all_units, sub_files):
        length = len(sub_files)
        # Holds sub-unit file index.
        index = 0

        # For every unit category.
        for key in all_units.keys():
            if index + 1 > length:
                break

            # Open a sub-unit file for a current unit category.
            file = open(
                sub_files[index],
                "r",
                encoding='ascii',
                errors='ignore')
            file_list = file.readlines()

            # Iterate over sub-unit data.
            for line in file_list:
                # Split by "|".This is our seperator for unit name, value,
                # description.
                temp = line.split("|")
                tempDict = {"unit": temp[0], "value": temp[1]}

                # If unit has description, take it, overwhise write "-".
                if len(temp) == 3:
                    tempDict["desc"] = temp[2]
                else:
                    tempDict["desc"] = "-"

                # Add a sub-unit.
                all_units[key]["units"].append(tempDict)

            print("(Sub Units):", sub_files[index], " is COMPLETE!")
            index += 1

        print("------------------------\n")

    # Initializes currencies.
    @staticmethod
    def InitCurrencies(all_units, currency_file):
        file = open(currency_file, "r")
        file_data = file.readlines()

        for item in file_data:
            all_units["currencies"]["units"].append(
                {"unit": item, "value": 0, "desc": "N/A"})
