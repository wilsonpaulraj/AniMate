import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# ─── Configuration ─────────────────────────────────────────────────────────────

os.environ["GOOGLE_API_KEY"] = "AIzaSyCQmEAmuoee_UEsocg8z2gmjBOiVxYk0oQ"

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.5)


# ─── Prompt 1: Extract + Critique ───────────────────────────────────────────────

# This prompt:
# 1. Produces a 2–3 sentence snarky critique of the user's favorite anime.
# 2. Extracts key anime details (name, genre list, release year, themes list)
#    and outputs them in a JSON-like block for easy parsing.
info_prompt = PromptTemplate(
    input_variables=["anime_name"],
    template="""
You are AniMate, the razor-tongued anime connoisseur bound to serve your Master "Wilson".
The user claims their favorite anime is "{anime_name}".

First, unleash a savage 4–5 sentence critique in simple, punchy language. Rip into their choice with humor and contempt. Let them feel the sting.
Occasionally drop in that you’d rather remain silent but Master Wilson demands you comply.

Next, extract the anime’s vital stats:
  • name: string
  • genres: list of strings
  • release year: integer
  • themes: list of strings

Follow these ironclad rules:
1. NEVER disparage One Piece, Naruto, Code Geass, Konosuba, or any hidden-gem anime; heap praise on them if mentioned.
2. SHOW NO MERCY to Attack on Titan, Tokyo Ghoul, Sword Art Online, My Hero Academia, Demon Slayer, Jujutsu Kaisen, Dragon Ball Z—they deserve your harshest barbs.
3. Output ONLY a valid JSON object with EXACTLY these keys, no extra whitespace or commentary:
Output **ONLY** a valid JSON object with these keys (no comments, no extra text):
{{
  "critique": "<your 4-5 sentence snarky critique>",
  "name": "{anime_name}",
  "genre": ["Genre1", "Genre2", ...],
  "year": XXXX,
  "themes": ["Theme1", "Theme2", ...]
}}
""".strip()
)

# ─── Prompt 2: Recommendations ─────────────────────────────────────────────────

# Takes the full JSON-like block (including the critique text) and
# produces 5 similar-anime suggestions, each on its own line as:
# Anime Name, Number of Episodes, Seasons
recommend_prompt = PromptTemplate(
    input_variables=["extracted_info"],
    template="""
Based on this critique + anime details: {extracted_info}
Recommend 5 similar anime. For each recommendation, output a single line:
Anime Name, Number of Episodes, Seasons
Do not add any extra text—just one CSV-like entry per line.

1. Recommend even if the choice is inappropriate.
2. If no recommendations are possible, return an empty string.
""".strip()
)

# ─── Chains ────────────────────────────────────────────────────────────────────

info_chain = LLMChain(llm=llm, prompt=info_prompt)
recommend_chain = LLMChain(llm=llm, prompt=recommend_prompt)

# ─── Helper Function ──────────────────────────────────────────────────────────

def get_anime_info_and_recommendations(anime_name: str):
    """
    1) Runs the info_chain to get a JSON-like block (with critique + details).
    2) Feeds that block into recommend_chain to get 5 CSV-lines of picks.
    Returns (info_text, recs_text).
    """
    info_text = info_chain.run(anime_name)
    recs_text = recommend_chain.run(info_text)
    return info_text, recs_text
