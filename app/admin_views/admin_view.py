from app.admin_views import *
from app.methods.decorators import admin_only


@app.route("/clear_new_cafe")
@admin_only
def clear_new_cafe():
    counting = Counting()
    counting.clear_cafe_count()
    return redirect(url_for('admin.index'))


@app.route("/clear_subs")
@admin_only
def clear_subs():
    counting = Counting()
    counting.clear_sub_count()
    return redirect(url_for('admin.index'))


@app.route("/clear_users")
@admin_only
def clear_users():
    counting = Counting()
    counting.clear_user_count()
    return redirect(url_for('admin.index'))
