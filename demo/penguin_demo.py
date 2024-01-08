import os

from PIL import Image
from loguru import logger

from funcaptcha_challenger import predict_penguin

this_dir = os.path.dirname(os.path.realpath(__file__))

image_path = os.path.join(this_dir, 'captcha-images', 'penguin',
                          '0b5bea73081263debe1ccb062816800b285355acf3edd57dea115a62c44ec244_1.jpg')

image = Image.open(image_path)

index = predict_penguin(image)
logger.info(f"Predicted index: {index}")
