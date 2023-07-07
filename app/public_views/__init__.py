from flask import Blueprint, render_template, flash, request, redirect, url_for
from app.methods.database_methods import DataBaseInfo
from flask_login import current_user, login_required, login_user
from app.methods.api_manager import ApiInfo
from app.methods.get_image import GetPhoto
from app.methods.contact_manager import AddNewMessage
from app import app

from .index_view import index
from app.public_views.about.about_view import about
from app.public_views.country.all_country_view import country
from app.public_views.contact.contact_view import contact_us
from app.public_views.city.load_city_view import load_city
from app.public_views.country.load_country_view import load_country
from app.public_views.login.login import user_login
from app.public_views.singin.signin import user_sing_in
from app.public_views.singin.signin_options_view import signin_options
from .singup_or_login_view import login_sing_up_choice
from app.public_views.terms.terms_view import terms
from app.public_views.blog.load_blog_post_view import load_blog_post
from app.public_views.blog.all_blog_posts_view import blog
from app.public_views.sbcscibe_view import sub
from app.public_views.cafe.load_cafe_view import load_cafe
from app.public_views.cafe.follow_unfollow_cafe_view import follow, unfollow
from app.public_views.cafe.vote_view import voting
