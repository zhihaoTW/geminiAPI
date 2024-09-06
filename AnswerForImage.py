
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])


# Upload the file and print a confirmation.
sample_file = genai.upload_file(path="jetpack.jpg",
                            display_name="Jetpack drawing")

print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")

file = genai.get_file(name=sample_file.name)
print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")


# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Prompt the model with text and the previously uploaded image.
response = model.generate_content([sample_file, "Describe how this product might be manufactured."])

print(response.text)

#Markdown(">" + response.text)

'''
import PIL.Image

sample_file_2 = PIL.Image.open('piranha.jpg')
sample_file_3 = PIL.Image.open('firefighter.jpg')

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Write an advertising jingle showing how the product in the first image could solve the problems shown in the second two images."

response = model.generate_content([prompt, sample_file, sample_file_2, sample_file_3])

Markdown(">" + response.text)
'''


'''
# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Return a bounding box for the piranha. \n [ymin, xmin, ymax, xmax]"
response = model.generate_content([piranha, prompt])

print(response.text)

'''
