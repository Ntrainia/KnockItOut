# 8-6 City Names:
def city_country(city, country):
    pair = city + ", " + country
    return pair.title()


while True:
    print("Please tell me the name of your city and country.")
    print("(enter 'q' at any time to quit)")
    city = input("Enter city: ")
    if city == 'q':
        break
    country = input("Enter country: ")
    if country == 'q':
        break

    city_country_pair = city_country(city, country)
    print(city + ", " + country)
