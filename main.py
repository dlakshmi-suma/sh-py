# import requests

# token = ''

# # Roll resource token (used to access resources)
# TOKEN = "artifact-acc-token"  # Replace with your credential ID or actual token value
# url = "https://https://eu.artifactory.swg-devops.com/access/api/v1/tokens"  # Replace with the actual URL

# headers = {
#     "Authorization": "Bearer " + TOKEN,
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# data = {
#     "audience": "jfac@*",
#     "description": "8 Day Access Token",
#     "include_reference_token": "true",
#     "expires_in": "691200"
# }

# response = requests.post(url, headers=headers, data=data)

# if response.status_code == 200:
#     j = response.json()
#     token = j['reference_token']
# else:
#     print("Request failed with status code:", response.status_code)
#     exit(1)

# print(TOKEN)
# print(j)
print("Hello World")
