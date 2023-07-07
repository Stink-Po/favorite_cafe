from app.methods import *
from app.my_db_models import BlogPost


class BlogManager:
    """Manage Adding new blog posts and paginate of the blog page"""
    def __init__(self):
        self.blog = db.session.query(BlogPost).all()
        self.paginate = None
        self.new_post = None
        self.date = date.today().strftime("%B %d, %Y")

    def blog_post_paginate(self, num):
        """
        making paginate for blog page
        :param num: it's a number of the page that we are init in blog page
        :return: a paginated object from blogpost
        """
        self.paginate = BlogPost.query.paginate(per_page=3, page=num, error_out=True)
        return self.paginate

    def add_new_post(self, title, subtitle, body, img_path, author):
        """
        adding new post to BlogPost table in mysql db
        :param title: title of the blog post
        :type title: str
        :param subtitle: subtitle of the new post
        :type subtitle: str
        :param body: body of the blog post
        :type body: str encoded with flask_ckeditor
        :param img_path: path of the image of the blog post that will create from UploadPhoto class and stored
         in webserver
        :type img_path: str
        :param author: creator of the blog post
        :type author: user class object
        :return: new post that we just created
        """
        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            body=body,
            img_path=img_path,
            author=author,
            date=self.date
        )
        db.session.add(new_post)
        db.session.commit()
        self.new_post = new_post
        return self.new_post
