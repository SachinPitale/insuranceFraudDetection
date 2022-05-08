from datetime import datetime


class App_Logger:
    def __init__(self):
        pass

    def log(self,file_object,log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_date = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_date) + "\t\t" + log_message +"\n"
        )
