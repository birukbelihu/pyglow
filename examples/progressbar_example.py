import time
from pyglow.views.progressbar import ProgressBar


def main():
    progress = ProgressBar(
        total=100,
        width=30,
        color="#145BC7"
    )

    # Simulate some work

    for i in range(101):
        progress.update(i)
        time.sleep(0.05)

    # Stop the progressbar when done

    progress.finish()


if __name__ == "__main__":
    main()
