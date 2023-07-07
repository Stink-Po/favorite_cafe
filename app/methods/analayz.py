from app.my_db_models.website_analayz import Analyzer
from app.extentions import db


class AnalyzeManager:
    def __init__(self):
        self.start()

    @staticmethod
    def start():

        new_view_count = Analyzer.query.first()

        if new_view_count:

            new_view_count.total_view += 1
            new_view_count.today_view += 1

        else:
            new_view_count = Analyzer(total_view=1,
                                      today_view=1)

            db.session.add(new_view_count)

        db.session.commit()
