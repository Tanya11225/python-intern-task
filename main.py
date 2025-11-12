import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    users = res.json()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
    exit(1)

if not users:
    print("No users returned.")
    exit(0)

print(" All Users")
print("=" * 50)

for i, u in enumerate(users, 1):
    name = u.get('name', '—')
    username = u.get('username', '—')
    email = u.get('email', '—')
    city = u.get('address', {}).get('city', '—')

    print(f"User {i}:")
    print(f"Name: {name}")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"City: {city}")
    print("-" * 40)

#  city starts with 'S'
print("\n Bonus: Cities starting with 'S'")
print("=" * 50)

s_users = [
    u for u in users
    if u.get('address', {}).get('city', '').startswith('S')
]

if s_users:
    for i, u in enumerate(s_users, 1):
        print(f"User {i}:")
        print(f"Name: {u['name']}")
        print(f"Username: {u['username']}")
        print(f"Email: {u['email']}")
        print(f"City: {u['address']['city']}")
        print("-" * 40)
else:

    print("None found.")


# output
"""
All Users
==================================================
User 1:
Name: Leanne Graham
Username: Bret
Email: Sincere@april.biz
City: Gwenborough
----------------------------------------
User 2:
Name: Ervin Howell
Username: Antonette
Email: Shanna@melissa.tv
City: Wisokyburgh
----------------------------------------
User 3:
Name: Clementine Bauch
Username: Samantha
Email: Nathan@yesenia.net
City: McKenziehaven
----------------------------------------
User 4:
Name: Patricia Lebsack
Username: Karianne
Email: Julianne.OConner@kory.org
City: South Elvis
----------------------------------------
User 5:
Name: Chelsey Dietrich
Username: Kamren
Email: Lucio_Hettinger@annie.ca
City: Roscoeview
----------------------------------------
User 6:
Name: Mrs. Dennis Schulist
Username: Leopoldo_Corkery
Email: Karley_Dach@jasper.info
City: South Christy
----------------------------------------
User 7:
Name: Kurtis Weissnat
Username: Elwyn.Skiles
Email: Telly.Hoeger@billy.biz
City: Howemouth
----------------------------------------
User 8:
Name: Nicholas Runolfsdottir V
Username: Maxime_Nienow
Email: Sherwood@rosamond.me
City: Aliyaview
----------------------------------------
User 9:
Name: Glenna Reichert
Username: Delphine
Email: Chaim_McDermott@dana.io
City: Bartholomebury
----------------------------------------
User 10:
Name: Clementina DuBuque
Username: Moriah.Stanton
Email: Rey.Padberg@karina.biz
City: Lebsackbury
----------------------------------------

 Bonus: Cities starting with 'S'
==================================================
User 1:
Name: Patricia Lebsack
Username: Karianne
Email: Julianne.OConner@kory.org
City: South Elvis
----------------------------------------
User 2:
Name: Mrs. Dennis Schulist
Username: Leopoldo_Corkery
Email: Karley_Dach@jasper.info
City: South Christy
----------------------------------------
"""
