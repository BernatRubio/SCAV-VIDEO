import sys
from PyQt5.QtWidgets import QApplication
from application import MyApp

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec_()) 