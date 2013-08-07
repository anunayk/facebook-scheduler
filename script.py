from facepy import GraphAPI
from time import *

POST_TIME = "07 08 2013 18:15:00" # 07 August 2013 18:15:00
POST_MESSAGE = "Your message here!"

t1 = localtime()
t2 = strptime(POST_TIME, "%d %m %Y %H:%M:%S")
k = mktime(t2) - mktime(t1)
sleep(k-1)

ACCESS_TOKEN = 'From the Graph API Explorer'

graph = GraphAPI(ACCESS_TOKEN)
graph.post('me/feed', message=POST_MESSAGE)