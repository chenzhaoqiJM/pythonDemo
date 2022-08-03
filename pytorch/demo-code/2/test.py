import torchvision.transforms
from PIL import Image
import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential

image_path="dog.png"
img=Image.open(image_path)
# print(img)
img=img.convert('RGB')
# print(img)
transform=torchvision.transforms.Compose([torchvision.transforms.Resize((32,32)),torchvision.transforms.ToTensor()])
img1=transform(img)
# print(img1)


class zhao(nn.Module):
	def __init__(self):
		super(zhao, self).__init__()
		self.model1=Sequential(
			Conv2d(3, 32, 5, padding=2),
			MaxPool2d(2),
			Conv2d(32, 32, 5, padding=2),
			MaxPool2d(2),
			Conv2d(32, 64, 5, padding=2),
			MaxPool2d(2),
			Flatten(),
			Linear(1024, 64),
			Linear(64, 10)
		)

	def forward(self, input):
		output=self.model1(input)
		return output

zhao = zhao()
if __name__ == '__main__':
	# model = zhao()
	# model.load_state_dict(torch.load("zhao_10.pth"))
	mymodel = torch.load("zhao_10.pth")
 
	print(mymodel)
	img2=torch.reshape(img1,(1,3,32,32))
 
	mymodel.eval()
	print(img2.shape)
	with torch.no_grad():
		output=mymodel(img2)
	print(output)




