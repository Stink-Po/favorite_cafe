from app.public_views import *
from app.getting_news import NewsService



@app.route('/')
def index():
    service = NewsService()
    if service.check_file():
        if service.check_date():
            data = service.read_news()
        else:
            service.get_response()
            data = service.read_news()
    else:
        service.get_response()
        data = service.read_news()

    data_base_info = DataBaseInfo()
    api_info = ApiInfo()
    try:
        len_cafe = len(data_base_info.all_cafe)
    except TypeError:
        len_cafe = 0
    try:
        len_blog_post = len(data_base_info.all_blog)
    except TypeError:
        len_blog_post = 0

    len_api = api_info.total_api_key

    data_saved = {
        'len_country': data_base_info.all_country,
        'len_api': len_api,
        'len_cafe': len_cafe,
        'len_users': data_base_info.all_users,
        'len_blog': len_blog_post,
    }
    if current_user.is_authenticated:
        data_base_info.get_followed_cafes(user_id=current_user.id)
        cafe_list = data_base_info.all_following_cafe
    last_blog_posts = data_base_info.ret_last_posts()
    last_cafe = data_base_info.ret_last_cafe()
    img = GetPhoto(search_object='cafe')
    images = img.final
    return render_template("public/index.html",
                           user=current_user,
                           title="Favorite cafe",
                           images=images,
                           data_saved=data_saved,
                           last_blog_posts=last_blog_posts,
                           last_cafe=last_cafe,
                           news=data)
