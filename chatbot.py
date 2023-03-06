import openai
import tkinter as tk

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        self.conversation_label = tk.Label(master, text="Conversation:")
        self.conversation_label.grid(row=0, column=0, columnspan=2)

        self.conversation_text = tk.Text(master, height=20, width=150)
        self.conversation_text.grid(row=1, column=0, columnspan=2)

        self.message_label = tk.Label(master, text="Enter your message:")
        self.message_label.grid(row=2, column=0)

        self.message_entry = tk.Entry(master, width=80)
        self.message_entry.grid(row=2, column=1)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.grid(row=3, column=1, sticky="E")

    def send_message(self):
        openai.api_key = "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"
        message = self.message_entry.get()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{message}\n",
            max_tokens=2048,
            n = 1,
            stop=None,
            temperature=0.5
        )
        response = response["choices"][0]["text"]
        self.conversation_text.insert(tk.END, "YOU :  " + message + "\n")
        self.conversation_text.insert(tk.END, "BOT :  " + response + "\n")
        self.message_entry.delete(0, tk.END)

root = tk.Tk()
my_gui = ChatbotGUI(root)
root.mainloop()
