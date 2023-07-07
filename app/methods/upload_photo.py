import os
from io import BytesIO
import requests
from PIL import Image
from .get_image import GetPhoto
from app.config import Config
from uuid import uuid4
from app.extentions import db
from app.my_db_models.user_model import User


class UploadPhoto:
    def __init__(self):
        self.image_path = None

    def upload_cafe_image(self, cafe_image):
        filename = f'{str(uuid4())}.jpg'
        with Image.open(cafe_image) as new_image:
            new_image.save(os.path.join(Config.UPLOADS_PATH_CAFE, filename))
            self.image_path = f"upload/cafe/{filename}"

        return self.image_path

    def upload_photo_blog_post(self):
        title = f'{str(uuid4())}.jpg'
        img = GetPhoto(search_object="cafe")
        post_image = img.final[0]
        response = requests.get(post_image)
        with Image.open(BytesIO(response.content)) as new_image:
            new_image.save(os.path.join(Config.UPLOADS_PATH_BLOG, title))
            self.image_path = f"upload/blog/{title}"

        return self.image_path

    def upload_user_image(self, user_image, user_id: int):
        user = db.session.query(User).filter_by(id=user_id).first()
        if user:
            if user.image:
                file = user.image.replace('upload/user/', '')
                os.remove(os.path.join(Config.UPLOADS_PATH_USER, file))
        filename = f'{str(uuid4())}.jpg'
        with Image.open(user_image) as new_image:
            new_image.save(os.path.join(Config.UPLOADS_PATH_USER, filename))
            self.image_path = f"upload/user/{filename}"

        return self.image_path
