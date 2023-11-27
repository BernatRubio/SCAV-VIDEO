import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QComboBox, QStatusBar, QDesktopWidget
from PyQt5.QtCore import Qt
from rescompress import ResCompressor
import time

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Browser")
        self.setFixedSize(450,200)
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
        self.combobox.activated[str].connect(self.combobox_function)
        
        self.codecbox = QComboBox(self)
        self.codecbox.addItems(["","vp8", "vp9", "h265", "av1"])
        self.codecbox.setGeometry(120,150,300,30)
        self.codecbox.activated[str].connect(self.codecbox_function)
        
        
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("color: red;")
        
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
    
    def combobox_function(self, item_text):
        if (item_text == "Resize"):
            obj = ResCompressor()
            if((self.label.text()).split("Input File: ",1)[1]):
                obj.resize((self.label.text()).split("Input File: ",1)[1],720, 480)
            else:
                self.status_bar.showMessage("No file selected!", 3000)
        elif (item_text == "Change Codec" and self.codecbox.currentText() != ""):
            obj = ResCompressor()
            obj.changeCodec((self.label.text()).split("Input File: ",1)[1],self.codecbox.itemText(self.codecbox.currentIndex()))
            
    def codecbox_function(self):
        if((self.label.text()).split("Input File: ",1)[1] and self.codecbox.currentText() != "" and self.combobox.currentText() == "Change Codec"):
            obj = ResCompressor()
            obj.changeCodec((self.label.text()).split("Input File: ",1)[1],self.codecbox.itemText(self.codecbox.currentIndex()))
        elif self.codecbox.currentText() == "":
            self.status_bar.showMessage("Select a valid codec!", 2000)
        elif self.combobox.currentText() == "":
            self.status_bar.showMessage("Select the 'Change Codec' function before selecting a codec!", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
