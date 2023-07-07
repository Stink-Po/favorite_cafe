from app.public_views.blog import *
from app.methods.blog_manager import BlogManager


@app.route("/blog", methods=["POST", "GET"])
def blog():
    num = request.args.get('num')
    if num:
        num = int(num)
    else:
        num = 1

    blog_manager = BlogManager()
    len_posts = len(blog_manager.blog)
    if len_posts % 3 == 0:
        total_page = int(len_posts / 3)
    else:
        total_page = int(len_posts/3) + 1

    posts = blog_manager.blog_post_paginate(num=num)
    return render_template("blog/blog.html",
                           user=current_user,
                           posts=posts,
                           title="Blog",
                           num=num,
                           total_page=total_page)
