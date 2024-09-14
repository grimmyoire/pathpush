import requests

# Hugging Face API Key
API_KEY = "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"

# Blog Post Topic
blog_topic = "Latest Innovations in AI Technology"

# Hugging Face API URL
API_URL = "https://api-inference.huggingface.co/models/gpt-neo-2.7B"

# Headers for the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Data payload to generate text
data = {
    "inputs": f"Write a blog post about {blog_topic}",
}

# Send request to Hugging Face API
response = requests.post(API_URL, headers=headers, json=data)
response_json = response.json()

# Extract and save the generated blog post
blog_post = response_json[0]["generated_text"]
print(f"Generated Blog Post: \n\n{blog_post}")

# Save blog post to a text file
with open("latest_tech_blog.txt", "w") as file:
    file.write(blog_post)
