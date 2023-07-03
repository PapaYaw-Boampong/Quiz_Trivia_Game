from time import sleep


class Timer:
    def __init__(self):
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.has_hours = False

    def increment(self):

        if self.min >= 60:
            self.hour+=1
            if  not self.has_hours:
                self.has_hours = True
        if self.sec == 60:
            self.min += 1
            self.sec = 0
        elif self.sec < 60:
            self.sec += 1

    def reset_timer(self):
        self.sec = 0
        self.min = 0

    def format_time(self):
        if self.has_hours:
            if self.hour < 10:
                hour = f"0{self}"
            else:
                hour = f"{self}"
        else:
            hour = ""
        if self.sec < 10:
            seconds = f"0{self.sec}"
        else:
            seconds = f"{self.sec}"
        if self.min < 10:
            minutes = f"0{self.min}"
        else:
            minutes = f"{self.min}"
        if self.has_hours:
            return f"{hour}:{minutes}:{seconds}"
        return f"{minutes}:{seconds}"

    def update_clock(self, quiz, timer_label, window):
        self.increment()
        formatted_time = self.format_time()
        timer_label.config(text=f"{formatted_time}")
        if quiz.has_question:
            window.after(1000, lambda: self.update_clock(quiz, timer_label, window))
