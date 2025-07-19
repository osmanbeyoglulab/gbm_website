import streamlit as st
from persist import persist



st.markdown("<h2 style='text-align: center; color: black;'>Transcription Factor (TF) Activity Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Visualize spatially inferred transcription factor activities across glioblastoma samples using the STAN framework. Examine how TF activities distribute across the tissue architecture, overlaid on histology images. Comparative violin plots display TF activity across transcriptional metaprograms, revealing how regulation differs between malignant and non-malignant states and highlighting key regulators of specific tumor niches. Use the search box to enter TF names and the sample selector to browse different patient tumors.")

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_tf_tab/'

file = open('text_files/spatial_tf_activity_names.txt', 'r')
list = file.read().splitlines()

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)


a, b = st.columns(2)
df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = a.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 


option2 = b.selectbox(
    'TF',
    list) 
    
# a.subheader('Spatial Plot')            
a.image(f'{IMG_REPO}/spatial_tf_activity/{option2}/{option}.png')
# b.subheader('Violin Plot')
b.image(f'{IMG_REPO}/violin_tf_activity/{option2}/{option}.png')


IMG_REPO2 = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
st.markdown("<h3 style='text-align: center; color: black;'>TF Activity across Metaprograms</h3>", unsafe_allow_html=True)
st.image(f'{IMG_REPO2}/across_metaprogram_top_transcriptions_per_sample/{option}.png')

