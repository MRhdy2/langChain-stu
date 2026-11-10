import requests

url = "http://httpbin.org/post"
file_paths ={
    "file1": "test.txt",
    "file2": "test1.txt"
}
upload_files ={}

for fiele_name, file_path in file_paths.items():
    with open(file_path, "rb") as f:
        files = {fiele_name: f}
        response = requests.post(url, files=files)
        upload_files[fiele_name] = response.text
print(upload_files)