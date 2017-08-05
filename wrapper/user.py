import CircleCiClient as cciaw

token = ''

client = cciaw.CircleCiClient(token)
for x in range(30):
    data = client.recent_builds(x)
    print("--{}-->  '{}'".format(data.reponame, data.subject))


