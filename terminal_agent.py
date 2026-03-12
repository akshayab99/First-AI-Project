from langchain_community.llms import Ollama

llm = Ollama(model="tinyllama")

print("Akshay Bandal's AI Agent Ready")
print("Commands:")
print("1. ask <question>")
print("2. analyze <logfile>")
print("3. exit\n")

while True:

    user_input = input("You: ")

    if user_input == "exit":
        break

    if user_input.startswith("analyze"):

        file_path = user_input.split(" ")[1]

        try:
            with open(file_path, "r") as f:
                logs = f.read()

            prompt = f"""
You are a DevOps troubleshooting expert.

Analyze this log and explain:
1. What the error is
2. Possible root cause
3. Suggested fix

Log:
{logs}
"""

            response = llm.invoke(prompt)

            print("\nAnalysis:\n")
            print(response)

        except:
            print("Log file not found.")

    elif user_input.startswith("ask"):

        question = user_input.replace("ask ", "")

        response = llm.invoke(question)

        print("\nAgent:", response)

    else:
        print("Unknown command")
