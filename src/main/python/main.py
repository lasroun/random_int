from fbs_runtime.application_context.PySide6 import ApplicationContext
import sys

from package.main_window import MainWindow

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.setWindowTitle("Random Integer")
    window.setFixedSize(500, 400)
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
