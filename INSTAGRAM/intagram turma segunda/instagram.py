def get_page(page):
    print(page)



palavra_recebida = input("Digite uma palavra")
palavra_escrita = palavra_recebida + "/"
page = get_page("https://www.instagram.com/explore/tags/"+palavra_escrita)

