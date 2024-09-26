import pytesseract
from PIL import Image

import pandas as pd  


# 设置Tesseract的路径（如果不在系统PATH中）  
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows路径示例  



# OCR识别函数  
def ocr_to_dataframe(image_path):  
    # 使用Pillow库打开图像  
    image = Image.open(image_path)  
      
    # 使用pytesseract进行OCR识别  
    text = pytesseract.image_to_boxes(image,lang='chi_sim')  # 你可以根据需要更改语言代码  
      
    # 在这里，你可能需要编写一些代码来解析文本，并将其转换为结构化数据  
    # 例如，使用正则表达式或字符串分割等方法  
    print(text)  
    # 假设text是一个由逗号分隔的字符串，我们将它分割成一个列表  
    #data = text.split('\n')  
      
    # 将数据转换为DataFrame  
    #df = pd.DataFrame(data)  
    '''
    Tesseract 
    '''
    #return df  
  
# OCR识别并保存为Excel  
def save_ocr_to_excel(image_path, excel_path):  
    ocr_to_dataframe(image_path)  

      
    # 将DataFrame保存为Excel文件  
    #df.to_excel(excel_path, index=False)  
  
# 使用示例  
image_path = r'C:\Users\Administrator\Desktop\微信图片_20240220160554.png'  
excel_path = 'output.xlsx'  
save_ocr_to_excel(image_path, excel_path)
