import time
from pyler import notification

if __name__ == "__main__":
    while true:
        notification.notify(
            title = "Alert!!",
            message = "You need to take a break!!",
            time = 10
        )
        time.sleep(3600)
