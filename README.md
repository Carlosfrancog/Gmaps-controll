# S.E.N.D.E.R.: Simple Email Notification and Document Exporter Recorder

## Introdução

Este é um script Python que cria uma interface gráfica usando a biblioteca tkinter e permite que o usuário envie informações por email. O script solicita informações de quem está enviando e informações sobre o contexto do envio. Em seguida, ele gera um documento DOCX com as informações inseridas e envia por email.

## Uso

Para executar o script, siga estas etapas:

- Execute o script Python em um ambiente Python 3.x.
- Preencha os campos solicitados da interface gráfica com as informações desejadas.
- Verifique as informações inseridas antes de fazer o envio, clicando no botão "Verificar".
- Faça o envio das informações clicando no botão "Enviar".

## Dependências

O script depende das seguintes bibliotecas Python:

- `os`
- `smtplib`
- `datetime`
- `email.message`
- `tkinter`
- `email.mime.multipart`
- `email.mime.text`
- `email.mime.base`
- `email.encoders`
- `docx.Document`

## Estrutura do Código

O código é organizado da seguinte forma:

1. **Interface Gráfica:** Esta parte cria a janela da interface gráfica e permite que o usuário insira informações.
2. **Funções de Geração de Documento:** Funções que geram um documento DOCX com base nas informações inseridas pelo usuário.
3. **Envio de Email:** Função que envia o documento gerado por email.

## Personalização

Antes de usar este script, personalize os seguintes aspectos:

- Substitua as informações do servidor de email, como endereço e senha, na função `send_email()`.
- Modifique o conteúdo da mensagem de email e o assunto conforme necessário.
- Adicione um endereço de email de destino na função `send_email()`.

### Observações

- Este é um exemplo básico e pode ser estendido com recursos adicionais, como validação de entrada de dados, tratamento de erros mais robusto e uma interface de usuário mais sofisticada.
- Certifique-se de cumprir todas as leis de privacidade de dados ao coletar informações do usuário.
