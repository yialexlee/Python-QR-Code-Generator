from io import BytesIO
import qrcode

def Generate_QR_Image(Text, Fill_Color="#000000", Background_Color="#ffffff", File_Format="JPEG"):

    QR_Manager = qrcode.QRCode(  
        version=None,  
        error_correction=qrcode.constants.ERROR_CORRECT_M,  
        box_size=10,  
        border=2)     

    QR_Manager.add_data(Text)   
    QR_Manager.make(fit=True)   

    QR_Image = QR_Manager.make_image(fill_color=Fill_Color, back_color=Background_Color)  

    Buffered = BytesIO()  
    QR_Image.save(Buffered, format=File_Format)  

    return Buffered.getvalue()  
