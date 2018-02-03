from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        # the underscore before method meaans it's a private method
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        pass

    def _user_has_account(self):
        return Database.find_one('blogs', {'author': self.user}) is not None

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()

    def run_menu(self):
        # User read or write blogs?
        # if read:
            # list blogs in Database
            # allow user to pick
            # display posts
        # if write:
            # check if user has a blogs
            # if they do, prompt to write a post2
            # if not, prompt to create new blog
        pass
