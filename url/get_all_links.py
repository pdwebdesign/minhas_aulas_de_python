import requests

def get_page(page):
    page = requests.get(page)
    print(page)
    print(page.status_code)  # 200 significa requisição OK
    page = str(page.content)
    return page

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

page = get_page("https://www.facebook.com/")
print_all_links(page)
