import requests
from bs4 import BeautifulSoup
import argparse
import time

# ASCII art do título
def print_banner():
    print("                    0000000000000000000000000000")
    print("                  00000000000000000000000000000000")
    print("                 0000000000000000000000000000000000")
    print("                000000000000000000000000000000000000")
    print("               00000000000000000000000000000000000000")
    print("               000000000000000000000000000000000000000")
    print("              30000000000000000000000000000000000000000")
    print("               000000000000000000000000000000000000000000")
    print("               000000000000000000000000000000000000000000000")
    print("               00000000000000000000000000000000000000000000002")
    print("               0000000000000000000000000000000000000")
    print("               000000000000000000000000000000000000006")
    print("              00000000000000000000000000000000000000000")
    print("              0000000000000000000000000000000000000000000")
    print("             000000000000000000000000000000000000000000000")
    print("            30000000000000000000000000000000000000000000000")
    print("            00000000000000000000000000000000000000000000000")
    print("                 90000000000000000000000000000000000000")
    print("                   000000000000000000000000000000000000")
    print("                    0000000000000000000000000000000000000000")
    print("                     000000000000000000000000000000000004600000")
    print("                     000000000000000000000000000000000       000")
    print("               2000000000000000000000000000000000000008       000")
    print("                000000000000000000000000000000000000005       002   77777")
    print("                 0000000000000000000000000000000047           00   0000000")
    print("                 00000000000000000000000000000                008 20000000")
    print("               000000000000000000000000000000                 000000000000")
    print("              0000000000000000000000000000001                  00000000000")
    print("             0000000000000000000000000000000000000               00000000")
    print("            0000000000000000000000000000000000000000000")
    print("           0000000000000000000000000000000000000000008")
    print("          000000000000000000000000000000000000000000")
    print("         0 social_sleuth V.0.1 000000000000000000")

# Lista de URLs de redes sociais
social_media_urls = {
    'Odysee': 'https://odysee.com/@{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Medium': 'https://medium.com/@{}',
    'Facebook': 'https://www.facebook.com/{}',
    'GitHub': 'https://github.com/{}',
    # Adicione mais redes sociais conforme necessário...
}

# Obtém o conteúdo da página
def get_page_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=9)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f'[!] Erro ao acessar {url}: {e}')
        return None

# Verifica presença de um nome de usuário
def check_social_media(username):
    results_found = False
    for social_media, url_template in social_media_urls.items():
        base_url = url_template.format(username)
        try:
            content = get_page_content(base_url)
            if content:
                soup = BeautifulSoup(content, 'html.parser')
                if username in soup.get_text():
                    print(f'[+] Username encontrado no {social_media}: {base_url}')
                    results_found = True
        except Exception as e:
            print(f'[!] Erro de requisição para {social_media}: {e}')
        time.sleep(1)  # Atraso para evitar bloqueios

    if not results_found:
        print(f'[-] Nenhum resultado encontrado para o username "{username}"')

# Função principal para iniciar a busca
def sherlock(username):
    print(f'[+] Iniciando busca por "{username}"...\n')
    check_social_media(username)

# Função principal de entrada
def main():
    print_banner()  # Exibe o banner de início
    parser = argparse.ArgumentParser(description="Verifique se um usuário existe em diversas redes sociais.")
    parser.add_argument("username", help="Nome de usuário a ser verificado")
    args = parser.parse_args()
    sherlock(args.username)

if __name__ == "__main__":
    main()
