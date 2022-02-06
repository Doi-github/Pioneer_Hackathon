from record_and_to_text import *
from play_and_text_to_speech import *

def judge_text(text):
    if "音楽" in text or "流" in text:
        text2 = "音楽を再生します。"
        auto_speech("音楽を再生します。","1.mp3")
        play("music.mp3")
        return text2

    if "バンド" in text or "名前" in text:
        text2 = "このアーティストはスピッツです。"
        auto_speech("このアーティストはスピッツです。","2.mp3")
        return text2

    if "昨日" in text or "ゴルフ" in text:
        text2 = "お父様の昨日の目的地は銀座です。"
        auto_speech("お父様の昨日の目的地は銀座です。","3.mp3")
        return text2

    if "やましい" in text:
        text2 = "お母様、グローブボックスを開けてください。"
        auto_speech("お母様、グローブボックスを開けてください。","4.mp3")
        return text2