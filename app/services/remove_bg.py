from PIL import Image
import requests
from io import BytesIO
from rembg import remove
import base64

def remove_bg_of_img(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    output = remove(img)
    out_stream = BytesIO()
    output.save(out_stream, format="PNG")
    image_data = out_stream.getvalue()
    base64_image = base64.b64encode(image_data).decode('utf-8')
    return base64_image
