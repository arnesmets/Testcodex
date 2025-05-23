from plyer import notification
import time


def stuur_melding():
    notification.notify(
        title="Tijd voor een korte wandeling",
        message="Sta even op en wandel 1 minuut voor een betere doorbloeding.",
        timeout=10
    )


if __name__ == "__main__":
    while True:
        stuur_melding()
        time.sleep(3600)

