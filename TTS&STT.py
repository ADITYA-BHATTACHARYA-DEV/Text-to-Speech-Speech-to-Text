**Run in Colab**
**Text to Speech**




!pip install --upgrade pip
!pip install --upgrade transformers scipy


!pip install transformers

from transformers import pipeline
text="Python is a high-level, general-purpose programming language"

pipe=pipeline("text-to-speech", model="suno/bark-small", device="cuda")

output = pipe(text)

output

from IPython.display import Audio
Audio(output["audio"], rate=output['sampling_rate'])
from gtts import gTTS


**Speech to Text**

from gtts import gTTS
!pip install gTTS

language = "en"
text="Hello World, I am Aditya Bhatatcharya, A fervent technophile, Driven by curiosity, I dive into emerging technologies, unraveling complex systems, building innovative solutions, and pushing the boundaries of what's possible"
speech = gTTS(text=text, lang=language, slow = False, tld="com.au" )
speech.save("textToSpeech.mp3")
