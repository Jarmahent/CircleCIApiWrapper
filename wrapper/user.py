import Circleciclient as cciaw

token = ''

client = cciaw.CircleciClient(token)

me = client.me()
print(me.all_emails)