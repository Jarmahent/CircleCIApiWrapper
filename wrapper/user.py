import Circleciclient as cciaw

token = ''

client = cciaw.CircleciClient(token)

fd = client.detailed_single_build('github', 'jarmahent', 'CircleCIApiWrapper', '1')
print(fd)








