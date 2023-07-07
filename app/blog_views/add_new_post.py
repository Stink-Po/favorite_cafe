from app.blog_views import *
from flask_login import login_required, current_user
from app.methods.decorators import admin_only
from app.forms.create_blog_post_form import CreateBlogPostForm
from flask import request, render_template, redirect, url_for
from app.methods.upload_photo import UploadPhoto
from app.methods.blog_manager import BlogManager
from app.methods.send_mail import SendGroupMail


@app.route('/blog/add_new_post', methods=["POST", "GET"])
@login_required
@admin_only
def add_blog_post():
    form = CreateBlogPostForm()
    if form.validate_on_submit() and request.method == 'POST':
        image_maker = UploadPhoto()
        blog_manager = BlogManager()
        img_path = image_maker.upload_photo_blog_post()
        new_post = blog_manager.add_new_post(title=form.title.data,
                                             subtitle=form.subtitle.data,
                                             body=form.body.data,
                                             img_path=img_path,
                                             author=current_user,
                                             )

        SendGroupMail(new_post=new_post).send()
        return redirect(url_for('blog'))

    return render_template('blog/add_post.html',
                           user=current_user,
                           form=form,
                           title='New Post')
