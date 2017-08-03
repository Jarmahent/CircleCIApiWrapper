import Circleciclient as cciaw

token = '457779903ab5f8df6f3df7b3b1dd8f993b5b0c6d'

client = cciaw.CircleciClient(token)

fd = client.trigger_new_build('github', 'jarmahent', 'gameengine', 'master')

print(fd.previous)








