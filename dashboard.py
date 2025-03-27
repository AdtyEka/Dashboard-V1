import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import toml

# Baca file config.toml
config = toml.load("config.toml")

# judul 
st.markdown("<h1 style='text-align: center;'>Proyek Analisis Data - Bike</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <hr style="border: 2px solid #FF6347; margin-top: 20px; margin-bottom: 20px;">
    """, unsafe_allow_html=True
)

with st.sidebar:# membuat sid-bar untuk penampilan tanggal
    # Menambahkan logo 
    st.image("logo data.webp")
    st.markdown(
    """
    <hr style="border: 2px solid #FF6347; margin-top: 20px; margin-bottom: 20px;">
    """, unsafe_allow_html=True
    )
    st.write ("Bio Data : ")
    st.markdown (''' - Aditya Eka Narayan
                ''')
    st.markdown (''' - 19 Tahun 
                ''')
    st.markdown (''' - Mahasiswa ( UDINUS )
                ''')
    st.markdown (''' - Teknik Informatika  
                ''')
    st.write ("Tentang : ")
    st.write ("Saya seorang mahasiswa semester 1 yang sedang memulai perjalanan dalam dunia analisis data. Dengan ketertarikan dalam mengolah data, Saya mulai belajar tentang statistik, pemrograman, dan alat-alat yang digunakan dalam analisis data seperti Python, Pandas, dan berbagai teknik visualisasi data. Sebagai mahasiswa, Saya sangat antusias untuk mendalami topik-topik seperti machine learning, analisis prediktif, dan teknik-teknik analisis data lainnya yang akan membentuknya menjadi seorang data analyst yang kompeten di masa depan ")
    
    
# Membaca file CSV
data_clean_df = pd.read_csv("all_data_bike.csv")

st.markdown('''
            <h5> Pertanyaan 1 : </h5>
            <h5> Jam berapa pengguna aktif lebih sering menyewa sepeda dibandingkan pengguna non-aktif ?</h5>
            ''', unsafe_allow_html=True)

# Fungsi untuk membuat data pertanyaan 1
def create_data_pertanyaan1_df(df):
    data_pertanyaan1_df = df.groupby(by=['Jam']).agg({
        'Total Penyewa_y': 'sum',
        'non aktif_y': 'sum',
        'aktif_y': 'sum'
    }).reset_index()

    return data_pertanyaan1_df


# Memproses data menggunakan fungsi
data_pertanyaan1_df = create_data_pertanyaan1_df(data_clean_df)

# Membuat plot dengan barplot
fig, ax = plt.subplots(figsize=(12, 6))

# Barplot untuk Total Penyewa, Pengguna Aktif, dan Pengguna Non-Aktif
df_melted = data_pertanyaan1_df.melt(id_vars=['Jam'], 
                                     value_vars=['Total Penyewa_y', 'aktif_y', 'non aktif_y'], 
                                     var_name='Kategori', 
                                     value_name='Jumlah')

sns.barplot(x='Jam', y='Jumlah', hue='Kategori', data=df_melted, ax=ax)

# Menambahkan judul dan label
ax.set_title('Pola Penyewaan Sepeda per Jam', fontweight='bold', pad=20)
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah')
ax.legend(title='Kategori')

# Menampilkan plot di Streamlit
st.pyplot(fig)

# Jawaban Pertanyaan 1
st.write("")
st.markdown('''
            <p> Jawaban Pertanyaan 1 : </p>
            ''', unsafe_allow_html=True)
st.write ("1. Pola Umum Penyewaan Sepeda Penyewaan sepeda memiliki pola yang berfluktuasi sepanjang hari, dengan beberapa jam menunjukkan lonjakan signifikan Secara keseluruhan, jumlah penyewaan sepeda tertinggi terjadi pada jam-jam tertentu, yang kemungkinan besar berhubungan dengan aktivitas harian masyarakat, seperti jam berangkat dan pulang kerja.")
st.write ("2. Perbandingan Antara Pengguna Aktif dan Non-Aktif Pengguna aktif cenderung lebih dominan dalam jumlah penyewaan dibandingkan pengguna non-aktif, terutama pada jam-jam sibuk. Pengguna non-aktif tetap berkontribusi terhadap total penyewaan, tetapi jumlahnya lebih kecil dibandingkan pengguna aktif. Puncak penyewaan sepeda oleh pengguna aktif terjadi pada waktu-waktu tertentu, yang mengindikasikan bahwa mereka lebih sering menyewa sepeda pada saat tertentu dalam sehari.")
st.markdown ('''3. Jam Sibuk (Peak Hours) dalam Penyewaan Sepeda Dari grafik, terdapat pola jam sibuk dalam penyewaan sepeda: 
                Pagi Hari (06:00 - 09:00)
                Terjadi lonjakan signifikan dalam penyewaan sepeda, kemungkinan besar berhubungan dengan jam berangkat kerja atau sekolah. 
                Pada jam ini, pengguna aktif lebih dominan, yang dapat menunjukkan bahwa mereka lebih sering menggunakan sepeda untuk keperluan rutin seperti transportasi ke kantor/sekolah. Sore Hari (17:00 - 20:00)
                Kembali terjadi peningkatan jumlah penyewaan, yang mungkin berkaitan dengan jam pulang kerja atau aktivitas santai sore hari. Seperti pada pagi hari, pengguna aktif tetap menjadi kelompok dominan dalam penyewaan sepeda.
                ''')
st.markdown ('''4. Jam dengan Penyewaan Rendah
                Malam Hari (Setelah 21:00)
                Penyewaan sepeda mulai menurun drastis setelah pukul 21:00. Hal ini mungkin disebabkan oleh berkurangnya mobilitas masyarakat pada malam hari.
                Siang Hari (10:00 - 15:00)
                Terdapat periode yang lebih tenang dengan jumlah penyewaan yang relatif lebih rendah dibandingkan pagi dan sore hari. Ini bisa menunjukkan bahwa sebagian besar masyarakat tidak menggunakan sepeda saat jam kerja atau jam sekolah.
                ''')

st.markdown('''
            <h5> Pertanyaan 2 : </h5>
            <h5> Bagaimana pola penyewaan sepeda di pagi hari (06:00 - 09:00) dibandingkan dengan malam hari (18:00 - 21:00)?</h5>
            ''', unsafe_allow_html=True)

def create_data_pertanyaan2_df(df, jam_mulai, jam_selesai):
    # Memilih data berdasarkan rentang jam
    filtered_df = df[(df['Jam'] >= jam_mulai) & (df['Jam'] <= jam_selesai)]
    
    # Mengelompokkan data berdasarkan jam dan menghitung total penyewa dan pengguna aktif/non-aktif
    data_pertanyaan2_df = filtered_df.groupby(by=['Jam']).agg({
        'Total Penyewa_y': 'sum',
        'non aktif_y': 'sum',
        'aktif_y': 'sum'
    }).reset_index()
    
    return data_pertanyaan2_df

# Pilih apakah ingin menganalisis data pagi atau malam
waktu_pilih = st.radio("Pilih waktu analisis:", ('Pagi (06:00 - 09:00)', 'Malam (18:00 - 21:00)'))

# Menentukan jam mulai dan jam selesai berdasarkan pilihan
if waktu_pilih == 'Pagi (06:00 - 09:00)':
    jam_mulai, jam_selesai = 6, 9
else:
    jam_mulai, jam_selesai = 18, 21

# Memproses data menggunakan fungsi
data_pertanyaan2_df = create_data_pertanyaan2_df(data_clean_df, jam_mulai, jam_selesai)

# Menampilkan DataFrame yang sudah dikelompokkan
st.write("Data Analisis Penyewaan Sepeda")
st.dataframe(data_pertanyaan2_df)

# Membuat plot bar chart untuk data
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='Jam', y='Total Penyewa_y', data=data_pertanyaan2_df, color='blue', ax=ax, label='Total Penyewa')
sns.barplot(x='Jam', y='aktif_y', data=data_pertanyaan2_df, color='green', ax=ax, label='Pengguna Aktif')
sns.barplot(x='Jam', y='non aktif_y', data=data_pertanyaan2_df, color='red', ax=ax, label='Pengguna Non-Aktif')

# Menambahkan judul dan label
ax.set_title(f'Pola Penyewaan Sepeda ({waktu_pilih})', fontweight='bold', pad=20)
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewaan')
ax.legend(title="Kategori")

# Menampilkan plot di Streamlit
st.pyplot(fig)

st.markdown('''
            <p> Jawaban Pertanyaan 2 : </p>
            ''', unsafe_allow_html=True)

st.write ('''Pagi (06:00 - 09:00)
Jumlah Penyewa:

- Pada periode pagi, terlihat bahwa ada peningkatan jumlah penyewaan sepeda yang signifikan pada jam-jam tertentu, dengan jumlah penyewa yang lebih tinggi pada jam-jam tertentu (misalnya sekitar jam 7-8 pagi).
Total Penyewa menunjukkan tren peningkatan jumlah penyewaan pada jam-jam sibuk pagi, kemungkinan karena banyak orang yang menggunakan sepeda untuk beraktivitas di luar, seperti pergi ke tempat kerja atau sekolah.
Pengguna Aktif vs Non-Aktif:

- Pengguna Aktif: Ini adalah kategori pengguna yang telah melakukan pendaftaran atau menggunakan aplikasi secara reguler. Pada jam pagi, grafik menunjukkan bahwa pengguna aktif cenderung lebih banyak dibandingkan dengan pengguna non-aktif pada beberapa jam tertentu.

- Pengguna Non-Aktif: Pada beberapa jam tertentu, meskipun ada sejumlah besar pengguna aktif, pengguna non-aktif masih memiliki kontribusi signifikan terhadap jumlah total penyewaan sepeda.
''')

st.write ('''Malam (18:00 - 21:00)
Jumlah Penyewa:

- Pada periode malam, grafik menunjukkan penurunan jumlah penyewaan sepeda dibandingkan dengan pagi hari. Ini mungkin disebabkan oleh fakta bahwa banyak orang tidak menggunakan sepeda pada malam hari setelah aktivitas mereka selesai.
Total Penyewa menunjukkan bahwa penyewaan sepeda lebih sedikit dibandingkan dengan pagi hari, yang mungkin karena waktu malam yang lebih tenang dan lebih sedikitnya aktivitas yang membutuhkan sepeda.
Pengguna Aktif vs Non-Aktif:

- Pengguna Aktif: Pada malam hari, meskipun jumlah total penyewa lebih rendah, pengguna aktif masih menunjukkan kontribusi yang signifikan.

- Pengguna Non-Aktif: Di sisi lain, kategori pengguna non-aktif mungkin lebih rendah pada malam hari, namun tetap ada beberapa pengguna yang masih menggunakan sepeda meskipun mereka tidak terdaftar sebagai pengguna aktif.''')

st.markdown('''
            <h5> Pertanyaan 3 : </h5>
            <h5> Bagaimana distribusi penyewaan sepeda berdasarkan hari dalam seminggu ?</h5>
            ''', unsafe_allow_html=True)

# Fungsi untuk menghitung total penyewaan per hari dalam seminggu
def calculate_daily_rentals(df):
    # Pastikan kolom 'dteday' adalah tipe datetime
    df['dteday'] = pd.to_datetime(df['dteday'])
    
    # Hitung total penyewaan per hari dalam seminggu
    daily_rentals = df.groupby(by=df['dteday'].dt.day_name())['Total Penyewa_x'].sum().sort_values(ascending=False)
    
    return daily_rentals

# Memproses data menggunakan fungsi
daily_rentals = calculate_daily_rentals(data_clean_df)

# Menampilkan DataFrame yang sudah dikelompokkan
st.write("Total Penyewaan Sepeda per Hari dalam Seminggu")
st.dataframe(daily_rentals)

# Membuat plot bar chart untuk distribusi penyewaan per hari
fig, ax = plt.subplots(figsize=(10, 6))

# Menggambar bar chart
sns.barplot(x=daily_rentals.index, y=daily_rentals.values, ax=ax, palette='viridis')

# Menambahkan judul dan label
ax.set_title('Distribusi Penyewaan Sepeda Berdasarkan Hari dalam Seminggu', fontweight='bold', pad=20)
ax.set_xlabel('Hari')
ax.set_ylabel('Total Penyewaan')

# Rotasi label sumbu x agar mudah dibaca
plt.xticks(rotation=45, ha='right')

# Menampilkan plot di Streamlit
st.pyplot(fig)

st.markdown('''
            <p> Jawaban Pertanyaan 3 : </p>
            ''', unsafe_allow_html=True)

st.write (''' Hari Jumat sebagai Hari Penyewaan Puncak:

- Hari Jumat tampaknya merupakan hari dengan jumlah penyewaan sepeda tertinggi dalam seminggu. Ini bisa disebabkan oleh beberapa faktor, seperti orang-orang yang menggunakan sepeda untuk bepergian menuju tempat kerja, sekolah, atau aktivitas lain menjelang akhir pekan.

- Kemungkinan faktor utama: Banyak orang yang menggunakan sepeda untuk beraktivitas di luar ruangan, seperti olahraga, berkeliling kota, atau berkumpul dengan teman-teman.
''' )

st.markdown(
    """
    <hr style="border: 2px solid #FF6347; margin-top: 20px; margin-bottom: 20px;">
    """, unsafe_allow_html=True
)

st.markdown('''
            <h5> Bagaiamana Kesan Anda Dengan Dashboard ini ?</h5>
            ''', unsafe_allow_html=True)

values = st.slider(
    label='Beri Nilai Untuk Dashboard Di Atas',
    min_value=0, max_value=100)
st.write('Values:', values) # slide angka 1 - 100 seperti pada volume  


st.caption('Copyright (c) 2024 Aditya Eka Narayan') # caption / Footer
