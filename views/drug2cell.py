import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms
import pandas as pd
from utils import url_is_alive

# IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_drug2cell'
IMG_REPO2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/violin_drug2cell'
IMG_REPO_ren = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/ren_drug'
IMG_REPO_son = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/sonpatki_drug'

st.markdown("<h2 style='text-align: center; color: black;'>Drug2Cell Score Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Integrate spatial transcriptomic data with Drug2Cell predictions to map drug sensitivity scores across glioblastoma samples. Identify tumor regions that may respond to specific drugs based on local transcription factor and pathway activity profiles. Compare drug scores across metaprograms to uncover therapeutic targets tied to distinct tumor niches or cellular states. Use the search box to enter drug names and the sample selector to explore across different tumors.")

file = open('text_files/drug2cell_names.txt', 'r')
drug_ravi = sorted(file.read().splitlines())

drug_ren = pd.read_csv('text_files/drug_list_ren.csv', header=None)[0].tolist()
drug_son = pd.read_csv('text_files/drug_list_sonpatki.csv', header=None)[0].tolist()

a, b = st.columns(2)

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)

# option = b.selectbox(
#     'drug2cell',
#     list)

df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()

samples_ren = st.session_state.get("samples_ren", [])
samples_son = st.session_state.get("samples_son", [])


# option2 = a.selectbox(
#     label='Sample',
#     options=sample_list,
#     key = persist("sample_id")
#     ) 

option = a.selectbox(
    label='Sample',
    options=sample_list,
    format_func=lambda sample: f"{sample} - validation" if sample in samples_ren + samples_son else f"{sample} - main",
    key=persist("sample_id")
)

# Choose gene list based on which dataset the sample belongs to
if option in samples_ren:
    drug_options = drug_ren
elif option in samples_son:
    drug_options = drug_son
else:
    drug_options = drug_ravi

option2 = b.selectbox(
    'Drug',
    drug_options
)


image_na = "./logo/no_available_icon.png"

if option not in samples_ren + samples_son:

  image_spatial = f"{IMG_REPO}/{option}/{option2}.png"
  if url_is_alive(image_spatial):
      a.image(image_spatial)
  else:
      a.image(image_na)

  image_spatial = f"{IMG_REPO2}/{option}/{option2}.png"
  if url_is_alive(image_spatial):
      b.image(image_spatial)
  else:
      b.image(image_na)
  # a.image(f'{IMG_REPO}/{option}/{option2}.png')
  # b.image(f'{IMG_REPO2}/{option}/{option2}.png')
  
  IMG_REPO3 = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
  st.markdown("<h3 style='text-align: center; color: black;'>Drug2Cell Scores across Metaprogram</h1>", unsafe_allow_html=True)
  st.image(f'{IMG_REPO3}/across_metaprogram_top_drugs_per_sample/{option2}.png')

else:
  if option in samples_ren:
    image_spatial = f"{IMG_REPO_ren}/{option2}/{option}.png"
  else:
    image_spatial = f"{IMG_REPO_son}/{option2}/{option}.png"
  _,c,_ = st.columns([1, 2, 1])
  if url_is_alive(image_spatial):
      c.image(image_spatial)
  else:
      c.image(image_na)
