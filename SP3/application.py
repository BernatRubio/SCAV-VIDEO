import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QComboBox, QStatusBar, QDesktopWidget, QLineEdit
from PyQt5.QtGui import QIntValidator
from rescompress import ResCompressor

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Browser")
        self.setFixedSize(450,280)
        self.center_on_screen()

        self.label = QLabel("Input File: ", self)
        self.label.setGeometry(20, 20, 600, 30)
        
        self.label_function = QLabel("Select Function: ", self)
        self.label_function.setGeometry(20, 100, 600, 30)
        
        self.label_codec = QLabel("Select Codec: ", self)
        self.label_codec.setGeometry(20, 150, 600, 30)

        self.browse_button = QPushButton("Browse File", self)
        self.browse_button.setGeometry(20, 60, 80, 30)
        self.browse_button.clicked.connect(self.browse_file)
        
        self.combobox = QComboBox(self)
        self.combobox.addItems(["","Resize", "Change Codec"])
        self.combobox.setGeometry(120,100,300,30)
        
        self.codecbox = QComboBox(self)
        self.codecbox.addItems(["","vp8", "vp9", "h265", "av1"])
        self.codecbox.setGeometry(120,150,300,30)
        
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("color: red;")
        
        self.execute_button = QPushButton("Execute", self)
        self.execute_button.setGeometry(20, 200, 80, 30)
        self.execute_button.clicked.connect(self.execute_function)
        
        self.resx = QLineEdit(self)
        self.resx.setGeometry(20, 250, 80, 30)
        self.resx.setValidator(QIntValidator(100, 7680, self))
        
        self.resy = QLineEdit(self)
        self.resy.setGeometry(100, 250, 80, 30)
        self.resy.setValidator(QIntValidator(100, 4320, self))
        
    def center_on_screen(self):
        # Get the screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()
        
        center_x = screen_geometry.width() // 2 - self.width() // 2
        center_y = screen_geometry.height() // 2 - self.height() // 2
        
        self.move(center_x, center_y)

    def browse_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Select Video File")

        if file_path:
            self.label.setText(f"Input File: {file_path}")
            
    def execute_function(self):
        obj = ResCompressor()
        if (self.combobox.currentText() == "Resize"):
            if((self.label.text()).split("Input File: ",1)[1]):
                obj.resize((self.label.text()).split("Input File: ",1)[1],720, 480)
            else:
                self.status_bar.showMessage("No file selected!", 3000)
        elif (self.combobox.currentText() == "Change Codec" and self.codecbox.currentText() != "" and (self.label.text()).split("Input File: ",1)[1]):
            obj.changeCodec((self.label.text()).split("Input File: ",1)[1],self.codecbox.itemText(self.codecbox.currentIndex()))
        elif (self.combobox.currentText() == ""):
            self.status_bar.showMessage("No function selected!", 3000)
        elif (self.combobox.currentText() == "Change Codec" and self.codecbox.currentText() == ""):
            self.status_bar.showMessage("No codec selected!", 3000)
        elif (self.combobox.currentText() == "Change Codec" and self.codecbox.currentText() != "" and (self.label.text()).split("Input File: ",1)[1] == ""):
            self.status_bar.showMessage("No file selected!", 3000)
            
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
