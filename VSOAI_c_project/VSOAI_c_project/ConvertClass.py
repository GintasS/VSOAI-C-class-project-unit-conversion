from forex_python.converter import CurrencyRates


class Convert(object):
    # Converts from unit A to unit B.
    @staticmethod
    def convert_unit(all_units, unitCategory, unitFrom, unitTo, amount):
        """
        If user chose currencies, convert from currency A to B via
        3rd party library.
        """

        # if any of the parameters are empty, inform user.
        if (len(all_units) == 0 or len(unitCategory) == 0 or len(
                unitFrom) == 0 or len(unitTo) == 0 or len(str(amount)) == 0):
            return "Invalid data."

        # If user put a negative amount, inform him.
        if amount < 0:
            return str("Negative amount.")

        if unitCategory == "currencies":
            c = CurrencyRates()
            result = c.convert(unitFrom, unitTo, amount)
        else:
            pair = {"from_value": "", "to_value": ""}

            # If user entered invalid userCategory, tell him.
            if unitCategory not in all_units:
                return str("Invalid Unit Category.")

            # Find unit A & B.
            for item in all_units[unitCategory]["units"]:

                if item["unit"] == unitFrom:
                    pair["from_value"] = float(eval(item["value"]))
                if item["unit"] == unitTo:
                    pair["to_value"] = float(eval(item["value"]))

            # If we didn't found user entered units, inform him.
            if len(str(pair["from_value"])) == 0 or len(
                    str(pair["to_value"])) == 0:
                return "Invalid Unit(s)."

            # Convert.
            result = float(pair["from_value"] * amount / pair["to_value"])

        return result
