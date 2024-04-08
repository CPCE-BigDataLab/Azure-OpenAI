import os
from openai import AzureOpenAI

client = AzureOpenAI(api_version="API_VERSION",				#INPUT API VERSION LIKE 2023-01-01
azure_endpoint="AZURE_ENDPOINT_URL",					#YOU CAN FOUND IT UNDER "Keys and Endpoint" -> "Endpoint", LIKE https://YOURENDPOINT.openai.azure.com/
api_key="API_KEY")							#YOUR API KEY

print("Welcome to Chatbot! (Type 'exit' to end the conversation)")

conversation=[{"role": "system", "content": "You are a helpful assistant based on Azure OpenAI ChatGPT-4 Technology. My GPT version is 4."}]

while(True):
    user_input = input("You: ")
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="DEPOLYMENT_NAME",	#DEPOLYMENT NAME YOU CAN IN AZURE OPENAI STUDIO
    messages = conversation)

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("Chatbot: " + response.choices[0].message.content + "\n")