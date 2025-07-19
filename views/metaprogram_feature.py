import streamlit as st
import urllib.request
from persist import persist
# from views.utils import get_sample_metaprograms

IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'


st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram-Associated Features</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Use the interactive map to select and explore metaprogram related molecular features such as transcription factor and pathway activities, as well as predicted drug sensitivities across each sample.")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()
option = st.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 



st.markdown("<h3 style='text-align: center; color: black;'>TF Activity across Metaprograms</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_metaprogram_top_transcriptions_per_sample/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Pathway Activity across Metaprograms</h1>", unsafe_allow_html=True)

i, j = st.columns([.11, .95])
j.image(f'{IMG_REPO}/across_metaprogram_top_pathways_per_sample/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Drug2Cell Scores across Metaprogram</h1>", unsafe_allow_html=True)
st.image(f'{IMG_REPO}/across_metaprogram_top_drugs_per_sample/{option}.png')


