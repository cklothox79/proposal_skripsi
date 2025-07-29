import streamlit as st

st.title("📚 Isi Skripsi")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Bab I", "Bab II", "Bab III", "Bab IV", "Bab V"])

with tab1:
    st.subheader("Bab I - Pendahuluan")
    st.write("Berisi latar belakang, rumusan masalah, tujuan, manfaat penelitian.")

with tab2:
    st.subheader("Bab II - Dasar Teori")
    st.write("Berisi teori-teori dan tinjauan pustaka.")

with tab3:
    st.subheader("Bab III - Metode Penelitian")
    st.write("Berisi data, metode, prosedur penelitian, dan tahapan analisis.")

with tab4:
    st.subheader("Bab IV - Hasil dan Pembahasan")
    st.write("Berisi hasil analisis, tabel, grafik, pembahasan hasil penelitian.")

with tab5:
    st.subheader("Bab V - Kesimpulan dan Saran")
    st.write("Berisi kesimpulan akhir dan saran penelitian.")
