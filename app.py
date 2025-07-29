import streamlit as st

st.set_page_config(page_title="Dokumentasi Skripsi Ferri Kusuma", layout="wide")

# Tampilkan logo di header
st.image("assets/logo_stmkg.jpg", width=120)

st.title("📖 PENENTUAN NILAI AMBANG BATAS INDEKS STABILITAS ATMOSFER")
st.subheader("Dengan Data METAR di Stasiun Meteorologi Juanda")

st.write("---")
st.markdown("""
### 👤 Identitas Penulis
- **Nama:** Ferri Kusuma  
- **NPT:** 14.22.0003  
- **Program Studi:** Sarjana Terapan Meteorologi  
- **Sekolah Tinggi Meteorologi Klimatologi dan Geofisika (STMKG)**  
- **Tangerang, 2025**
""")

st.write("### 👨‍🏫 Tim Pembimbing dan Penguji")
st.markdown("""
- **Dosen Pembimbing:** Dr. Yosafat Donni Haryanto, SP., M.Si.  
  NIP. 197612281999031002  

- **Dosen Penguji I:** Ahmad Fadlan, SST., M.Si.  
  NIP. 199003092010121001  

- **Dosen Penguji II:** Latifah Nurul Qomariyatuzzamzami, SPd., M.PFis.  
  NIP. 19900729 201502 2002
""")

st.write("---")
st.info("Gunakan menu di sidebar untuk menavigasi seluruh isi skripsi.")
