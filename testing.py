from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://media.istockphoto.com/id/1463013729/photo/online-registration-form-for-modish-form-filling.jpg?s=1024x1024&w=is&k=20&c=EHI3hS1rXOMpRmM1LKEV8zxwYBFEkU-TqffuKtoBPC4=')
img = Image.open(BytesIO(response.content))

print(img.shape)