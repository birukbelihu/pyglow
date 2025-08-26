import time
import threading
from pyglow.views.spinner import Spinner

spinner = Spinner(prefix="Loading please wait", bar_color="#FFFFFFF", delay=0.1)

t = threading.Thread(target=spinner.start)
t.start()

# Simulate some work
for i in range(1, 3):
    time.sleep(1)

# Stop the spinner when done
spinner.stop()
