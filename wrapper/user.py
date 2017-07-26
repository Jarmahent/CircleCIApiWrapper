import Circleciclient as cciaw

token = ''

client = cciaw.CircleciClient(token)

for x in range(7):
    me = client.recent_builds(x)
    print(me.committer_date)
    x+=1



