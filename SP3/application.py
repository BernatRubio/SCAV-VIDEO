from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStatusBar, QDesktopWidget
from PyQt5.QtCore import QDir, QThreadPool, QTimer
from PyQt5 import QtGui, QtCore
from rescompress import ResCompressor
from widget import Window
from worker import Worker

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.central_widget = Window()
        self.setCentralWidget(self.central_widget)

        self.setWindowTitle("Video Operations GUI")
        self.screen_geometry = QDesktopWidget().screenGeometry()
        self.setFixedSize(self.screen_geometry.width() // 3, self.screen_geometry.height() // 3)
        self.center_on_screen()

        self.movie = QtGui.QMovie("./assets/wallpaper.webp")
        self.movie.setScaledSize(QtCore.QSize(self.screen_geometry.width() // 3, self.screen_geometry.height() // 3))
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()
        
        icon = QtGui.QIcon("./assets/icon.png")
        self.setWindowIcon(icon)
        
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.setStyleSheet("color: white;")
        
        self.central_widget.browse_button.clicked.connect(self.browse_file)
        self.central_widget.browse_folder_button.clicked.connect(self.browse_folder)
        self.central_widget.execute_button.clicked.connect(self.execute_function)
        
        self.filepath = ""
        self.outfilepath = ""
        
        self.threadpool = QThreadPool()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_threadpool)
        self.timer.start(1000)
    
    
    def center_on_screen(self):
        
        center_x = self.screen_geometry.width() // 2 - self.width() // 2
        center_y = self.screen_geometry.height() // 2 - self.height() // 2
        
        self.move(center_x, center_y)
    
    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QtGui.QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
    
    def browse_file(self):
        file_dialog = QFileDialog(self,directory=QDir.homePath())
        file_path, _ = file_dialog.getOpenFileName(self, "Select Video File")

        if file_path:
            self.filepath = file_path
            file_path = file_path.split('/')[-1]
            self.central_widget.label_path.setText(f"{file_path}")
    
    def browse_folder(self):
        outfilepath = QFileDialog.getExistingDirectory(self, "Select Directory", QDir.homePath())

        if outfilepath:
            self.outfilepath = outfilepath
            self.central_widget.label_path_output.setText(f"{outfilepath}")
            
    def check_threadpool(self):
        # Update the status bar based on the number of active threads
        if self.threadpool.activeThreadCount() > 0:
            self.status_bar.showMessage(f"Executing...", 1000)
                   
    def execute_function(self):
        obj = ResCompressor()
        
        if (self.filepath == ""):
            self.status_bar.showMessage("No file selected!", 3000)
        
        elif (self.outfilepath == ""):
            self.status_bar.showMessage("Select output directory!", 3000)
        
        elif (self.central_widget.functionbox.currentText() == ""):
            self.status_bar.showMessage("No function selected!", 3000)
        
        elif (self.central_widget.functionbox.currentText() == "Resize" and self.central_widget.resx.text() != "" and self.central_widget.resy.text() != ""):
            worker = Worker(obj.resize, self.filepath,int(self.central_widget.resx.text()), int(self.central_widget.resy.text()),self.outfilepath)
            self.threadpool.start(worker)
        
        elif (self.central_widget.functionbox.currentText() == "Resize" and (self.central_widget.resx.text() == "" or self.central_widget.resy.text() == "")):
            self.status_bar.showMessage("Resx and Resy must be defined!", 3000)

        elif (self.central_widget.functionbox.currentText() == "Change Codec" and self.central_widget.codecbox.currentText() != ""):
            worker2 = Worker(obj.changeCodec, self.filepath,self.central_widget.codecbox.itemText(self.central_widget.codecbox.currentIndex()),self.outfilepath)
            self.threadpool.start(worker2)
        
        elif (self.central_widget.functionbox.currentText() == "Change Codec" and self.central_widget.codecbox.currentText() == ""):
            self.status_bar.showMessage("No codec selected!", 3000)
        
        elif (self.central_widget.functionbox.currentText() == "Compare Codecs" and self.central_widget.codecbox1.currentText() != "" and self.central_widget.codecbox2.currentText() != ""):
            worker3 = Worker(obj.compareCodecs, self.filepath,self.central_widget.codecbox1.currentText(),self.central_widget.codecbox2.currentText(),self.outfilepath)
            self.threadpool.start(worker3)
        
        elif (self.central_widget.functionbox.currentText() == "Compare Codecs" and (self.central_widget.codecbox1.currentText() == "" or self.central_widget.codecbox2.currentText() == "")):
            self.status_bar.showMessage("Codec 1 and Codec 2 must be chosen!", 3000)