__author__ = 'hira'

from twitter.twitter_client import TwitterClient

def main():
    client = TwitterClient()
    client.post_with_date("@yamazaki_sensei 落ちた")

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        import sys
        traceback.print_exc()
        print ("ERROR")
        sys.exit(1)
