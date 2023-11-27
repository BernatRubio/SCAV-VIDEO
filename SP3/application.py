import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QComboBox, QStatusBar
from PyQt5.QtCore import Qt
from rescompress import ResCompressor

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Browser")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Input File: ", self)
        self.label.setGeometry(20, 20, 600, 30)

        self.browse_button = QPushButton("Browse", self)
        self.browse_button.setGeometry(20, 60, 80, 30)
        self.browse_button.clicked.connect(self.browse_file)
        
        self.combobox = QComboBox(self)
        self.combobox.addItems(["Resize", "Change Codec"])
        self.combobox.setGeometry(20,100,300,30)
        
        self.combobox.activated[str].connect(self.combobox_function)
        
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("color: red;")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
