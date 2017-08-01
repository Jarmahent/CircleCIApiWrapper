import Circleciclient as cciaw

token = ''

client = cciaw.CircleciClient(token)

fd = client.trigger_new_build('github', 'jarmahent', 'CircleCIApiWrapper', 'master')

print(fd)








