import streamlit as st
import urllib.request
from persist import persist


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/plot_spatial/main'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/plot_violin/main'


st.markdown("<h2 style='text-align: center; color: black;'>Gene Expression Maps</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Explore the spatial patterns of individual gene expression within glioblastoma tissue sections. Visualize how any gene of interest is localized across the tumor microenvironment, highlighting expression in malignant cells, immune populations, or stromal regions. Use the search box to enter gene symbols and the sample selector to navigate different patient tumors.")

file = open('text_files/spatial_gene_names.txt', 'r')
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
    'Gene',
    list)

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
