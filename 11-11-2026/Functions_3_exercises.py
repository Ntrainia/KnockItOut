# 8-3. T-Shirt:

def make_shirt(size):
    print("Your shirt size is " + size + ".")

make_shirt('large')
make_shirt(size = 'medium')

# 8-4. Large Shirts:
def make_shirt_2(size = 'Large'):
    print("\nYour shirt size is " + size.lower() + ".")
    print("Your shirt message's is 'I love Python.'")

make_shirt_2()
make_shirt_2('small')

# 8-5. Cities:
def describe_city(city, country):
    print("\n" + city + " is in " + country)

describe_city('New York City', 'United States')
describe_city(city = 'Tokyo', country = 'Japan')
describe_city(city = 'Seoul', country = 'Korea')