import os
from dotenv import load_dotenv, find_dotenv
from groq import Groq

# স্বয়ংক্রিয়ভাবে যেখানেই .env থাকুক খুঁজে বের করবে
load_dotenv(find_dotenv())

# API Key লোড করা
api_key = os.getenv("GROQ_API_KEY")

# Groq Client তৈরি
client = Groq(api_key=api_key)

# AI-কে প্রশ্ন পাঠানো
response = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "তুমি একজন অভিজ্ঞ টেক এক্সপার্ট। সংক্ষেপে ও পয়েন্ট আকারে উত্তর দেবে।"},
        {"role": "user", "content": "২০ হাজার টাকার মধ্যে সেরা ফোনগুলোর একটি তালিকা দাও।"}
    ],
    model="llama-3.3-70b-versatile"
)

# উত্তর প্রিন্ট করা
print("--- AI Response ---")
print(response.choices[0].message.content)