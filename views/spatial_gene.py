import streamlit as st
import urllib.request
from persist import persist
import pandas as pd


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/plot_spatial/main'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/plot_violin/main'
IMG_REPO_ren = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/ren_transcription'
IMG_REPO_son = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/sonpatki_transcription'


st.markdown("<h2 style='text-align: center; color: black;'>Gene Expression Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Explore the spatial patterns of individual gene expression within glioblastoma tissue sections. Visualize how any gene of interest is localized across the tumor microenvironment, highlighting expression in malignant cells, immune populations, or stromal regions. Use the search box to enter gene symbols and the sample selector to navigate different patient tumors.")

file = open('text_files/spatial_gene_names.txt', 'r')
gene_ravi = file.read().splitlines()

gene_ren = pd.read_csv('text_files/gene_list_ren.csv', header=None)[0].tolist()
gene_son = pd.read_csv('text_files/gene_list_sonpatki.csv', header=None)[0].tolist()

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

samples_ren = st.session_state.get("samples_ren", [])
samples_son = st.session_state.get("samples_son", [])

a, b = st.columns(2)

option = a.selectbox(
    label='Sample',
    options=sample_list,
    format_func=lambda sample: f"{sample} - validation" if sample in samples_ren + samples_son else f"{sample} - main",
    key=persist("sample_id")
)

# Choose gene list based on which dataset the sample belongs to
if option in samples_ren:
    gene_options = gene_ren
elif option in samples_son:
    gene_options = gene_son
else:
    gene_options = gene_ravi

option2 = b.selectbox(
    'Gene',
    gene_options
)

def url_is_alive(url):
    """
    Checks that a given URL is reachable.
    :param url: A URL
    :rtype: bool
    """
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request)
        return True
    except urllib.request.HTTPError:
        return False

image_na = "./logo/no_available_icon.png"

if option not in samples_ren + samples_son:
  
  # a.subheader('Spatial Plot')
  image_spatial = f"{IMG_REPO}/{option2}/{option}.png"
  # st.text(image_spatial)
  if url_is_alive(image_spatial):
      a.image(image_spatial)
  else:
      a.image(image_na)
  # b.subheader('Violin Plot')
  image_violin = f"{IMG_REPO_2}/{option2}/{option}.png"
  # st.text(image_violin)
  if url_is_alive(image_violin):
      b.image(image_violin)
  else:
      b.image(image_na)
else:
  if option in samples_ren:
    image_spatial = f"{IMG_REPO_ren}/{option2}/{option}.png"
  else:
    image_spatial = f"{IMG_REPO_son}/{option2}/{option}.png"
  if url_is_alive(image_spatial):
      st.image(image_spatial)
  else:
      st.image(image_na)
