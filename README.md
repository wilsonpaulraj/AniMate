# 🎭 AniMate - Your Snarky Anime Companion

**AniMate** is an AI-powered anime recommendation app with an attitude. Just enter your favorite anime title — you'll be roasted by a brutally honest critique and then rewarded with five AI-curated anime recommendations that (hopefully) redeem your taste.

Built with **Streamlit** and **Google Gemini 1.5 Flash** via **LangChain**, AniMate is fast, fun, and ruthlessly funny.

![AniMate Demo](https://via.placeholder.com/800x400?text=AniMate+Demo)

## 🚀 Features

- 🔍 Input your favorite anime title
- 🤖 Receive a savage yet hilarious AI-generated critique
- 🎯 Get 5 similar anime recommendations (episodes & season info included)
- 🎨 Clean and responsive Streamlit UI
- ⚡ Powered by Google's Gemini LLM (via LangChain)

## 🛠️ Tech Stack

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Google Generative AI (Gemini)](https://ai.google.dev/)

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/wilsonpaulraj/animate.git
cd animate
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API key
You can either:

- Set the environment variable in your terminal:
  ```bash
  export GOOGLE_API_KEY=your_gemini_api_key_here
  ```

- Or, if you prefer using a .env file:
  ```
  GOOGLE_API_KEY=your_gemini_api_key_here
  ```
  (And load it using python-dotenv or similar, if you modify the code.)

### 5. Run the app
```bash
streamlit run app.py
```

## 🌐 Live Demo

Coming soon on Streamlit Community Cloud

## 📁 Project Structure

```
animate/
├── app.py              # Frontend (Streamlit UI)
├── core.py             # LangChain chains and Gemini prompts
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ✅ Example Usage

1. Enter "Attack on Titan" as your favorite anime.
2. Get roasted for your "mainstream, brooding edge-lord choice".
3. See 5 snark-free recommendations like "91 Days, 24, 1".
4. Repeat until your taste improves.

## 📱 Screenshots

<div align="center">
  <img src="https://via.placeholder.com/250x450?text=Mobile+View" alt="Mobile View" width="250"/>
  <img src="https://via.placeholder.com/500x300?text=Desktop+View" alt="Desktop View" width="500"/>
</div>

## 🙏 Credits

- Built by Wilson Paulraj
- Prompt design and LLM response handled using LangChain
- Powered by Google Gemini 1.5 Flash

## 📜 License

This project is licensed under the MIT License.

Use it, modify it, deploy it, and roast responsibly.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
