# list iterator
# create list containing 5 city names use iter() to create an iterato and next to print first 3 cities

cities = ['surat', 'jhansi', 'raipur', 'banglore', 'bhilai']

city_iterator = iter(cities)

print(next(city_iterator))
print(next(city_iterator))
print(next(city_iterator))

# iterator position
num = [1, 2, 3, 4, 5, 6]

num_iterator = iter(num)

print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))