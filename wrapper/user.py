import Circleciclient as cciaw

token = ''

client = cciaw.CircleciClient(token)

me = client.build_summary('github', 'jarmahent', 'pyimgur', 4)
print(me.build_num)

