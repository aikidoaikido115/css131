from Project import app
from Project.Config import Channel_access_token
import time
from Add_ons.add_ons import Broadcast



import threading


time_set = ['09:00']
def timer():
    while True:
        real_time = time.strftime('%H:%M')
        if real_time in time_set:
            data = "fool"
            Broadcast(data, Channel_access_token)
            time.sleep(70)

        time.sleep(0.25)

thread = threading.Thread(target=timer)
thread.start()

if __name__ == '__main__':
    app.run(port = 5000)