import requests
from bs4 import BeautifulSoup
import argparse
import time


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
print("         0 mr.sherlock.py V.1.1 000000000000000000")  

#lista de sites:

social_media_urls = {
    'Odysee': 'https://odysee.com/@{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Medium': 'https://medium.com/@{}',
    'Facebook': 'https://www.facebook.com/{}',
    'GitHub': 'https://github.com/{}',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'WeChat': 'https://weixin.qq.com/u/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Skype': 'https://join.skype.com/invite/{}',
    'Spotify': 'https://open.spotify.com/user/{}',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'YouTube': 'https://www.youtube.com/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'TikTok': 'https://www.tiktok.com/@{}',
    'FreeCodeCamp': 'https://www.freecodecamp.org/{}',
    'TryHackMe': 'https://tryhackme.com/p/{}',
    'Freelancer': 'https://www.freelancer.com/u/{}',
    'GitLab': 'https://gitlab.com/{}',
    'Archive.org': 'https://archive.org/details/@{}',
    'Fandom': 'https://www.fandom.com/wiki/User:{}',
    'Interpals': 'https://www.interpals.net/{}',
    'PSNProfiles': 'https://psnprofiles.com/{}',
    'About.me': 'https://about.me/{}',
    'PyPI': 'https://pypi.org/user/{}',
    'Tumblr': 'https://{}.tumblr.com/',
    '9GAG': 'https://9gag.com/u/{}',
    'VK': 'https://vk.com/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'YouPic': 'https://youpic.com/photographer/{}',
    'MyAnimeList': 'https://myanimelist.net/profile/{}',
    'Wattpad': 'https://www.wattpad.com/user/{}',
    'MySpace': 'https://myspace.com/{}',
    'Disqus': 'https://disqus.com/by/{}',
    'Threads': 'https://threads.net/{}',
    'Behance': 'https://www.behance.net/{}',
    'Tripadvisor': 'https://www.tripadvisor.com.br/Profile/{}',
    'Polyvore': 'https://polyvore.ch/author/{}/',
    'Kongregate': 'https://www.kongregate.com/accounts/{}',
    'Geeksforgeeks': 'https://www.geeksforgeeks.org/user/{}/',
    'Spice Works': 'https://www.spiceworks.com/user/about/{}',
    'Stackoverflow': 'https://pt.stackoverflow.com/search?q={}',
    'Researchgate': 'https://www.researchgate.net/profile/{}',
    'Meetup Community': 'https://www.meetup.com/{}/',
    'Wiki Osgeo': 'https://wiki.osgeo.org/wiki/User:{}',
    'Wikimon': 'https://wikimon.net/User:{}',
}

# Essa função é responsável por buscar o conteúdo de uma página web, fazendo uma requisição HTTP usando a biblioteca requests.
def get_page_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
        }
# Cabeçalhos (headers): O User-Agent é um cabeçalho HTTP que simula uma requisição feita por um navegador.        
        response = requests.get(url, headers=headers, timeout=9) # timeout=15 define que a requisição deve falhar se não for respondida em 15 segundos.
        if response.status_code == 200:# checa se o código de status HTTP retornado pela página é 200, que é "OK".
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e: # Captura exceções caso a requisição falhe (por exemplo, problemas de rede, servidor não encontrado, etc.)
        print(f'[!] Erro ao acessar {url}: {e}')
        return None

# Função para verificar se o nome de usuário está presente em alguma rede social
def check_social_media(username):
    results_found = False
    for social_media, url_template in social_media_urls.items(): # Esse dicionário contém as URLs base de diversas redes sociais.
        base_url = url_template.format(username) # Para cada rede social, o código substitui o {} na URL pelo nome de usuário fornecido, criando o link completo pro perfil.
        try:
            content = get_page_content(base_url) # Chama a função get_page_content para buscar o conteúdo da página de perfil da rede social.
            if content:
                soup = BeautifulSoup(content, 'html.parser')
# Usa a biblioteca BeautifulSoup pra parsear o HTML retornado. Essa biblioteca facilita a extração de informações do HTML de forma estruturada.
# Função soup.get_text() pega o texto visível da página HTML. A verificação if username in soup.get_text() checa se o nome de usuário está presente na página.
                if username in soup.get_text():
                    print(f'[+] Username encontrado no {social_media}: {base_url}')
                    results_found = True

        except Exception as e:
            print(f'[!] Erro de requisição para {social_media}: {e}')

        # Atraso de 1 segundo entre cada requisição
        time.sleep(1)  # Aguarda 1 segundo antes de fazer a próxima requisição.

    if not results_found:
        print(f'[-] Nenhum resultado encontrado para o username "{username}"')

# Função principal para iniciar a busca
def sherlock(username):
    print(f'[+] Iniciando busca por "{username}"...\n')
    check_social_media(username)

# Função para lidar com argumentos fornecidos ao script quando executado pela de linha de comando
def main():
    # Criando o parser de argumentos
    parser = argparse.ArgumentParser(description="Verifique se um usuário existe em diversas redes sociais.")
    parser.add_argument("username", help="Nome de usuário a ser verificado")

    # Parse do argumento
    args = parser.parse_args()

    # Chama a função de verificação com o nome de usuário fornecido
    sherlock(args.username)
# Esse trecho é uma verificação padrão para garantir que o código seja executado apenas quando o script for chamado    
if __name__ == "__main__":
    main()
