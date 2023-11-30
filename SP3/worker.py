from PyQt5.QtCore import QObject, pyqtSignal, QRunnable, pyqtSlot

class WorkerSignals(QObject):
    update_status = pyqtSignal(str)

class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        try:
            # Before running the function, emit a signal to update the status bar
            self.signals.update_status.emit("Executing...")

            # Run the specified function
            self.fn(*self.args, **self.kwargs)

            # After completion, emit a signal to update the status bar
            self.signals.update_status.emit("Execution completed successfully!")
        except Exception as e:
            # If an exception occurs, emit a signal with the error message
            self.signals.update_status.emit(f"Error: {str(e)}")