from app.my_db_models import UserCafe
from app.extentions import db


class FollowManager:
    def __init__(self, user, cafe):
        """

        :param user: a user object
        :param cafe: a cafe object
        """
        self.cafe = cafe
        self.user = user
        self.following = False
        self.is_following()

    def follow(self) -> None:
        following = UserCafe(
            user=self.user,
            cafe=self.cafe
        )
        db.session.add(following)
        db.session.commit()

    def unfollow(self) -> None:
        unfollowing = db.session.query(UserCafe).filter_by(user_id=self.user.id, cafe_id=self.cafe.id).first_or_404()
        db.session.delete(unfollowing)
        db.session.commit()

    def is_following(self):
        if db.session.query(UserCafe).filter_by(user_id=self.user.id, cafe_id=self.cafe.id).first():
            self.following = True
        return self.following


