import streamlit as st

st.title("📑 Dokumen Utama")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Halaman Judul", "Lembar Persetujuan", "Pernyataan Orisinalitas", "Kata Pengantar", "Daftar Isi"])

with tab1:
    st.subheader("Halaman Judul")
    st.markdown("""
    **PENENTUAN NILAI AMBANG BATAS INDEKS STABILITAS ATMOSFER**  
    Dengan Data METAR di Stasiun Meteorologi Juanda  
    Ferri Kusuma - 14.22.0003  
    STMKG Tangerang, 2025
    """)

with tab2:
    st.subheader("Lembar Persetujuan")
    st.write("Berisi tanda tangan dosen pembimbing dan penguji.")

with tab3:
    st.subheader("Pernyataan Orisinalitas")
    st.write("Berisi pernyataan asli karya ilmiah.")

with tab4:
    st.subheader("Kata Pengantar")
    st.write("Berisi kata pengantar penulis.")

with tab5:
    st.subheader("Daftar Isi, Daftar Gambar, Daftar Tabel, Daftar Lampiran")
    st.write("Berisi daftar isi, tabel, gambar, dan lampiran skripsi.")
