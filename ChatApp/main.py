#BOTAO INICIAR CHAT
#POPUP PARA ENTRAR CHAT
#QUANDO ENTRAR NO CHAT: APARECE PARA TODOS
  # A MENSAGEM QUE BC ENVIOU 
  #O CAMPO  PARA ENVIAR MENSAGEM 

# A CADA MENSAGEM QUE VC ENVIA APARECE PARA TODOS
  #NOME (TEXTO MENSAGEM)

import flet as ft

def main(pagina):
    texto = ft.Text("Testando Flask")

    #Criando o chat
    chat = ft.Column()


    #Nome Usuario
    nome_usuario = ft.TextField(label="Escreva seu nome")

    #Funcao enviar mensagem para todos os users
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            #Add mensagem no chat
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}")) #Adiciona o valor do campo mensagem, na coluna chat para todos. Com nome e mensagem do user
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.colors.DEEP_PURPLE_ACCENT_400))
        pagina.update() #atualiza o chat de todos depois

    
    pagina.pubsub.subscribe(enviar_mensagem_tunel) # faz a ligação entre túnel, com outros usuários


    #Envia a mensagem, para o túnel de todos
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto":campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"}) #Enviar pro tunel, tanto a mensagem e o nome do usuario
        #limpar campo de mensagem
        campo_mensagem.value = '' #Depois limpamos a caixa de texto
        pagina.update()


    #Campo de mensagem
    campo_mensagem = ft.TextField(label= "Digite uma mensagem", on_submit=enviar_mensagem)

    #Botao de envio mensagem
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem) #Chama a função enviar mensagem


    # Após abrir o popup, iremos executar essa função
    def entrar_popup(event):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        #Adicionar chat
        pagina.add(chat)
        #Fechar o popup
        popup.open = False
        #Remover o botao iniciar chat e texto
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #Campo mensagem
        #Criar o campo de enviar mensagem do user
        pagina.add(ft.Row([campo_mensagem,botao_enviar_mensagem])) # Para deixar todos na mesma linha

        pagina.update()


    popup = ft.AlertDialog(
        open=False, #Vai ficar fechado qnd abrir
        modal=True, # Mostar que é um Popup
        title=ft.Text("Bem vindo ao GabiZap!"), #Titulo à mostar
        content=nome_usuario,     #Nome que o user vai passar
        actions=[ft.ElevatedButton("Iniciar Chat!", on_click=entrar_popup)] #Chama a funcao Entrar Popup
    )

    #Função de clicar no botao e add uma mensagem
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() # Atualiza a página

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=entrar_chat) #Botao e funcao que ira executar qnd for clicado  


    pagina.add(texto) 
    pagina.add(botao_iniciar) #Add  Botao 


ft.app(target=main,view=ft.WEB_BROWSER, port=8000) #Formato de Web