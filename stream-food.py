import pickle
import streamlit as st

# Membaca model
try:
    with open('food_model.sav', 'rb') as file:
        food_model = pickle.load(file)
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan file berada di jalur yang benar.")
except Exception as e:
    st.error(f"Error saat memuat model: {e}")

# Judul web
st.title('Prediksi Kepuasan Pelanggan')

# Input data dengan contoh angka valid untuk pengujian
Age = st.text_input('Age', '1')
Feedback = st.text_input('Feedback', '0')
Monthly_Income = st.text_input('Monthly Income', '1')
Marital_Status = st.text_input('Marital Status', '0')

Kepuasan = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Convert input to appropriate data types
        Age = st.text_input('Age', '1')
        Feedback = st.text_input('Feedback', '0')
        Monthly_Income = st.text_input('Monthly Income', '1')
        Marital_Status = st.text_input('Marital Status', '0')

        # Melakukan prediksi
        Satisfaction = resto_model.predict([[Age, Feedback, Monthly_Income, Marital_Status]])

        # Menentukan kategori harga berdasarkan prediksi
        if Satisfaction[0] == 1:
            Kepuasan = 'Yes'
        else Satisfaction[0] == 2:
            Kepuasan = 'No'
        
        st.success(Kepuasan)

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
    