# Pytube é uma biblioteca que deixa fácil o trabalho de realizar downloads de vídeo do youtube. É possivel realizar
# download em todas as qualidade e tipos, possível tbm baixar somente o audio daquele vídeo. E ainda é possível retirar dados estatíticos do vídeo.


from pytube import YouTube, Playlist


# Para mais informações entrar em https://medium.com/umcodigo/download-de-v%C3%ADdeos-e-playlists-do-youtube-com-python-e24197272c9e

def download_one_video(url_video: str, output='downloaded'):
    video = YouTube(url=url_video)
    print(f'Iniciando o download do vídeo "{video.title}" do canal {video.author}')
    video.streams.get_highest_resolution().download(output_path=output)


def download_playlist(url_playlist, output='downloaded'):
    # Vai recerber vários objetos(cada um sendo uma url com seus possíveis tipos de formatos e resolução)
    playlist = Playlist(url=url_playlist)
    print(f'Iniciando o download da playlist "{playlist.title}".')

    for url in playlist.video_urls:
        print(url)



if __name__ == '__main__':
    links = []
    entrada = input('Insere Link: ')

    while entrada != "-1":
        links.append(entrada)
        entrada = input('Insere Link: ')


    for link in links:
        download_one_video(link)

    # download_playlist('https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng')
