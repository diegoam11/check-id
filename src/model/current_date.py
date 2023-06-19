import datetime

class CurrentDate:
    def get_current_date(self):
        current_date = datetime.date.today()
        return current_date

    def get_current_time(self):
        current_time = datetime.datetime.now()
        return current_time
