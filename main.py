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
