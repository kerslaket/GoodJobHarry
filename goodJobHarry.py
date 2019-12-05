import tweepy
import time
import random

#authorisation tokens
auth = tweepy.OAuthHandler(tokens)#insert tokens here
auth.set_access_token(tokens)#insert tokens here

#gets authorisation
api = tweepy.API(auth)


running = True 
while running == True:#keeps running the code while the programs open
    for status in tweepy.Cursor(api.user_timeline).items():#checks every item in the timeline
        try:
            api.destroy_status(status.id)#deletes each item
        except:
            pass
    num = random.randint(1,5)#generatesa random number between1 and 5 to pick from the 5 compliments
    try:
        if num == 1:
            api.update_status("You're doing a great job @_harrycrocker")
        if num == 2:
            api.update_status("Wow. Your just swell @_harrycrocker")
        if num == 3:
            api.update_status("You know what. You're just the best @_harrycrocker")
        if num == 4:
            api.update_status("You're doing a really good job @_harrycrocker")
        if num == 5:
            api.update_status("Wow looking handsome today @_harrycrocker")
    except:
        pass
    time.sleep(600)#waits 10 minutes
