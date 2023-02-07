import schedule, time, threading
from utils.subscriber import reset_subscriptions

def resetauto():
    schedule.every(30).days.at("00:00").do(reset_subscriptions)


scheduler_thread = threading.Thread(target=resetauto)
scheduler_thread.start()