import sys
import multiprocessing

import pyinotify


class EventHandler(pyinotify.ProcessEvent):
    """Event handler for changes on disk

    Defines reactions for different events,
    such as:
        modification
        creation
        deletion
    Each event has such parameters:
        maskname: e.g "IN_MODIFY"
        name, path, pathname (actual path with filename),
        directory: is file a directory
    """

    def __init__(self, *args, **kwargs):
        super(EventHandler, self).__init__(*args, **kwargs)

    def process_IN_MODIFY(self, event):
        print "Modifying:", event.pathname

    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname

    def process_IN_DELETE(self, event):
        print "Deleting:", event.pathname


def watch_for_changes(directory):
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY

    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)

    try:
        wdd = wm.add_watch(directory, mask, rec=True)
        notifier.loop()
    finally:
        wm.rm_watch(wdd.values())


def main():
    try:
        directory = sys.argv[1]
        watcher = multiprocessing.Process(target=watch_for_changes,
                                          args=(directory,))
        watcher.start()
    except:
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
