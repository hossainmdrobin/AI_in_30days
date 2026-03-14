from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(model_id)

pipe = pipe.to("cpu")

prompt = input("Enter image prompt: ")

image = pipe(
    prompt,
    height=512,
    width=512,
    num_inference_steps=30
).images[0]

image.save("output/generated.png")

print("Image saved to output/generated.png")