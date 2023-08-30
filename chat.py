import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Dame una lista de proyectos en Python"
        }
    ],
    # maxTokens = 100,
)

print(response)