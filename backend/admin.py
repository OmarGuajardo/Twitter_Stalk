import tweepy
class Admin:

    def __init__(self,consumer_key,consumer_secret,access_token,__access_token_secret):
        self.__consumer_key = consumer_key
        self.__consumer_secret = consumer_secret
        self.__access_token = access_token
        self.__access_token_secret = __access_token_secret
        # self.__consumer_key = "7ksSJSUIId4vc880oikcdcyeB"
        # self.__consumer_secret = "6Has0BGJ4gwgML5PSwkpOCpminmPHS5D7NyjPAvSJBwShOoHfK"
        # self.__access_token = "3105662358-5dJtYPmRqz4BnTeIXffPGRgr7X3PFVWx43w4l2b"
        # self.__access_token_secret = "GJlH2gK9gcv7W9kbC1oFvywhgZWb63xnroU0OgxJkPo0H"

        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)
        self.api = tweepy.API(auth)
    
    def get_profile_pic(self, username):
        user_object = self.api.get_user(username)
        return(user_object.profile_image_url)

    def followers(self,username):
        users = []
        page_count = 0
        for i, user in enumerate(tweepy.Cursor(self.api.followers, id=username, count=200).pages()):
            users += user
        return users
    def following (self, username):
        users = []
        page_count = 0
        for i, user in enumerate(tweepy.Cursor(self.api.friends, id=username, count=200).pages()):
            users += user
        return users

    def make_tweet(self,text):
        self.api.update_status(text)
        print("You have published your tweet")

    def make_tweet_picture(self , address_of_pic, text):
        media_object = self.api.media_upload(address_of_pic)
        self.api.update_with_media(address_of_pic,status = text)
        print("You have published your tweet with a pic!!!")

    def dming(self,recipient_handle,message):
        recipient_id = self.api.get_user(recipient_handle).id
        self.api.send_direct_message(recipient_id,message)
        print("You succesfully made a direct message to "+ recipient_handle)

    def stalking(self, username , amount_of_favorites):
        username_id = self.api.get_user(username).id
        username_timeline = self.api.user_timeline(username_id, count = amount_of_favorites)
        for statuses in username_timeline:   
            try:
                self.api.create_favorite(statuses.id)
            except:
                pass
        print("Congrats you liked A LOT of "+ username +"'s tweets")

    def unfollow_list(self,username):
        followers_object = self.followers(username)
        following_object = self.following(username)
        unfollow_names = ""
        counter = 0
        for i,following in enumerate(following_object):
            counter += 1
            if not(following.verified) and not(following in followers_object):
                unfollow_names += "@"+following.screen_name+"\n"
            if(counter == 50 or i == len(following_object)-1):
                print(unfollow_names)
                self.dming(username,unfollow_names)
                unfollow_names = ""
                counter = 0
        
        return unfollow_names
        
        

        