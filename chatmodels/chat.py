# from dotenv import load_dotenv

# load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model(
#     "gemini-flash-latest" ,
#     model_provider="google_genai")

# print(type(model))


# response = model.invoke("Who is Virat Kohli?")

# print(response.content)

from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

response = model.invoke("write a poem on AI")

print(response.content)