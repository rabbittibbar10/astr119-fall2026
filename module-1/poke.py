import requests
import time

url = input('Input a url: ').strip()
if not url.startswith(('http://', 'https://')):
    url = 'http://' + url
start_time = time.perf_counter()
response = requests.get(url)
nbytes = len(response.content)
end_time = time.perf_counter()
total_time = end_time - start_time
megabytes = nbytes / 1e6
if total_time > 0:
    mb_ps = megabytes / total_time
else:
    mb_ps = 0.0
print(f"{nbytes} bytes ({megabytes:.4f} MB) read from {url}")
print(f"Time taken was {total_time:.4f} seconds")
print(f"Inferred rate is {mb_ps:.2f} megabytes per second")