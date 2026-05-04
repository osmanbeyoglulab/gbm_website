import streamlit as st
from persist import persist
import pandas as pd
from views.utils import url_is_alive


st.markdown("<h2 style='text-align: center; color: black;'>Transcription Factor (TF) Activity Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Visualize spatially inferred transcription factor activities across glioblastoma samples using the STAN framework. Examine how TF activities distribute across the tissue architecture, overlaid on histology images. Comparative violin plots display TF activity across transcriptional metaprograms, revealing how regulation differs between malignant and non-malignant states and highlighting key regulators of specific tumor niches. Use the search box to enter TF names and the sample selector to browse different patient tumors.")

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/spatial_tf_tab/'
IMG_REPO_ren = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/ren_transcription'
IMG_REPO_son = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/sonpatki_transcription'

file = open('text_files/spatial_tf_activity_names.txt', 'r')
tf_ravi = file.read().splitlines()

tf_ren = pd.read_csv('text_files/tf_list_ren.csv', header=None)[0].tolist()
tf_son = pd.read_csv('text_files/tf_list_sonpatki.csv', header=None)[0].tolist()

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

samples_ren = st.session_state.get("samples_ren", [])
samples_son = st.session_state.get("samples_son", [])

# option = a.selectbox(
#     label='Sample',
#     options=sample_list,
#     key = persist("sample_id")
#     ) 


# option2 = b.selectbox(
#     'TF',
#     list) 

st.write(sample_list)  
option = a.selectbox(
    label='Sample',
    options=sample_list,
    format_func=lambda sample: f"{sample} - validation" if sample in samples_ren + samples_son else f"{sample} - main",
    key=persist("sample_id")
)

# Choose gene list based on which dataset the sample belongs to
if option in samples_ren:
    tf_options = tf_ren
elif option in samples_son:
    tf_options = tf_son
else:
    tf_options = tf_ravi

option2 = b.selectbox(
    'TF',
    tf_options
)
if option not in samples_ren + samples_son:    
  # a.subheader('Spatial Plot')            
  a.image(f'{IMG_REPO}/spatial_tf_activity/{option2}/{option}.png')
  # b.subheader('Violin Plot')
  b.image(f'{IMG_REPO}/violin_tf_activity/{option2}/{option}.png')
  
  
  IMG_REPO2 = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
  st.markdown("<h3 style='text-align: center; color: black;'>TF Activity across Metaprograms</h3>", unsafe_allow_html=True)
  st.image(f'{IMG_REPO2}/across_metaprogram_top_transcriptions_per_sample/{option}.png')
  
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
