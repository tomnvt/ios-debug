from iosdebug.stop import stop
from iosdebug.start import start

if os.environ['ENABLE_PREVIEWS'] == "YES":
    raise SystemExit

stop(update_project=False)
start(update_project=False)