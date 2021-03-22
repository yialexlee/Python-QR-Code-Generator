import sys
from qr_generate import Generate_QR_Image
from gui_hexrgb import Hex_To_RGB, Hex_To_RGBA
from PyQt5.QtWidgets import QGraphicsDropShadowEffect  
from PyQt5.QtWidgets import QApplication, QDesktopWidget  
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QFileDialog  
from PyQt5.QtGui import QIcon, QPixmap  
from PyQt5.QtGui import QPainter, QBrush, QColor  
from PyQt5.QtGui import QFontDatabase  
from PyQt5.QtCore import Qt  
from PyQt5.QtCore import QRect, QSize  


def Main():  

    App = QApplication(sys.argv)   
    Main_Window = Window()          
    sys.exit(App.exec())            

class Window(QWidget):

    def __init__(self):

        super().__init__()

        ScreenGeometry = QDesktopWidget().screenGeometry()
        Window_Resolution = 9/16

        self.Title = "二维码生成器"

        self.Width = ScreenGeometry.width() / 1.5
        self.Height = self.Width * Window_Resolution

        self.Left = (ScreenGeometry.width() - self.Width) / 2
        self.Top = (ScreenGeometry.height() - self.Height) / 2

        self.InitWindow()

    def InitWindow(self):

        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle(self.Title)
        self.setGeometry(self.Left, self.Top, self.Width, self.Height)

        self.setStyleSheet('''
                                    Window {
                                                background: QLinearGradient(x1:0,y1:0,x2:1,y2:1,stop:0 #082c6c,stop: .9 #2069e0, stop: 1 #1365eb);
                                        }                     
                            ''')

        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus(True)

        self.setFixedSize(self.Width, self.Height)

        self.show()

        self.On_Window_Loaded()

    def On_Window_Loaded(self):

        if (True):  

           QFontDatabase().addApplicationFont("./Assets/Fonts/Cabin-Bold.ttf")

        if (True): 

            self.GUI_Labels()

            self.GUI_LineEdits()

            self.GUI_Buttons()

            self.GUI_Images()

        if (True):  

            self.Show_QR_Image('https://yialexlee.tk/')

    def GUI_Labels(self):

        if (True):  

           Labels = [
                {'Text': '二维码生成器',
                    'Left': self.Width * 0.07, 'Top': self.Height * 0.18,
                 'Font_Size': int(self.Height * 0.14),
                 'Text_Color': Hex_To_RGBA("#ffffff", 1)},
                {'Text': '一键生成二维码',
                 'Left': self.Width * 0.08, 'Top': self.Height * 0.35,
                 'Font_Size': int(self.Height * 0.03),
                 'Text_Color': Hex_To_RGBA("#ffffff", 1)}]

        if (True):

            for Label_Data in Labels:

                StyleSheet = ('''
                                    QLabel{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                    }}
                                    ''').format(**Label_Data)

                Label = QLabel(Label_Data.get('Text'), self)  
                Label.setStyleSheet(StyleSheet)  
                Label.move(Label_Data.get('Left'), Label_Data.get('Top'))  
                Label.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)) 

                Label.show()  

    def GUI_LineEdits(self):

        if (True): 

            LineEdits = [
                {'PlaceHolder_Text': '输入链接或文本',
                 'Left': self.Width*0.07, 'Top': self.Height*0.56,
                 'Width': self.Width*0.25, 'Height': self.Height*0.10,
                 'Font_Size': int(self.Height*0.03),
                 'Padding_Left': self.Height*0.03, 'Padding_Right': self.Height*0.03,
                 'Text_Color': Hex_To_RGBA("#000000", 0.8),
                 'Background_Color': Hex_To_RGBA("#ffffff", 0.4),
                 'Round': self.Height*0.05}]

        if (True):  

            for LineEdit_Data in LineEdits:

                StyleSheet = ('''
                                    QLineEdit{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                        padding-left: {Padding_Left}px;
                                        padding-right: {Padding_Right}px;
                                        background-color: rgba{Background_Color};
                                        border-radius: {Round}px;

                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}
                                    ''').format(**LineEdit_Data)

                self.LineEdit = QLineEdit(self)
                self.LineEdit.setPlaceholderText(LineEdit_Data.get('PlaceHolder_Text'))
                self.LineEdit.setStyleSheet(StyleSheet)  
                self.LineEdit.move(LineEdit_Data.get('Left'), LineEdit_Data.get('Top')) 
                self.LineEdit.show()

    def GUI_Buttons(self):

        if (True):  
                Buttons = [
                {'Text': '生成二维码',
                 'Left': self.Width*0.39, 'Top': self.Height*0.56,
                 'Width': self.Width*0.25, 'Height': self.Height*0.10,
                         'Font_Size': int(self.Height*0.03),
                 'Text_Color': Hex_To_RGBA("#ffffff", 0.9),
                 'Background_Color': Hex_To_RGBA("#01000a", 0.9),
                 'Hover_Background_Color': Hex_To_RGBA("#01000a", 0.9),
                 'Pressed_Background_Color': Hex_To_RGBA("#01000a", 0.9),
                 'Round_Top_Left': self.Height*0.05, 'Round_Top_Right': self.Height*0.05,
                 'Round_Bottom_Left': 0, 'Round_Bottom_Right': self.Height*0.05,
                         'Object_Name': 'Generate QR'},
                {'Text': '保存二维码',
                 'Left': self.Width*0.7, 'Top': self.Height*0.61,
                 'Width': self.Height*0.38, 'Height': self.Height*0.05,
                         'Font_Size': int(self.Height*0.03),
                         'Text_Color': Hex_To_RGBA("#ffffff", 1),
                         'Background_Color': Hex_To_RGBA("#ffffff", 0.25),
                         'Hover_Background_Color': Hex_To_RGBA("#ffffff", 0.15),
                         'Pressed_Background_Color': Hex_To_RGBA("#ffffff", 0.4),
                 'Round_Top_Left': 0, 'Round_Top_Right': 0,
                 'Round_Bottom_Left': self.Height*0.05, 'Round_Bottom_Right': self.Height*0.05,
                         'Image': 'Assets/Images/download-white-64x64.png',
                 'Image_Width': self.Height*0.025, 'Image_Height': self.Height*0.025,
                         'Object_Name': 'Download'}]
		

        if (True):  

            for Button_Data in Buttons:

                StyleSheet = ('''
                                    QPushButton{{
                                        font-size: {Font_Size}px;
                                        font-family: Cabin;
                                        color: rgba{Text_Color};
                                        background-color: rgba{Background_Color};
                                        
                                        border-top-left-radius: {Round_Top_Left}px;
                                        border-top-right-radius: {Round_Top_Right}px;
                                        border-bottom-left-radius: {Round_Bottom_Left}px;
                                        border-bottom-right-radius: {Round_Bottom_Right}px;

                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}

                                    QPushButton:hover{{
                                        background-color: rgba{Hover_Background_Color};
                                    }}

                                    QPushButton:pressed{{
                                        background-color: rgba{Pressed_Background_Color};
                                    }}
                                    ''').format(**Button_Data)

                Button = QPushButton(Button_Data.get('Text'), self)
                Button.setStyleSheet(StyleSheet)  
                Button.move(Button_Data.get('Left'), Button_Data.get('Top')) 
                Button.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3))  
                Button.clicked.connect(self.on_Click)
                Button.setObjectName(Button_Data.get('Object_Name'))

                if ('Image' in Button_Data):  

                    Button.setIcon(QIcon(Button_Data.get('Image')))
                    Button.setIconSize(QSize(Button_Data.get('Image_Width'), Button_Data.get('Image_Height')))

                Button.show()

    def GUI_Images(self):

        if (True):  

            Images = [
                {'Left': self.Width*0.7, 'Top': self.Height*0.23,
                 'Width': self.Height*0.38, 'Height': self.Height*0.38}]

        if (True):  

            for Image_Data in Images:

                StyleSheet = ('''
                                    QLabel{{
                                        min-width: {Width}px;
                                        max-width: {Width}px;
                                        min-height: {Height}px;
                                        max-height: {Height}px;
                                    }}
                                    ''').format(**Image_Data)

                self.Image = QLabel(self)
                self.Image.setStyleSheet(StyleSheet)  
                self.Image.move(Image_Data.get('Left'), Image_Data.get('Top'))  
                self.Image.setScaledContents(True)
                self.Image.setFixedSize(Image_Data.get('Width'), Image_Data.get('Height'))

                self.Image.show()


    def Show_QR_Image(self, Text):
        '''
            Generating And Showing The QR Code, Based On The Given Text.
        '''

        self.QR_Manager = Generate_QR_Image(Text, File_Format="PNG")  

        Pixmap = QPixmap()
        Pixmap.loadFromData(self.QR_Manager)  

        self.Image.setPixmap(Pixmap)  

    def Save_QR_Image(self):
        '''
            Opening The File Dialog. 
            After The User Clicks "Save", The QR Image Will Be Saved.
        '''

        
        File_Path, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "QR Image", "All Files (*);;PNG Files (*.png);;JPEG Files (*.jpeg)")

        if File_Path:  
            with open(File_Path, 'wb') as File:  
                File.write(self.QR_Manager)


    def on_Click(self):

        
        if (self.sender().objectName() == 'Generate QR'):  

            self.Show_QR_Image(self.LineEdit.text())  

        elif (self.sender().objectName() == 'Download'):  

            self.Save_QR_Image()  





if __name__ == "__main__":

    Main()
