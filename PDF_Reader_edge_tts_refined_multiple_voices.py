import asyncio
import edge_tts

voices = ['en-AU-NatashaNeural','en-AU-WilliamNeural','en-CA-ClaraNeural','en-CA-LiamNeural','en-GB-LibbyNeural']
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
voice = voices[1]
output_file = "test_NatashaNeural.mp3"

async def amain() -> None:
    communicate = edge_tts.Communicate(text,voice)
    await communicate.save(output_file)
loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    loop.run_until_complete(amain())
except:
    loop.close()