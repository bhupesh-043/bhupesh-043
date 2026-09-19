import threading
import time

def download():
    print("Downloading...")
    time.sleep(3)
    print("Download completed")


def send_email():
    print("Sending email...")
    time.sleep(2)
    print("Email sent")


t1 = threading.Thread(target=download)
t2 = threading.Thread(target=send_email)

t1.start()
t2.start()

t1.join()
t2.join()