import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/metaprogram_tab/'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'
IMG_REPO_4 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_drug_score'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram Spatial Distribution</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Visualize the spatial distribution of 14 transcriptional metaprograms within glioblastoma tissue samples. These metaprograms capture key malignant subtypes—such as mesenchymal, neural progenitor-like, and proliferative states—as well as important non-malignant populations, including immune, vascular, and glial cells. Use the interactive map to select and explore metaprograms, viewing their spatial localization alongside histology images and related molecular features such as transcription factor and pathway activities, as well as predicted drug sensitivities across each sample.")

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



st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by TF</h1>", unsafe_allow_html=True)


st.image(f'{IMG_REPO_2}/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by Pathway</h1>", unsafe_allow_html=True)

i, j = st.columns([.11, .95])
j.image(f'{IMG_REPO_3}/{option}.png')

st.markdown("<h3 style='text-align: center; color: black;'>Metaprogram by Drug2Cell</h1>", unsafe_allow_html=True)

a, b = st.columns([.11, .95])
b.image(f'{IMG_REPO_4}/{option}.png')
st.write(f'{IMG_REPO_4}/{option}.png')
