import pymongo
from pymongo import MongoClient
import humanize
import datetime
from bson import ObjectId


class Posts:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.codewizard
        self.Users=self.db.users
        self.Posts=self.db.posts
        self.Comments=self.db.comments
    def insert_post(self,data):
        inserted = self.Posts.insert({'username': data.username, 'content': data.content,"date_added":datetime.datetime.now()})
        return True
    def add_comment(self,comment):
        inserted=self.Comments.insert({"post_id":comment["post_id"],"content":comment["content"],
                                               "date-added":datetime.datetime.now(),"username":comment["username"]})
        print("soemthig")
        return inserted
    def get_all_post(self):
        all_posts=self.Posts.find()
        new_posts=[]

        for post in all_posts:
            post["user"]=self.Users.find_one({"username": post["username"]})
            post["timestamp"]=humanize.naturaltime(datetime.datetime.now()-post["date_added"])
            post["old_comments"]=self.Comments.find({"post_id":str(post["_id"])})
            post["comments"]=[]
            for comment in post["old_comments"]:
                comment["user"]=self.Users.find_one({"username":comment["username"]})
                comment["timestamp"]=humanize.naturaltime(datetime.datetime.now()-comment["date-added"])
                post["comments"].append(comment)
            new_posts.append(post)
        return new_posts
