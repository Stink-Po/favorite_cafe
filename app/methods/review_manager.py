from app.my_db_models.reviewes_model import Reviews
from app.extentions import db


class ManageReview:
    def __init__(self):
        self.review = None

    def add_review(self, text, review_author, parent_cafe):
        try:
            self.review = Reviews(
                text=text,
                review_author=review_author,
                parent_cafe=parent_cafe,
            )
            db.session.add(self.review)
            db.session.commit()
            return self.review

        except Exception as e:
            db.session.rollback()
            return e.args
