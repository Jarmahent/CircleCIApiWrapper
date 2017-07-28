![alt text](http://i.imgur.com/Zzu6tJw.png "Logo Title Text 1")

# CirceCI API Wrapper for Python

### I have created this wrapper for educational purposes and it is not meant to be used for actual working purposes, but feel free to take it and edit it in anyway you like. Just make sure to credit this repo.
   
### Example code:
```python
import circleciclient

token = 'Your token here'

client = circleciClient(token)
me = client.me()
print(me.num_projects_followed)
```
`Output`
```bash
CircleCi Version: 1.1
4
```







