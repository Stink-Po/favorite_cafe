from app.public_views.blog import *


@app.route("/blog/post/<int:post_id>", methods=["GET"])
def load_blog_post(post_id):
    database_info = DataBaseInfo()
    post = database_info.ret_a_blog_post_with_id(post_id=post_id)

    return render_template("blog/load_blog_post.html",
                           user=current_user,
                           post=post,
                           title=post.title)
