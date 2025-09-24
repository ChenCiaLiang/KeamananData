import streamlit as st
from pathlib import Path
import frontmatter
from datetime import datetime

st.set_page_config(page_title="My Streamlit Blog", page_icon="🗞️", layout="wide")

# ---------- Helpers ----------
POSTS_DIR = Path("posts")

@st.cache_data
def load_posts():
    posts = []
    for p in sorted(POSTS_DIR.glob("*.md")):
        fm = frontmatter.load(p)
        meta = fm.metadata or {}
        posts.append({
            "path": p,
            "slug": p.stem,
            "title": meta.get("title", p.stem.replace("-", " ").title()),
            "date": meta.get("date", ""),
            "tags": meta.get("tags", []),
            "summary": meta.get("summary", ""),
            "content": fm.content
        })
    # Sort newest first if date present
    def sort_key(x):
        try:
            return datetime.fromisoformat(x["date"])
        except Exception:
            return datetime.min
    posts.sort(key=sort_key, reverse=True)
    return posts

def render_post(post):
    st.title(post["title"])
    meta_line = []
    if post["date"]: meta_line.append(f"**{post['date']}**")
    if post["tags"]: meta_line.append(" • " + ", ".join([f"`{t}`" for t in post["tags"]]))
    if meta_line:
        st.caption("".join(meta_line))
    st.markdown(post["content"])

# ---------- UI ----------
st.sidebar.title("Posts")
posts = load_posts()

# Search + filter
query = st.sidebar.text_input("Search title / summary")
if query:
    posts = [p for p in posts if query.lower() in (p["title"] + " " + p["summary"]).lower()]

# Post picker
titles = [p["title"] for p in posts]
selection = st.sidebar.radio("Select a post", titles) if titles else None

# Home header
st.header("🗞️ My Streamlit Blog")
st.write("Built with Streamlit + Markdown files in `/posts`.")

# Show either the selected post or a list
if selection:
    post = next(p for p in posts if p["title"] == selection)
    render_post(post)
else:
    for p in posts:
        st.subheader(p["title"])
        if p["date"] or p["tags"]:
            small = []
            if p["date"]: small.append(p["date"])
            if p["tags"]: small.append(", ".join(p["tags"]))
            st.caption(" • ".join(small))
        if p["summary"]:
            st.write(p["summary"])
        if st.button(f"Read: {p['title']}", key=p["slug"]):
            st.session_state["selected"] = p["title"]
            st.experimental_rerun()
