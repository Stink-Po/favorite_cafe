from datetime import datetime


class Time:
    """Create formatted time for  using in project"""
    def __init__(self):
        self.formatted_time = None
        self.unix_time = None
        self.now_formatted_time()
        self.get_unix_time()

    def now_formatted_time(self):
        """
        create formatted time
        :return: string formatted time day month year
        """
        self.formatted_time = str(datetime.utcnow().strftime("%d %b %Y"))
        return self.formatted_time

    def get_unix_time(self):
        self.unix_time = int(datetime.now().timestamp())
        return self.unix_time
