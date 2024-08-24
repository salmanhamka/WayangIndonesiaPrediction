import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



st.set_page_config(
    page_title = 'WAYANGS INDONESIAN TYPE - EDA',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    #membuat title
    st.title('TIPE WAYANG DI INDONESIA')
    
    
    #membuat subheader
    st.subheader('Cintai Wayang Sebagai Budaya Indonesia')
    
    #menambahkan gambar
    st.image('https://imgcdn.solopos.com/@space/2022/10/Faris-Wibisono-Wonogiri.jpg')
    caption= ('Wayang Type Indonesia')  
    
    #menambahkan deskripsi
    st.write('# Dibuat oleh Salman Hamka De Qais')
        
    
    #membuat garis
    st.markdown('---')
    
    
    #magicsyntax
    '''
    pada page ini, penuis akan melakukan explorasi sederhana, contoh gambar dibawah ini adalah gambar dari salah satu wayang di Indonesia
    
    '''    
    #menambahkan gambar
    st.image('output.png')
    
        
if __name__ == '__main__':
    run()
    
