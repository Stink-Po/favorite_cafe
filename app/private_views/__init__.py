from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_required, current_user, logout_user, login_user
from app.methods.decorators import admin_only
from app.methods.cafe_manager import CafeManager
from app.methods.database_methods import DataBaseInfo
from app.methods.get_image import GetPhoto
from app.methods.send_mail import EmailSender, ConfirmEmail, SendForgotPasswordEmail
from app import app

from app.private_views.logout.logout import log_out
from app.private_views.new_cafe.add_new_cafe_view import add_cafe
from app.private_views.send_confirm.send_confirm_email_view import send_conformation, confirm_email
from app.private_views.rest_password.rest_password_view import check_user_email
from app.private_views.user_dashboard_view import load_dashboard
from app.private_views.chnage_email_view import change_email
from app.private_views.change_password_view import check_pass
from app.private_views.generate_api_key import create_key
