
from gtts import gTTS

import os

mtext = 'Sam'

language = 'en'

myobj = gTTS(text=mtext, lang=language, slow=False)

myobj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")
