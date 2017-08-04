import circleciClient as cciaw

token = '457779903ab5f8df6f3df7b3b1dd8f993b5b0c6d'

client = cciaw.circleciClient(token)
for x in range(30):
    data = client.recent_builds(x)
    print("--{}-->  '{}'".format(data.reponame, data.subject))


