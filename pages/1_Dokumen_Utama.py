import streamlit as st
from docx import Document

st.title("📑 Dokumen Utama")

tab1, tab2 = st.tabs(["Halaman Judul", "Lembar Persetujuan & Daftar Isi"])

with tab1:
    try:
        doc = Document("docs/Halaman_Judul.docx")
        for para in doc.paragraphs:
            if para.text.strip():
                st.write(para.text)
    except:
        st.warning("⚠️ File Halaman_Judul.docx belum ditemukan.")

with tab2:
    try:
        doc = Document("docs/Halaman_Persetujuan_daftar_isi.docx")
        for para in doc.paragraphs:
            if para.text.strip():
                st.write(para.text)
    except:
        st.warning("⚠️ File Halaman_Persetujuan_daftar_isi.docx belum ditemukan.")
