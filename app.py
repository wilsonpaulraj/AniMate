import streamlit as st
import time
import json
from core import get_anime_info_and_recommendations

# Page configuration
st.set_page_config(
    page_title="AniMate - Personal Anime Recommender",
    layout="wide"
)

# Responsive style
st.markdown(
    '''<style>
        .block-container {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            padding-top: 2rem;
            padding-left: 5%;
            padding-right: 5%;
            padding-bottom: 0;
        }
        .main-content {
            flex: 1;
        }

        /* Make markdown blockquote look nicer */
        blockquote {
            padding: 0.5em 1em;
            margin: 1em 0;
            border-left: 0.25em solid #ccc;
            font-style: italic;
        }

        /* Ensure footer text is smaller on mobile */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 2%;
                padding-right: 2%;
            }
        }
        @media (max-width: 768px) {
    .element-container {
        flex-direction: column !important;
    }
}
    </style>''',
    unsafe_allow_html=True
)

# Main content wrapper
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Title and description
st.title("🎭 AniMate")
st.write("Discover personalized anime recommendations generated by AI.")

# User input
anime_name = st.text_input("Enter your favorite anime:")
if st.button("Get Recommendations"):
    if not anime_name:
        st.warning("Please enter an anime title to search.")
    else:
        with st.spinner("Analyzing taste..."):
            info_text, recs_text = get_anime_info_and_recommendations(anime_name)

        # Extract and display critique
        cleaned = info_text
        if cleaned.strip().startswith("```"):
            cleaned = cleaned.strip().lstrip('`')
            lines = cleaned.splitlines()
            if lines and lines[0].startswith("json") or lines[0].startswith("```json"):
                lines = lines[1:]
            if lines and lines[-1].strip().startswith("```"):
                lines = lines[:-1]
            cleaned = "".join(lines)
        try:
            info_dict = json.loads(cleaned)
            critique = info_dict.get("critique", cleaned)
        except Exception:
            critique = cleaned

        if critique:
            st.markdown(f"> {critique}")  # Markdown blockquote

        # Parse recommendations
        rec_lines = [line.strip() for line in recs_text.split("\n") if line.strip()]
        recs = []

        if not rec_lines:
            st.warning("No recommendations found.")

        for line in rec_lines:
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 3:
                recs.append({"name": parts[0], "episodes": parts[1], "seasons": parts[2]})

        # Display recommendations in responsive grid
        cols_per_row = 2  # Fallback to 1 on mobile
        for i in range(0, len(recs), cols_per_row):
            cols = st.columns(cols_per_row)
            for idx, rec in enumerate(recs[i:i+cols_per_row]):
                with cols[idx]:
                    st.markdown(
                        f"- **{rec['name']}**\n"
                        f"    - 📺 Episodes: {rec['episodes']}\n"
                        f"    - 🎬 Seasons: {rec['seasons']}"
                    )
else:
    st.info("Type an anime above and click 'Get Recommendations' to start.")

# Close main content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; padding: 1rem; font-size:0.85rem; color:#555;'>"
    "AniMate v1.0 | © 2025 Wilsonpaulraj | GitHub: <a href='https://github.com/wilsonpaulraj'>wilsonpaulraj</a>"
    "</div>", unsafe_allow_html=True
)
