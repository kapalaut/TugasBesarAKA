import streamlit as st
import time
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

st.title("Analisis perbandingan kompleksitas algoritma iteratif dan rekursif dalam pencarian skor tertinggi pada data Ujian Tulis Berbasis Komputer(UTBK).")

def max_iteratif(A):
    maks = A[0]
    for i in range(1, len(A)):
        if A[i] > maks:
            maks = A[i]
    return maks

def max_rekursif(A, kiri, kanan):
    if kiri == kanan:
        return A[kiri]
    
    mid = (kiri + kanan) // 2
    
    max_kiri = max_rekursif(A, kiri, mid)
    max_kanan = max_rekursif(A, mid + 1, kanan)
    
    if max_kiri > max_kanan:
        return max_kiri
    else:
        return max_kanan

st.header("1. Pengujian Input")

tingkat = st.radio("Pilih jumlah data (n):", 
                   ["Sekolah (n=100)", "Kabupaten (n=1.000)", "Provinsi (n=25.000)", "Nasional (n=100.000)"])

if tingkat == "Sekolah (n=100)":
    n = 100
elif tingkat == "Kabupaten (n=1.000)":
    n = 1000
elif tingkat == "Provinsi (n=25.000)":
    n = 25000
else:
    n = 100000

data = [random.randint(0, 1000) for _ in range(n)]

if st.button("Jalankan Perbandingan"):
    
    start = time.perf_counter()
    hasil_iteratif = max_iteratif(data)
    waktu_iteratif = (time.perf_counter() - start) * 1000 
    
    start = time.perf_counter()
    hasil_rekursif = max_rekursif(data, 0, len(data)-1)
    waktu_rekursif = (time.perf_counter() - start) * 1000
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(f"**Iteratif** (n={n})")
        st.write(f"Maks: {hasil_iteratif}")
        st.write(f"Waktu: **{waktu_iteratif:.5f} ms**")
    
    with col2:
        st.info(f"**Rekursif** (n={n})")
        st.write(f"Maks: {hasil_rekursif}")
        st.write(f"Waktu: **{waktu_rekursif:.5f} ms**")

st.markdown("---")

st.header("2. Grafik Order of Growth")

max_test_n = st.slider("Maksimum n:", min_value=100, max_value=100000, value=1000, step=100)

if st.button("Buat Grafik"):
        
    step_n = int(max_test_n / 20) if max_test_n > 200 else 10
    
    sizes = range(step_n, max_test_n + 1, step_n)
    times_iter = []
    times_rec = []
    
    progress_bar = st.progress(0)
    
    for i, size in enumerate(sizes):
        progress_bar.progress((i + 1) / len(sizes))
        
        temp_data = [random.randint(0, 10000) for _ in range(size)]
        
        start = time.perf_counter()
        max_iteratif(temp_data)
        times_iter.append((time.perf_counter() - start) * 1000) 
        
        start = time.perf_counter()
        max_rekursif(temp_data, 0, len(temp_data)-1)
        times_rec.append((time.perf_counter() - start) * 1000) 
            
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(sizes, times_iter, marker='o', linestyle='-', color='blue', label='Iteratif O(n)')
    ax.plot(sizes, times_rec, marker='x', linestyle='--', color='red', label='Rekursif O(n)')
    
    ax.set_title(f"Runtime: Iteratif vs Rekursif")
    ax.set_xlabel("Jumlah Input (n)")
    ax.set_ylabel("Waktu Eksekusi (ms)")
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    
    st.pyplot(fig)
  
 
with st.expander("Source Code Algoritma"):
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("**1. Algoritma Iteratif**")
        st.code("""
def max_iteratif(A):
    maks = A[0]
    for i in range(1, len(A)):
        if A[i] > maks:
            maks = A[i]
    return maks
        """, language="python")
        
    with c2:
        st.markdown("**2. Algoritma Rekursif**")
        st.code("""
def max_rekrusif(A, kiri, kanan):
    if kiri == kanan:
        return A[kiri]
    
    mid = (kiri + kanan) // 2
    
    max_kiri = max_rekursif(A, kiri, mid)
    max_kanan = max_rekursif(A, mid + 1, kanan)
    
    if max_kiri > max_kanan:
        return max_kiri
    else:
        return max_kanan
        """, language="python")