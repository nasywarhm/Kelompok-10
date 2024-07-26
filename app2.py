import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Lottie URL
lottie_url = "https://lottie.host/014c7f55-c04a-4e92-b604-4c4899e3a5e9/x2n7xRzfEB.json"

# Fungsi untuk memproses lottie url
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Fungsi untuk menghitung AQI berdasarkan PM2.5
def calculate_aqi(pm25):
    c = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
    i = [0, 50, 100, 150, 200, 300, 400, 500]
    # Menghitung nilai IAQI (Individual AQI) untuk PM2.5
    if pm25 <= c[1]:
        aqi = ((i[1] - i[0]) / (c[1] - c[0])) * (pm25 - c[0]) + i[0]
    elif pm25 <= c[2]:
        aqi = ((i[2] - i[1]) / (c[2] - c[1])) * (pm25 - c[1]) + i[1]
    elif pm25 <= c[3]:
        aqi = ((i[3] - i[2]) / (c[3] - c[2])) * (pm25 - c[2]) + i[2]
    elif pm25 <= c[4]:
        aqi = ((i[4] - i[3]) / (c[4] - c[3])) * (pm25 - c[3]) + i[3]
    elif pm25 <= c[5]:
        aqi = ((i[5] - i[4]) / (c[5] - c[4])) * (pm25 - c[4]) + i[4]
    elif pm25 <= c[6]:
        aqi = ((i[6] - i[5]) / (c[6] - c[5])) * (pm25 - c[5]) + i[5]
    elif pm25 <= c[7]:
        aqi = ((i[7] - i[6]) / (c[7] - c[6])) * (pm25 - c[6]) + i[6]
    else:
        aqi = 500

    return round(aqi)

# Fungsi untuk mendapatkan deskripsi kualitas udara berdasarkan nilai AQI
def get_aqi_description(aqi_value):
    if aqi_value <= 50:
        return "Kualitas udara baik; tidak ada atau sedikit risiko bagi kesehatan."
    elif aqi_value <= 100:
        return "Kualitas udara sedang; risiko kesehatan bagi kelompok sensitif."
    elif aqi_value <= 150:
        return "Kualitas udara tidak sehat bagi kelompok sensitif."
    elif aqi_value <= 200:
        return "Kualitas udara tidak sehat; bagi semua orang dapat terpengaruh."
    elif aqi_value <= 300:
        return "Kualitas udara sangat tidak sehat; efek serius pada kesehatan."
    else:
        return "Kualitas udara berbahaya; risiko kesehatan darurat."

# Fungsi untuk mendapatkan warna berdasarkan nilai AQI
def get_aqi_color(aqi_value):
    if aqi_value <= 50:
        return "green"  # warna untuk AQI baik
    elif aqi_value <= 100:
        return "yellow"  # warna untuk AQI sedang
    elif aqi_value <= 150:
        return "orange"  # warna untuk AQI tidak sehat
    elif aqi_value <= 200:
        return "red"  # warna untuk AQI sangat tidak sehat
    else:
        return "purple"  # warna untuk AQI berbahaya

# Fungsi untuk mendapatkan tindakan yang harus diambil berdasarkan nilai AQI
def get_aqi_action(aqi_value):
    if aqi_value <= 50:
        return "Tidak perlu tindakan khusus."
    elif aqi_value <= 100:
        return "Kelompok sensitif sebaiknya mengurangi aktivitas luar ruangan."
    elif aqi_value <= 150:
        return "Kelompok sensitif sebaiknya menghindari aktivitas luar ruangan. Orang lain sebaiknya mengurangi aktivitas luar ruangan."
    elif aqi_value <= 200:
        return "Semua orang sebaiknya menghindari aktivitas luar ruangan."
    elif aqi_value <= 300:
        return "Semua orang sebaiknya menghindari aktivitas luar ruangan dan menggunakan masker."
    else:
        return "Semua orang sebaiknya tetap di dalam ruangan dan menggunakan pembersih udara jika tersedia."

# Fungsi untuk menampilkan UI aplikasi menggunakan Streamlit
def main():
    # Mengatur gaya CSS untuk ukuran font dan latar belakang
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://www.example.com/your-background-image.jpg'); /* Ganti dengan URL gambar latar belakang Anda */
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #ffffff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }
        .description {
            font-size: 18px;
            color: #ffffff;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
        }
        .sidebar .sidebar-content {
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # List of options for the select box
    options = ('Home', 'Definisi', 'Kalkulator AQI')

    # Display a select box in the sidebar
    selected_option = st.sidebar.selectbox('Main Menu', options)

    # Perform actions based on the selected option
    if selected_option == 'Home':
        # Pembuatan 2 kolom
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown('<div class="title">Project LPK Kelompok 10</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">1. Aura Shyfa (2330490)</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">2. Nasywa Rahmadani H (2330518)</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">3. Nazmi Asyam (2330519)</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">4. Shafiqah Fauziah (2330530)</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">5. Selviana Valia (2230471)</div>', unsafe_allow_html=True)
            st.markdown('<div class="description">6. Zaki Raditya (2330534)</div>', unsafe_allow_html=True)

        # Memproses animasi lottie
        lottie_json = load_lottie_url(lottie_url)
        # Menampilkan animasi lottie
        with col2:
            if lottie_json is not None:
                st_lottie(lottie_json)
            else:
                st.write("Failed to load Lottie animation.")

    elif selected_option == 'Definisi':
        st.markdown('<div class="title">Definisi PM2.5 dan AQI</div>', unsafe_allow_html=True)

        st.markdown('<div class="header">Definisi PM2.5</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="description">
        PM2.5 adalah singkatan dari Particulate Matter 2.5, yang merujuk pada partikel udara dengan diameter kurang dari 2,5 mikrometer. Partikel ini sangat kecil dan dapat masuk ke dalam paru-paru dan bahkan aliran darah, menyebabkan berbagai masalah kesehatan termasuk penyakit pernapasan dan kardiovaskular.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="header">Definisi AQI</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="description">
        Air Quality Index (AQI) adalah angka yang digunakan untuk menggambarkan tingkat polusi udara. AQI dihitung berdasarkan konsentrasi beberapa polutan udara seperti PM2.5, PM10, ozon, karbon monoksida, dan nitrogen dioksida.
        </div>
        """, unsafe_allow_html=True)

    elif selected_option == 'Kalkulator AQI':
        st.markdown('<div class="title">Kalkulator AQI</div>', unsafe_allow_html=True)
        pm25 = st.number_input('Masukkan nilai PM2.5:', min_value=0.0, max_value=1000.0, value=0.0, step=0.1)
        
        if pm25 >= 0:
            aqi_value = calculate_aqi(pm25)
            aqi_description = get_aqi_description(aqi_value)
            aqi_color = get_aqi_color(aqi_value)
            aqi_action = get_aqi_action(aqi_value)
            
            st.markdown(f'<div class="description" style="color: {aqi_color};">AQI: {aqi_value}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="description">{aqi_description}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="description">{aqi_action}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #87CEEB, #B0E57C); /* Gradasi dari biru ke hijau */
        color: #ffffff;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .header {
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    .description {
        font-size: 18px;
        color: #ffffff;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
