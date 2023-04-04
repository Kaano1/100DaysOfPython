travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#:rotating_light: Do NOT change the code above
#TODO: Write the function that will allow new countries
#to be added to the travel_log. :point_down:
def add_new_country(country, count_city, city):
    new  = {"country": country, "visits": count_city, "cities": city }
    travel_log.append(new)
#:rotating_light: Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
