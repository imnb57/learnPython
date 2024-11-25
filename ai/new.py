from transformers import pipeline

# Create a text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Give a more direct instruction to GPT-2 to generate a new story
prompt = "Write a funny story about a cat who opens a bakery."

# Generate the text
generated_text = generator(prompt, max_length=200, num_return_sequences=1)

# Print the generated story
print(generated_text[0]['generated_text'])
