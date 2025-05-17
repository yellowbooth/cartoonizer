from flask import Flask, request, jsonify
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
from io import BytesIO
import requests
import os

app = Flask(__name__)

# Load the model once (on server start)
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16
).to("cuda")

@app.route("/cartoonize", methods=["POST"])
def cartoonize():
    try:
        image_url = request.json.get("image")
        if not image_url:
            return jsonify({"error": "Missing 'image' in request"}), 400

        prompt = "a cartoon portrait of a wedding couple, disney style, smooth shading, colorful"
        image = pipe(prompt).images[0]

        output_path = "/app/output.png"
        image.save(output_path)

        return jsonify({"output": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200
