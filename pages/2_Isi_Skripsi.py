import streamlit as st
from docx import Document

st.title("📚 Isi Skripsi")

try:
    doc = Document("docs/Bab_1_sampai_5.docx")
    content = [para.text for para in doc.paragraphs if para.text.strip() != ""]

    tabs = st.tabs(["Bab I", "Bab II", "Bab III", "Bab IV", "Bab V"])

    bab_isi = {"Bab I": [], "Bab II": [], "Bab III": [], "Bab IV": [], "Bab V": []}
    current_bab = "Bab I"
    for line in content:
        if "BAB I" in line.upper():
            current_bab = "Bab I"
        elif "BAB II" in line.upper():
            current_bab = "Bab II"
        elif "BAB III" in line.upper():
            current_bab = "Bab III"
        elif "BAB IV" in line.upper():
            current_bab = "Bab IV"
        elif "BAB V" in line.upper():
            current_bab = "Bab V"
        bab_isi[current_bab].append(line)

    for tab, bab in zip(tabs, bab_isi.keys()):
        with tab:
            for paragraf in bab_isi[bab]:
                st.write(paragraf)

except:
    st.warning("⚠️ File Bab_1_sampai_5.docx belum ditemukan.")
