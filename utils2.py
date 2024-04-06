import openai
openai.api_key = "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"   
def generate_prescription(inputt):
    messages = [{
        "role": "system",
        "content": """Suggest me some medicines and their average dosage to overcome my ailment from the information provided to you.  \n""" 
    }]

    messages.append({"role": "user", "content": f"{inputt}"})

    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = completion.choices[0].message.content
        return reply
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None  # Or handle the error differently