'''
@Author: Wang Meng
@Date: 2020-06-27 17:32:40
@LastEditors: Wang Meng
@LastEditTime: 2020-06-28 14:04:40
@Description: extract useful information from json, generate txt file
'''
import json


def process_continents(continent_json_path, continent_txt_path):
    with open(continent_json_path, "r") as fi:
        with open(continent_txt_path, "w") as fo:
            for line in fi:
                record = json.loads(line.strip())
                fo.write(record["objectId"] + "\t" +
                         record["code"] + "\t" + record["name"] + "\n")
            fi.close()
            fo.close()


def process_languages(language_json_path, language_txt_json):
    with open(language_json_path, "r") as fi:
        with open(language_txt_json, "w") as fo:
            for line in fi:
                record = json.loads(line.strip())
                fo.write(record["objectId"] + "\t" +
                         record["code"] + "\t" + record["name"] + "\t" + record["native"] + "\n")
            fi.close()
            fo.close()


def process_countries(country_json_path, country_txt_json):
    with open(country_json_path, "r") as fi:
        with open(country_txt_json, "w") as fo:
            for line in fi:
                record = json.loads(line.strip())
                fo.write(record["objectId"] + "\t" +
                         record["code"] + "\t" + record["name"] + "\t" +
                         record["native"] + "\t" + record["continent"]["objectId"] + "\t" + 
                         record["capital"] + "\t" + record["currency"] + "\t" + 
                         record["emoji"] + "\n")
            fi.close()
            fo.close()


def process_provinces(province_json_path, province_txt_json):
    with open(province_json_path, "r") as fi:
        with open(province_txt_json, "w") as fo:
            for line in fi:
                record = json.loads(line.strip())
                if "Subdivion_Type" in record.keys():
                    Subdivion_Type = record["Subdivion_Type"]
                else:
                    Subdivion_Type = ""
                fo.write(record["objectId"] + "\t" +
                         record["Country_Code"] + "\t" + record["Subdivision_Code"] + "\t" +
                         record["Subdivision_Name"] + "\t" + Subdivion_Type + "\t" +
                         record["country"]["objectId"] + "\n")
            fi.close()
            fo.close()


def process_cities(city_json_path, city_txt_json):
    with open(city_json_path, "r") as fi:
        with open(city_txt_json, "w") as fo:
            for line in fi:
                record = json.loads(line.strip())
                if "country" in record.keys():
                    countryId = record["country"]["objectId"]
                else:
                    countryId = ""
                fo.write(record["objectId"] + "\t" + record["name"] + "\t" +
                         str(record["location"]["latitude"]) + "\t" +
                         str(record["location"]["longitude"]) + "\t" + 
                         str(record["cityId"]) + "\t" + countryId + "\t" +
                         record["adminCode"] + "\n")
            fi.close()
            fo.close()


if __name__ == "__main__":
    continent_json_path = "backup4app/json/Continents.json"
    continent_txt_path = "backup4app/txt/Continents.txt"
    process_continents(continent_json_path, continent_txt_path)

    # language_json_path = "backup4app/json/Languages.json"
    # language_txt_path = "backup4app/txt/Languages.txt"
    # process_languages(language_json_path, language_txt_path)

    # country_json_path = "backup4app/json/Countries.json"
    # country_txt_path = "backup4app/txt/Countries.txt"
    # process_countries(country_json_path, country_txt_path)

    # province_json_path = "backup4app/json/Provinces.json"
    # province_txt_path = "backup4app/txt/Provinces.txt"
    # process_provinces(province_json_path, province_txt_path)

    # for i in range(1,5):
    #     city_json_path = "backup4app/json/Cities" + str(i) + ".json"
    #     city_txt_path = "backup4app/txt/Cities" + str(i) + ".txt"
    #     process_cities(city_json_path, city_txt_path)

