import streamlit as st

st.set_page_config(
    page_title="Kuisioner PMPJ Notaris",
    page_icon="🧾",
    layout="wide",
)

st.image(
    "assets/header.png", 
    use_column_width=True
)

st.title("🧾 Kuisioner Kepatuhan PMPJ bagi Notaris")
st.markdown("---")

st.markdown("""
Selamat datang di aplikasi **SERENA** 👋  

Aplikasi ini digunakan untuk mengisi dan mengelola kuisioner terkait  
**kepatuhan penerapan Prinsip Mengenal Pengguna Jasa (PMPJ)** bagi notaris.  

Gunakan menu di **sidebar** atau klik tombol di bawah untuk mulai mengisi kuisioner.
""")

# --- Tombol Next ---
if st.button("➡️ Mulai Isi Kuisioner"):
    st.switch_page("pages/stkanwil1.py")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 SERENA — oleh Kementerian Hukum Jawa Timur")
