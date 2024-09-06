
import google.generativeai as genai
import os
import PIL.Image

genai.configure(api_key=os.environ["API_KEY"])

sample_file = genai.upload_file(path="jetpack.jpg",
                            display_name="Jetpack drawing")

sample_file_2 = PIL.Image.open('piranha.jpg')
sample_file_3 = PIL.Image.open('firefighter.jpg')

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Write an advertising jingle showing how the product in the first image could solve the problems shown in the second two images."

response = model.generate_content([prompt, sample_file, sample_file_2, sample_file_3])

#Markdown(">" + response.text)

print(response.text)


# Choose a Gemini model.
# model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Return a bounding box for the piranha. \n [ymin, xmin, ymax, xmax]"
response = model.generate_content([sample_file_2, prompt])

print(response.text)


'''
# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

prompt = "Return a bounding box for the piranha. \n [ymin, xmin, ymax, xmax]"
response = model.generate_content([piranha, prompt])

print(response.text)

'''
