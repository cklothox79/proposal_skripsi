import streamlit as st

st.title("📂 Referensi dan Lampiran")

tab1, tab2 = st.tabs(["Daftar Pustaka", "Lampiran"])

with tab1:
    st.subheader("Daftar Pustaka")
    st.write("Berisi daftar referensi yang digunakan dalam penelitian.")

with tab2:
    st.subheader("Lampiran")
    try:
        with open("docs/skripsi_dummy.pdf", "rb") as file:
            st.download_button("📥 Unduh Skripsi Lengkap", file, file_name="skripsi_ferri_kusuma.pdf")
    except:
        st.info("Lampiran PDF akan ditambahkan di sini.")
