import circleciClient as cciaw

token = ''

client = cciaw.circleciClient(token)

fd = client.trigger_new_build('github', 'jarmahent', 'gameengine', 'master')

print(fd.previous)








