# import pafy

# import vlc

# url = "https://www.youtube.com/watch?v=OCzrpR7Jtsk"
# video = pafy.new(url)
# best = video.getbest()
# playurl = best.url


# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(playurl)
# Media.get_mrl()
# player.set_media(Media)
# player.audio_set_mute(True)
# player.play()

from youtube_video_play_pause_bot import *
url = "https://www.youtube.com/watch?v=OCzrpR7Jtsk"
youtube.open(url)
youtube.play_pause_video()
