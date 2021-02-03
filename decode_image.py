from encoder import spotify_bar_decode as s_b_decode
from image_read import get_sequence
import requests

sequence = get_sequence('code_test.jpeg')


del sequence[-1], sequence[0], sequence[10]

print(sequence)

decoded = s_b_decode(sequence)

print(decoded)

url = "https://spclient.wg.spotify.com/scannable-id/id/" + str(decoded) + "?format=json"

headers = {
  'Host': 'spclient.wg.spotify.com',
  'Accept-Encoding': 'gzip, deflate',
  'Connection': 'close',
  'Accept': '*/*',
  'Authorization': 'Bearer ' # Add your token here
}

response = requests.get(url, headers=headers)

print(response.json())

