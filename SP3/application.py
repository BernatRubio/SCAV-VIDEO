import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QStatusBar, QDesktopWidget
from PyQt5.QtCore import QDir
from PyQt5 import QtGui, QtCore
from rescompress import ResCompressor
from widget import Window

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.central_widget = Window()
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Video Operations GUI")
        self.setFixedSize(500, 170)
        self.center_on_screen()
        oImage = QtGui.QImage(os.path.join(CURRENT_DIR, "bgimage.jpg"))
        sImage = oImage.scaled(QtCore.QSize(500, 170))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(sImage))
        self.setPalette(palette)
        
        icon = QtGui.QIcon("./icon.png")  # Replace with the actual path to your icon
        self.setWindowIcon(icon)
        
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("color: white;")
        
        self.central_widget.browse_button.clicked.connect(self.browse_file)
        self.central_widget.execute_button.clicked.connect(self.execute_function)
        
        self.filepath = ""

    
    def center_on_screen(self):
        # Get the screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()
        
        center_x = screen_geometry.width() // 2 - self.width() // 2
        center_y = screen_geometry.height() // 2 - self.height() // 2
        
        self.move(center_x, center_y)
    
    def browse_file(self):
        file_dialog = QFileDialog(self,directory=QDir.homePath())
        file_path, _ = file_dialog.getOpenFileName(self, "Select Video File")

        if file_path:
            self.filepath = file_path
            file_path = file_path.split('/')[-1]
            self.central_widget.label_path.setText(f"{file_path}")
            
    def execute_function(self):
        obj = ResCompressor()
        if (self.filepath == ""):
            self.status_bar.showMessage("No file selected!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Resize" and self.central_widget.resx.text() != "" or self.central_widget.resx.text() != ""):
            if(self.filepath):
                obj.resize(self.filepath,int(self.central_widget.resx.text()), int(self.central_widget.resy.text()))
            else:
                self.status_bar.showMessage("No file selected!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Change Codec" and self.central_widget.codecbox.currentText() != "" and self.filepath):
            obj.changeCodec(self.filepath,self.central_widget.codecbox.itemText(self.central_widget.codecbox.currentIndex()))
        elif (self.central_widget.functionbox.currentText() == ""):
            self.status_bar.showMessage("No function selected!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Change Codec" and self.central_widget.codecbox.currentText() == ""):
            self.status_bar.showMessage("No codec selected!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Change Codec" and self.central_widget.codecbox.currentText() != "" and self.filepath == ""):
            self.status_bar.showMessage("No file selected!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Compare Codecs" and self.central_widget.codecbox1.currentText() != "" and self.central_widget.codecbox2.currentText() != "" and self.filepath):
            obj.compareCodecs(self.filepath,self.central_widget.codecbox1.currentText(),self.central_widget.codecbox2.currentText())
        elif (self.central_widget.functionbox.currentText() == "Resize" and (self.central_widget.resx.text() == "" or self.central_widget.resx.text() == "")):
            self.status_bar.showMessage("Resx and Resy must be defined!", 3000)
        elif (self.central_widget.functionbox.currentText() == "Compare Codecs" and (self.central_widget.codecbox1.currentText() == "" or self.central_widget.codecbox2.currentText() == "")):
            self.status_bar.showMessage("Codec 1 and Codec 2 must be chosen!", 3000)