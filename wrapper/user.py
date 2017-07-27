import Circleciclient as cciaw

token = 'e8214ce4170e05362c069a50e3c9e66aabe7ad8a'

client = cciaw.CircleciClient(token)

fd = client.detailed_single_build('github', 'jarmahent', 'CircleCIApiWrapper', '1')
print(fd)








