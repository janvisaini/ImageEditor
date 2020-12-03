from PIL import Image,ImageEnhance
import time

class ManualEdits:
	def __init__(self,image):
		self.image=image
		
	def Brightness(self,value):
		initail=ImageEnhance.Brightness(self.image)
		final=initail.enhance(value)
		return final

	def Sharpness(self,value):
		initail=ImageEnhance.Sharpness(self.image)
		final=initail.enhance(value)
		return final		
	
	def Color(self,value):
		initail=ImageEnhance.Color(self.image)
		final=initail.enhance(value)
		return final

	def Contrast(self,value):
		initail=ImageEnhance.Contrast(self.image)
		final=initail.enhance(value)
		return final


class Save:
	def __init__(self,image,path,originalSize):
		new_image=image.resize((int(originalSize[0]),int(originalSize[1])),Image.ANTIALIAS)
		new_image.save(path+str(time.time()).replace(".","")+".jpg")



