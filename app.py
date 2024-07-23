import streamlit as st

# Fungsi untuk menghitung AQI berdasarkan PM2.5
def calculate_aqi(pm):
    c = [0, 12.1, 35.5, 55.5, 150.5, 250.5, 350.5, 500.5]
    i = [0, 50, 100, 150, 200, 300, 400, 500]

    # Menghitung nilai IAQI (Individual AQI) untuk setiap parameter
    if pm <= c[1]:
        aqi = ((i[1] - i[0]) / (c[1] - c[0])) * (pm - c[0]) + i[0]
    elif pm <= c[2]:
        aqi = ((i[2] - i[1]) / (c[2] - c[1])) * (pm - c[1]) + i[1]
    elif pm <= c[3]:
        aqi = ((i[3] - i[2]) / (c[3] - c[2])) * (pm - c[2]) + i[2]
    elif pm <= c[4]:
        aqi = ((i[4] - i[3]) / (c[4] - c[3])) * (pm - c[3]) + i[3]
    elif pm <= c[5]:
        aqi = ((i[5] - i[4]) / (c[5] - c[4])) * (pm - c[4]) + i[4]
    elif pm <= c[6]:
        aqi = ((i[6] - i[5]) / (c[6] - c[5])) * (pm - c[5]) + i[5]
    elif pm <= c[7]:
        aqi = ((i[7] - i[6]) / (c[7] - c[6])) * (pm - c[6]) + i[6]
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

# Fungsi untuk menampilkan UI aplikasi menggunakan Streamlit
def main():
    st.title('Kalkulator AQI (Air Quality Index)')
    st.write('Masukkan nilai untuk setiap parameter untuk menghitung AQI:')

    # Input nilai untuk setiap parameter
    pm25_input = st.number_input('PM2.5 (µg/m³)', min_value=0.0, step=0.1, format='%f')
    pm10_input = st.number_input('PM10 (µg/m³)', min_value=0.0, step=0.1, format='%f')
    o3_input = st.number_input('O3 (ppb)', min_value=0.0, step=0.1, format='%f')
    no2_input = st.number_input('NO2 (ppb)', min_value=0.0, step=0.1, format='%f')
    so2_input = st.number_input('SO2 (ppb)', min_value=0.0, step=0.1, format='%f')
    co_input = st.number_input('CO (ppm)', min_value=0.0, step=0.1, format='%f')

    if st.button('Hitung AQI'):
        # Menghitung AQI untuk setiap parameter
        aqi_pm25 = calculate_aqi(pm25_input)
        aqi_pm10 = calculate_aqi(pm10_input)
        aqi_o3 = calculate_aqi(o3_input)
        aqi_no2 = calculate_aqi(no2_input)
        aqi_so2 = calculate_aqi(so2_input)
        aqi_co = calculate_aqi(co_input)

        # Menampilkan hasil AQI dan deskripsi kualitas udara untuk setiap parameter
        st.subheader('Hasil Perhitungan AQI:')
        st.write(f'PM2.5: {aqi_pm25} - {get_aqi_description(aqi_pm25)}')
        st.write(f'PM10: {aqi_pm10} - {get_aqi_description(aqi_pm10)}')
        st.write(f'O3: {aqi_o3} - {get_aqi_description(aqi_o3)}')
        st.write(f'NO2: {aqi_no2} - {get_aqi_description(aqi_no2)}')
        st.write(f'SO2: {aqi_so2} - {get_aqi_description(aqi_so2)}')
        st.write(f'CO: {aqi_co} - {get_aqi_description(aqi_co)}')

if __name__ == '__main__':
    main()
