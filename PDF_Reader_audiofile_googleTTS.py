from gtts import gTTS

text = """I
        A MESSAGE FROM THE AUTHOR says that
        n writing Mindset Secrets for Winning, I drew upon many aspects of my life, from business
        to sports, struggles to triumphs, and rags to riches. I researched broadly, from the
        preparation of Olympic athletes to the techniques of the world's best coaches, as well as to
        every influential aspect in the lives of the successful elite. As a peak performance book,
        Mindset Secrets for Winning often emphasizes examples from sports, but it is certainly not
        limited to athletics. Those who want to become the best version of themselves in whatever
        they do will benefit from this book. I encourage all readers to keep an open mind to gather
        insights that apply to their own lives. It's important to read the entire book, as each section
        builds on the previous section. In all your pursuits, I wish you the best."""

# Clean up the text formatting
text = text.replace("         ", " ").strip()

# Different language options (which will change the voice)
languages = {
    "English (US)": "en",
    "English (UK)": "en-uk", 
    "English (Australia)": "en-au",
    "English (India)": "en-in"
}

# Try different speeds
for lang_name, lang_code in languages.items():
    # Normal speed
    tts = gTTS(text, lang=lang_code, slow=False)
    tts.save(f'author_{lang_name.lower().replace(" ", "_")}_normal.mp3')
    
    # Slow speed
    tts = gTTS(text, lang=lang_code, slow=True)
    tts.save(f'author_{lang_name.lower().replace(" ", "_")}_slow.mp3')

print("All MP3 files have been created!")