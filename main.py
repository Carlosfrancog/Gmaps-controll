import smtplib
import email.message
import tkinter as tk


def verify():
    # new window
    verify_window = tk.Toplevel(root)
    verify_window.title("Gmaps verify")

    # form lables
    # form labels
    operador_label = tk.Label(verify_window, text=f"Operador: {operador_entry.get()}")
    operador_label.pack()

    nome_fantasia_label = tk.Label(verify_window, text=f"Nome Fantasia: {nome_fantasia_entry.get()}")
    nome_fantasia_label.pack()

    razao_social_label = tk.Label(verify_window, text=f"Razão Social: {razao_social_entry.get()}")
    razao_social_label.pack()

    cnpj_label = tk.Label(verify_window, text=f"CNPJ: {cnpj_entry.get()}")
    cnpj_label.pack()

    ramo_atividade_label = tk.Label(verify_window, text=f"Ramo de Atividade: {ramo_atividade_entry.get()}")
    ramo_atividade_label.pack()

    endereco_label = tk.Label(verify_window, text=f"Endereço: {endereco_entry.get()}")
    endereco_label.pack()

    cidade_label = tk.Label(verify_window, text=f"Cidade: {cidade_entry.get()}")
    cidade_label.pack()

    cep_label = tk.Label(verify_window, text=f"CEP: {cep_entry.get()}")
    cep_label.pack()

    telefone_label = tk.Label(verify_window, text=f"Telefone: {telefone_entry.get()}")
    telefone_label.pack()

    autorizante_label = tk.Label(verify_window, text=f"Autorizante: {autorizante_entry.get()}")
    autorizante_label.pack()

    cargo_label = tk.Label(verify_window, text=f"Cargo: {cargo_entry.get()}")
    cargo_label.pack()

    data_venda_label = tk.Label(verify_window, text=f"Data Venda: {data_venda_entry.get()}")
    data_venda_label.pack()

    vencimento_label = tk.Label(verify_window, text=f"Vencimento: {vencimento_entry.get()}")
    vencimento_label.pack()

    valor_label = tk.Label(verify_window, text=f"Valor: {valor_entry.get()}")
    valor_label.pack()

    email_label = tk.Label(verify_window, text=f"E-mail: {email_entry.get()}")
    email_label.pack()


def send_email():
    #mail info
    operador = operador_entry.get()
    nome_fantasia = nome_fantasia_entry.get()
    razao_social = razao_social_entry.get()
    cnpj = cnpj_entry.get()
    ramo_atividade = ramo_atividade_entry.get()
    endereco = endereco_entry.get()
    cidade = cidade_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    autorizante = autorizante_entry.get()
    cargo = cargo_entry.get()
    data_venda = data_venda_entry.get()
    vencimento = vencimento_entry.get()
    valor = valor_entry.get()
    email_destinatario = email_entry.get()
    alteracoes = alteracoes_text.get("1.0", tk.END)
    
    #body mail
    corpo_email = f"""
    <h1>ENVIO DE VENDA</h1>
    <br>
    <hr>
    <p><strong>Operador:</strong> <u>{operador.upper()}</u></p>
    <p><strong>Nome Fantasia:</strong> <u>{nome_fantasia.upper()}</u></p>
    <p><strong>Razão Social:</strong> <u>{razao_social.upper()}</u></p>
    <p><strong>CNPJ:</strong> <u>{cnpj.upper()}</u></p>
    <p><strong>Ramo de Atividade:</strong> <u>{ramo_atividade.upper()}</u></p>
    <p><strong>Endereço:</strong> <u>{endereco.upper()}</u></p>
    <p><strong>Cidade:</strong> <u>{cidade.upper()}</u></p>
    <p><strong>CEP:</strong> <u>{cep.upper()}</u></p>
    <p><strong>Telefone:</strong> <u>{telefone.upper()}</u></p>
    <p><strong>Autorizante:</strong> <u>{autorizante.upper()}</u></p>
    <p><strong>Cargo:</strong> <u>{cargo.upper()}</u></p>
    <p><strong>Data de Venda:</strong> <u>{data_venda.upper()}</u></p>
    <p><strong>Vencimento:</strong> <u>{vencimento.upper()}</u></p>
    <p><strong>Valor:</strong> <u>{valor.upper()}</u></p>
    <p><strong>Email:</strong> <u>{email_destinatario.upper()}</u></p>
    <br>
    <hr>
    <p><strong>Alterações:</strong></p>
    <p>{alteracoes.upper()}</p></u>
    """

    #to send
    msg = email.message.Message()
    msg['Subject'] = 'Assunto'
    msg['From'] = "testes.emails.teste@gmail.com"
    msg['To'] = 'carlosfranco.contato@gmail.com'
    password = 'fbcwexmgecnltpor'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #Login Credentials for sendin the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado!') 


# create Screen root
root = tk.Tk()
root.title("Gmaps controll")

