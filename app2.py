import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Lottie URL
lottie_url = "https://lottie.host/014c7f55-c04a-4e92-b604-4c4899e3a5e9/x2n7xRzfEB.json"

# Function to load Lottie animation from URL
def load_lottie_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None

# Function to calculate AQI based on PM2.5
def calculate_aqi(pm25):
    c = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
    i = [0, 50, 100, 150, 200, 300, 400, 500]
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

# Function to get AQI description
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

# Function to get AQI color
def get_aqi_color(aqi_value):
    if aqi_value <= 50:
        return "green"
    elif aqi_value <= 100:
        return "yellow"
    elif aqi_value <= 150:
        return "orange"
    elif aqi_value <= 200:
        return "red"
    else:
        return "purple"

# Function to get AQI action
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

# Custom CSS
def inject_css():
    st.markdown("""
        <style>
        .big-font {
            font-size: 24px !important;
        }
        .header-font {
            font-size: 32px !important;
            font-weight: bold;
        }
        .subheader-font {
            font-size: 28px !important;
        }
        .normal-font {
            font-size: 20px !important;
        }
        </style>
        """, unsafe_allow_html=True)

# Function to display the UI
def main():
    inject_css()  # Inject CSS styles

    options = ('Home', 'Definisi', 'Hubungan PM2.5 dan AQI', 'Kalkulator AQI')
    selected_option = st.sidebar.selectbox('Main Menu', options)

    if selected_option == 'Home':
        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown("<div class='header-font'>Project LPK Kelompok 10</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>1. Aura Shyfa (2330490)</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>2. Nasywa Rahmadani H (2330518)</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>3. Nazmi Asyam (2330519)</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>4. Shafiqah Fauziah (2330530)</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>5. Selviana Valia (2230471)</div>", unsafe_allow_html=True)
            st.markdown("<div class='normal-font'>6. Zaki Raditya (2330534)</div>", unsafe_allow_html=True)

        with col2:
            lottie_json = load_lottie_url(lottie_url)
            if lottie_json is not None:
                st_lottie(lottie_json)
            else:
                st.write("Failed to load Lottie animation.")

    elif selected_option == 'Definisi':
        st.markdown("<div class='header-font'>Definisi PM2.5 dan AQI</div>", unsafe_allow_html=True)

        st.markdown("<div class='subheader-font'>PM2.5</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='normal-font'>
            PM2.5 adalah singkatan dari Particulate Matter 2.5, yang merujuk pada partikel udara dengan diameter kurang dari 2,5 mikrometer. 
            Partikel ini sangat kecil dan dapat masuk ke dalam paru-paru dan bahkan aliran darah, menyebabkan berbagai masalah kesehatan termasuk 
            penyakit pernapasan dan kardiovaskular.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='subheader-font'>AQI</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='normal-font'>
            Air Quality Index (AQI) adalah indeks yang digunakan untuk menggambarkan kualitas udara berdasarkan tingkat polutan tertentu. 
            Nilai AQI berkisar dari 0 hingga 500, dengan kategori yang menunjukkan tingkat risiko kesehatan yang terkait. AQI membantu masyarakat 
            memahami seberapa bersih atau tercemarnya udara di wilayah mereka dan tindakan pencegahan apa yang perlu diambil.
            </div>
            """, unsafe_allow_html=True)

    elif selected_option == 'Hubungan PM2.5 dan AQI':
        st.markdown("<div class='header-font'>Hubungan PM2.5 dan AQI</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='normal-font'>
            PM2.5 dan AQI memiliki hubungan langsung, karena AQI dihitung berdasarkan konsentrasi PM2.5 di udara. Semakin tinggi konsentrasi PM2.5, 
            semakin tinggi nilai AQI, dan ini menunjukkan kualitas udara yang semakin buruk. Berikut adalah rentang nilai PM2.5 dan dampaknya terhadap AQI:
            
            - **0 - 12 µg/m³**: AQI berada pada kategori baik (0 - 50).
            - **12.1 - 35.5 µg/m³**: AQI berada pada kategori sedang (51 - 100).
            - **35.6 - 55.5 µg/m³**: AQI berada pada kategori tidak sehat bagi kelompok sensitif (101 - 150).
            - **55.6 - 150.5 µg/m³**: AQI berada pada kategori tidak sehat (151 - 200).
            - **150.6 - 250.5 µg/m³**: AQI berada pada kategori sangat tidak sehat (201 - 300).
            - **250.6 µg/m³ dan lebih**: AQI berada pada kategori berbahaya (301 - 500).
            </div>
            """, unsafe_allow_html=True)

    elif selected_option == 'Kalkulator AQI':
        st.markdown("<div class='header-font'>Kalkulator AQI (Air Quality Index)</div>", unsafe_allow_html=True)
        st.markdown("<div class='normal-font'>Masukkan nilai PM2.5 untuk menghitung AQI:</div>", unsafe_allow_html=True)

        pm25_input = st.number_input('PM2.5 (µg/m³)', min_value=0.0, step=0.1, format='%f')

        if st.button('Hitung AQI'):
            if pm25_input:
                aqi_value = calculate_aqi(pm25_input)
                aqi_description = get_aqi_description(aqi_value)
                aqi_color = get_aqi_color(aqi_value)
                aqi_action = get_aqi_action(aqi_value)
                st.markdown(f"<div class='subheader-font'>Nilai AQI yang dihitung adalah: {aqi_value}</div>", unsafe_allow_html=True)
                st.markdown(f'<p style="color: {aqi_color}; font-size: 20px;">{aqi_description}</p>', unsafe_allow_html=True)
                st.markdown(f'<p style="font-size: 20px;">Tindakan yang harus dilakukan: {aqi_action}</p>', unsafe_allow_html=True)

                st.markdown("<div class='subheader-font'>Tabel Nilai AQI:</div>", unsafe_allow_html=True)
                st.image("imgweb/aqi.png", use_column_width=True)

if __name__ == '__main__':
    main()
