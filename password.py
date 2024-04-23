import tkinter as tk
import random

def gerar_senha_aleatoria():
    chars = 'abcderfgijklmnopqrstuvwyz12345678910!@#$%*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    password = ''
    
    for _ in range(20):
        password += random.choice(chars)
    
    senha_label.config(text="Sua senha aleatória: " + password)

def gerar_senha_customizada(texto):
    # Converte o texto para uma lista de caracteres
    caracteres = list(texto)
    
    # Embaralha os caracteres
    random.shuffle(caracteres)
    
    # Junta os caracteres embaralhados para formar a senha
    senha = ''.join(caracteres)
    
    senha_label.config(text="Sua senha customizada: " + senha)

def gerar_senha():
    texto = entrada_texto.get()
    
    # Verifica se o campo de entrada está vazio
    if not texto:
        senha_label.config(text="Por favor, digite algo para gerar a senha.")
        return
    
    # Chama o método para gerar a senha customizada
    gerar_senha_customizada(texto)

# Criando a janela
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("500x400")
janela.iconbitmap("password.ico")


# Adiciona a imagem
imagem = tk.PhotoImage(file="password.png")
label_imagem = tk.Label(janela, image=imagem, bg="white")
label_imagem.pack(pady=10)  # Espaço após a imagem


# Rótulo e campo de entrada para texto customizado
texto_label = tk.Label(janela, text="Digite nomes, datas, caracteres, etc:", font=('Arial', 12))
texto_label.pack(pady=10)

entrada_texto = tk.Entry(janela, width=40, font=('Arial', 12))
entrada_texto.pack()

# Botão para gerar senha customizada
gerar_customizado_button = tk.Button(janela, text="Gerar Senha Customizada", command=gerar_senha, font=('Arial', 12), bg="#007bff", fg="white")
gerar_customizado_button.pack(pady=10)

# Rótulo para exibir senha gerada
senha_label = tk.Label(janela, text="Clique em 'Gerar Senha Aleatória' para obter sua senha aleatória", font=('Arial', 12))
senha_label.pack(pady=20)

# Botão para gerar senha aleatória
gerar_aleatoria_button = tk.Button(janela, text="Gerar Senha Aleatória", command=gerar_senha_aleatoria, font=('Arial', 12), bg="#007bff", fg="white")
gerar_aleatoria_button.pack()

janela.mainloop()
