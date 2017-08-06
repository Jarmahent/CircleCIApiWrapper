import CircleCiClient as cciaw
from private import my_token
token = my_token.token

client = cciaw.CircleCiClient(token)
data = client.follow_new_project('github', 'jarmahent', 'gameengine')
print(data.following)

