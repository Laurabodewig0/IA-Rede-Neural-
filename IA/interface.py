import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline

# Inicializando o pipeline da IA
chatbot = pipeline("text-generation", model="gpt2")

# Função para processar entrada e gerar resposta
def process_input():
    user_input = user_entry.get()
    if user_input.strip().lower() == "sair":
        root.destroy()
        return
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    bot_response = response[0]["generated_text"]
    
    chat_area.insert(tk.END, f"Você: {user_input}\n")
    chat_area.insert(tk.END, f"Chatbot: {bot_response}\n\n")
    user_entry.delete(0, tk.END)

# Configuração da Janela Principal
root = tk.Tk()
root.title("Chatbot com IA")

# Área de Texto para Mostrar a Conversa
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(padx=10, pady=10)

# Campo de Entrada do Usuário
user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)

# Botão para Enviar
send_button = tk.Button(root, text="Enviar", command=process_input)
send_button.pack(padx=10, pady=5)

# Loop Principal da Interface
root.mainloop()
