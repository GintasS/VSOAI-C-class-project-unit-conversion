class Init(object):

    # Read all unit types(time, length, temperature and etc).
    @staticmethod
    def InitMainFile(all_units, main_file):
        print("------------------------")            
        current_file = open(main_file, "r")
        file_data = current_file.readlines()[2:]        
 
        for line in file_data:
            unit = line.split(",")
            key = unit[2].strip()
            all_units[key] = { "name": unit[0], "symbol": unit[1], "units":[] }
            
        print("(Main Units): Main File is COMPLETE!")
    
    # Read all sub unit types(time -> second, hour, day;length -> metre, centimetre, kilometre).
    @staticmethod
    def InitConvertableUnits(all_units, sub_files):
        length = len(sub_files)
        index = 0
        for key in all_units.keys():
            if index + 1 > length:
                break

            current_file = open(sub_files[index], "r", encoding='utf-8', errors='ignore')
            current_file_list = current_file.readlines()
        
            for line in current_file_list:
                temp = line.split("|")

                tempDict = { "unit": temp[0], "value": temp[1] }

                if len(temp) == 3:
                    tempDict["desc"] = temp[2]
                else:
                    tempDict["desc"] = "-"

                all_units[key]["units"].append(tempDict)

            print("(Sub Units):", sub_files[index]," is COMPLETE!")
            index += 1
            
        print("------------------------\n")
