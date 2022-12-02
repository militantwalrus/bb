from __future__ import annotations

import signal


class CaughtSignal(Exception):
    """
    Wrap a signal as an Exception class
    """

    def __init__(self, signum):
        """
        Constructor
        """
        self.signum = signum


class SignalHandler:
    """
    Signal handler as context manager
    """

    def __init__(self):
        """
        Constructor
        """
        pass

    def __enter__(self):
        """
        Context manager __enter__
        """

        def handler(signum, frame):
            raise CaughtSignal(signum)

        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)

    def __exit__(self, exception, value, traceback):
        """
        Context manager __exit__
        """
        pass
