import requests

url = 'http://u.com/'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Hureee! Response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Oh nooo, salah requests {response.status_code}')
except Exception as e:
    print(f'Error Bang! {e}')
print('Program ended.')