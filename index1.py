import google.generativeai as genai

# Set your API key here
genai.configure(api_key="AIzaSyBIgG1KtXvIqwlmcvwAxxqxZ_FiHn4FwWQ")

# List all available models for your key
models = genai.list_models()

# Print model names
for model in models:
    print(model.name)
