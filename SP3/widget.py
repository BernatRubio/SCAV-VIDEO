from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
    QLabel,
    QComboBox,
    QLineEdit,
    QSizePolicy
)
from PyQt5.QtGui import QIntValidator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        self.label_input = QLabel("Input File: ")
        layout.addWidget(self.label_input,0,0)
        
        self.label_path = QLabel()
        layout.addWidget(self.label_path,0,1)
        
        self.browse_button = QPushButton("Browse File")
        layout.addWidget(self.browse_button,1,0)
        self.browse_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        
        self.label_function = QLabel("Select Function: ")
        self.label_function.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.label_function,2,0)
        
        self.functionbox = QComboBox()
        self.functionbox.addItems(["","Resize", "Change Codec", "Compare Codecs"])
        self.functionbox.activated[str].connect(lambda text: on_functionbox_change(text))
        self.functionbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.functionbox,2,1)

        self.resx = QLineEdit()
        self.resx.setValidator(QIntValidator(100, 7680, self))
        self.resx.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        
        self.resy = QLineEdit()
        self.resy.setValidator(QIntValidator(100, 4320, self))
        self.resy.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
         
        self.execute_button = QPushButton("Execute", self)
        self.execute_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.execute_button,4,0)
        
        
        self.setLayout(layout)
        
        def on_functionbox_change(text):
            # Clear the layout and add self.resx and self.resy if needed
            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setParent(None)
            layout.addWidget(self.label_input,0,0)
            layout.addWidget(self.label_path,0,1)
            layout.addWidget(self.browse_button,1,0)
            layout.addWidget(self.label_function,2,0)
            layout.addWidget(self.functionbox,2,1)
            layout.addWidget(self.execute_button,4,0)
            
            if text == "Resize":
                layout.addWidget(self.resx,3,1)
                labelx = QLabel("Select Res x: ")
                labelx.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                layout.addWidget(labelx,3,0)
                
                layout.addWidget(self.resy,3,3)
                labely = QLabel("Select Res y: ")
                labely.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                layout.addWidget(labely,3,2)
                
            elif text == "Change Codec":  
                label_codec = QLabel("Select Codec: ")
                label_codec.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                layout.addWidget(label_codec,3,0)
                self.codecbox = QComboBox()
                self.codecbox.addItems(["","vp8", "vp9", "h265", "av1"])
                layout.addWidget(self.codecbox,3,1)
                
            elif text == "Compare Codecs":
                label_codec1 = QLabel("Select Codec 1: ")
                label_codec1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                layout.addWidget(label_codec1,3,0)
                self.codecbox1 = QComboBox()
                self.codecbox1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.codecbox1.addItems(["","vp8", "vp9", "h265", "av1"])
                layout.addWidget(self.codecbox1,3,1)
                
                label_codec2 = QLabel("Select Codec 2: ")
                label_codec2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                layout.addWidget(label_codec2,3,2)
                self.codecbox2 = QComboBox()
                self.codecbox2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                self.codecbox2.addItems(["","vp8", "vp9", "h265", "av1"])
                layout.addWidget(self.codecbox2,3,3)