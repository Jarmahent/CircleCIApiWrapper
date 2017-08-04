import circleciClient as cciaw

token = ''

client = cciaw.circleciClient(token)
for x in range(30):
    data = client.recent_builds(x)
    print("--{}-->  '{}'".format(data.reponame, data.subject))