form_container = tk.Frame(root)
form_container.pack(padx=10, pady=10)

operador_label = tk.Label(form_container, text="Oprador:")
operador_label.grid(row=0, column=0, sticky=tk.E)

operador_entry = tk.Entry(form_container)
operador_entry.grid(row=0, column=1)
operador_entry.insert(0, "Oprador")

nome_fantasia_label = tk.Label(form_container, text="Nome Fantasia:")
nome_fantasia_label.grid(row=1, column=0, sticky=tk.E)

nome_fantasia_entry = tk.Entry(form_container)
nome_fantasia_entry.grid(row=1, column=1)
nome_fantasia_entry.insert(0, "Nome Fantasia")

razao_social_label = tk.Label(form_container, text="Razão Social:")
razao_social_label.grid(row=2, column=0, sticky=tk.E)

razao_social_entry = tk.Entry(form_container)
razao_social_entry.grid(row=2, column=1)
razao_social_entry.insert(0, "Razão Social")

cnpj_label = tk.Label(form_container, text="CNPJ:")
cnpj_label.grid(row=3, column=0, sticky=tk.E)

cnpj_entry = tk.Entry(form_container)
cnpj_entry.grid(row=3, column=1)
cnpj_entry.insert(0, "CNPJ")

ramo_atividade_label = tk.Label(form_container, text="Ramo de Atividade:")
ramo_atividade_label.grid(row=4, column=0, sticky=tk.E)

ramo_atividade_entry = tk.Entry(form_container)
ramo_atividade_entry.grid(row=4, column=1)
ramo_atividade_entry.insert(0, "Ramo de Atividade")

endereco_label = tk.Label(form_container, text="Endereço:")
endereco_label.grid(row=5, column=0, sticky=tk.E)

endereco_entry = tk.Entry(form_container)
endereco_entry.grid(row=5, column=1)
endereco_entry.insert(0, "Endereço")

cidade_label = tk.Label(form_container, text="Cidade:")
cidade_label.grid(row=6, column=0, sticky=tk.E)

cidade_entry = tk.Entry(form_container)
cidade_entry.grid(row=6, column=1)
cidade_entry.insert(0, "Cidade")

cep_label = tk.Label(form_container, text="CEP:")
cep_label.grid(row=7, column=0, sticky=tk.E)

cep_entry = tk.Entry(form_container)
cep_entry.grid(row=7, column=1)
cep_entry.insert(0, "CEP")

telefone_label = tk.Label(form_container, text="Telefone:")
telefone_label.grid(row=8, column=0, sticky=tk.E)

telefone_entry = tk.Entry(form_container)
telefone_entry.grid(row=8, column=1)
telefone_entry.insert(0, "Telefone")

autorizante_label = tk.Label(form_container, text="Autorizante:")
autorizante_label.grid(row=9, column=0, sticky=tk.E)

autorizante_entry = tk.Entry(form_container)
autorizante_entry.grid(row=9, column=1)
autorizante_entry.insert(0, "Autorizante")

cargo_label = tk.Label(form_container, text="Cargo:")
cargo_label.grid(row=10, column=0, sticky=tk.E)

cargo_entry = tk.Entry(form_container)
cargo_entry.grid(row=10, column=1)
cargo_entry.insert(0, "Cargo")

data_venda_label = tk.Label(form_container, text="Data Venda:")
data_venda_label.grid(row=11, column=0, sticky=tk.E)

data_venda_entry = tk.Entry(form_container)
data_venda_entry.grid(row=11, column=1)
data_venda_entry.insert(0, "Data Venda")

vencimento_label = tk.Label(form_container, text="Vencimento:")
vencimento_label.grid(row=12, column=0, sticky=tk.E)

vencimento_entry = tk.Entry(form_container)
vencimento_entry.grid(row=12, column=1)
vencimento_entry.insert(0, "Vencimento")

valor_label = tk.Label(form_container, text="Valor:")
valor_label.grid(row=13, column=0, sticky=tk.E)

valor_entry = tk.Entry(form_container)
valor_entry.grid(row=13, column=1)
valor_entry.insert(0, "Valor")

email_label = tk.Label(form_container, text="Email:")
email_label.grid(row=14, column=0, sticky=tk.E)

email_entry = tk.Entry(form_container)
email_entry.grid(row=14, column=1)
email_entry.insert(0, "Email")

alteracoes_label = tk.Label(form_container, text="Alterações:")
alteracoes_label.grid(row=15, column=0, sticky=tk.E)

alteracoes_text = tk.Text(form_container, width=30, height=10)
alteracoes_text.grid(row=15, column=1, sticky=tk.NSEW)
alteracoes_text.insert(tk.END, "Insira suas alterações aqui")

verificar_button = tk.Button(root, text="Verificar informações", command=verify)
verificar_button.pack(pady=10)


enviar_button = tk.Button(root, text="Enviar", command=send_email)
enviar_button.pack(pady=10)

root.mainloop()