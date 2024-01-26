import time
import openai

openai.api_key = "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"

# def chat_with_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         messages = [{"role":"user", "content":prompt}]
#     )

#     return response.choice[0].message.content.strip()

# if __name__ == "__main__" :
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit","exit", "bye"]:
#             break

#         response = chat_with_gpt(user_input)
#         print("Nancy AI: ", response)

# engines = openai.Engine.list()
# print(engines)

# def chat_with_gpt(user_input):
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo",
#         # model = "gpt-3.5-turbo-1106",
#         prompt=user_input,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             break
#         response = chat_with_gpt(user_input)
#         print(f"Bot: {response}")

def chat_with_gpt(user_input):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError as e:
        # Handle rate limit error with exponential backoff
        wait_time = 2  # Initial wait time in seconds
        max_retries = 5  # Maximum number of retries
        retries = 0

        while retries < max_retries:
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying.")
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff
            retries += 1

            try:
                response = openai.Completion.create(
                    engine="gpt-3.5-turbo",
                    prompt=user_input,
                    max_tokens=150
                )
                return response.choices[0].text.strip()
            except openai.error.RateLimitError:
                continue
        else:
            print("Max retries reached. Unable to get a response.")
            return "I'm currently experiencing issues. Please try again later."

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")