import json
from django.shortcuts import render
from decouple import config
import openai

openai.api_key = config("OPENAI_API_KEY")


def generate_colors(text):
    prompt = """
    You are an assistant that answer to text prompts for color palletes.
    You must generate color palletes that fit the instructions.
    The palletes should be between 2 and 8.
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {
                "role": "user",
                "content": "Google's Brand",
            },
            {
                "role": "assistant",
                "content": '["#4285F4", "#DB4437", "#F4B400", "#0F9D58"]',
            },
            {
                "role": "user",
                "content": "the ocean",
            },
            {
                "role": "assistant",
                "content": '["#064273", "#76b6c4", "#7fcdff", "#1da2d8", "#def3f6"]',
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )

    return json.loads(response.choices[0].message.content)


def index(request):
    return render(request, "index.html")


def colors(request):
    text = request.POST.get("text")
    colors = generate_colors(text)
    return render(request, "colors.html", {"colors": colors})
