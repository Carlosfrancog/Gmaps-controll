<h1>Documentação do código S.E.N.D.E.R.: Simple Email Notification and Document Exporter Recorder</h1>

<h2>Introdução</h2>
<p>Este é um script Python que cria uma interface gráfica usando a biblioteca tkinter e permite que o usuário envie informações por email. O script solicita informações de quem está enviando e informações sobre o contexto do envio. Em seguida, ele gera um documento DOCX com as informações inseridas e envia por email.</p>

<h2>Uso</h2>
<p>para executar o script siga as etapas:
    <ul>
        <li>Execute o script Python em um ambiente Python 3.x.</li>
        <li>Preencha os campos solicitados da interface gráfica com as informações desejadas.</li>
        <li>Verifique as informações inseridas antes de fazer o envio, clicando no botão "Verificar".</li>
        <li>Faça o envio das informaçõe clicando no botão "Enviar".</li>
    </ul>
</p>

<h2>Dependências</h2>
<p>O script depende das seguintes bibliotecas Python:
    <ul>
        <li>`os`</li>
        <li>`smtplib`</li>
        <li>`datetime`</li>
        <li>`email.message`</li>
        <li>`tkinter`</li>
        <li>`email.mime.multipart`</li>
        <li>`email.mime.text`</li>
        <li>`email.mime.base`</li>
        <li>`email.encoders`</li>
        <li>`docx.Document`</li>
    </ul>
</p>

<h2>Estrutura do Código</h2>
<p>
    <ol>
        <li><strong>Interface Gráfica:</strong> A parte que cria a janela da interface gráfica e permite que o usuário insira informações.</li>
        <li><strong>Funções de Geração de Documento:</strong> Funções que geram um documento DOCX com base nas informações inseridas pelo usuário.</li>
        <li><strong>Envio de Email:</strong> Função que envia o documento gerado por email.</li>
    </ol>
</p>

<h2>Personalização</h2>
<p>Antes de usar este script, personalize os seguintes aspectos:
    <ul>
        <li>Substitua as informações do servidor de email, como endereço e senha, na função `send_email()`.</li>
        <li>Modifique o conteúdo da mensagem de email e o assunto conforme necessário.</li>
        <li>Adicione um endereço de email de destino na função `send_email()`.</li>
    </ul>
</p>

<h3>Observações</h3>
<p>
    <ul>
        <li>Este é um exemplo básico e pode ser estendido com recursos adicionais, como validação de entrada de dados, tratamento de erros mais robusto e uma interface de usuário mais sofisticada.</li>
        <li>Certifique-se de cumprir todas as leis de privacidade de dados ao coletar informações do usuário.</li>
    </ul>
</p>

