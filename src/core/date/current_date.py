import datetime

class CurrentDate:
    def get_current_date(self):
        current_date = datetime.date.today()
        return current_date

    def get_current_time(self):
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M")  # Formato HH:MM
        return current_time
