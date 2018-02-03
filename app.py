from database import Database
from models.blog import Blog
from models.post import Post
import pprint


def add(a: int, b: int) -> int:
    return a + b



pp = pprint.PrettyPrinter(indent=4)

__author__ = 'sf'

Database.initialize()

blog = Blog(author="Jose",
            title="Sample title",
            description="Sample description")

# blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

posts = Post.from_blog("d5b78c6815c24cd9b8437f85b004e541")

for p in posts:
    pp.pprint(p)

# print() # Post.from_blog(id)
