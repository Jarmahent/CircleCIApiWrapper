import Circleciclient as cciaw

token = 'e8214ce4170e05362c069a50e3c9e66aabe7ad8a'

client = cciaw.CircleciClient(token)

me = client.build_summary('github', 'jarmahent', 'pyimgur')
print(me.retry_of)