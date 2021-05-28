from pytube import YouTube
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

print("""
  __  ___  _______  ________  .__   __.      ___      .___________. __    ______      .__   __. 
|  |/  / |   ____||       /  |  \ |  |     /   \     |           ||  |  /  __  \     |  \ |  | 
|  '  /  |  |__   `---/  /   |   \|  |    /  ^  \    `---|  |----`|  | |  |  |  |    |   \|  | 
|    <   |   __|     /  /    |  . `  |   /  /_\  \       |  |     |  | |  |  |  |    |  . `  | 
|  .  \  |  |____   /  /----.|  |\   |  /  _____  \      |  |     |  | |  `--'  |    |  |\   | 
|__|\__\ |_______| /________||__| \__| /__/     \__\     |__|     |__|  \______/     |__| \__| 
                                                                                               

""")

url=(input("Indica la url del video: "))
path="/keznationytconverter/downloads/mp3"

yt=YouTube(url)

print("Titulo......: " + yt.title)
print("Duracion(seg).: " , yt.length)

# lst=yt.streams.filter(only_audio=True).all()

st=yt.streams.get_by_itag("140")
descarga=st.download(path)


print(descarga)


#tipo=type(descarga)
#print(tipo)

audio=AudioSegment.from_file(descarga)
audio.export(yt.title+"_audio.mp3", format="mp3")

##https://www.youtube.com/watch?v=gf6voPX1Z4U

