import runpod
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import requests
from io import BytesIO

# Load model once on cold start
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

def cartoonize(image_url):
    prompt = "a cartoon portrait of a wedding couple, disney style, smooth shading, colorful"
    image = pipe(prompt=prompt).images[0]
    image.save("/tmp/cartoon.png")
    return "/tmp/cartoon.png"

def handler(event):
    image_url = event['input'].get('image')
    if not image_url:
        return {"error": "Missing image URL"}

    cartoon_path = cartoonize(image_url)
    return {"output": cartoon_path}
