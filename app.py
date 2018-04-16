import tweepy
from config import Config
import wget
import sys
from Common.Ascii_converter import makeascii, monochrome


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def get_user( api,name):
    user = api.get_user(screen_name=name)
    return user


def main():
    cfg = {
        "consumer_key": Config.CONSUMER_KEY,
        "consumer_secret": Config.CONSUMER_SECRET,
        "access_token": Config.ACCESS_TOKEN,
        "access_token_secret": Config.ACCESS_TOKEN_SECRET
    }

    api = get_api(cfg)
    user = get_user(api, sys.argv[1])

    print(user)
    json = {
        "Name": user.name,
        "location": user.location,
        "tweets": user.status,
        "photo": user.profile_image_url
    }
    word = ""
    if "_normal" in json.get("photo"):
        print(json.get("photo"))
        word =str(json.get("photo")).replace("_normal", "")
        print(word)
    wget.download(word, out="Profile.jpg")

    makeascii(monochrome("Profile", ".jpg"), "Profile")

if __name__ == "__main__":
   main()
