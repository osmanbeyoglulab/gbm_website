import streamlit as st
import urllib.request
from persist import persist
from views.utils import get_sample_metaprograms


IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/metaprogram_tab/'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_tf_activity'
IMG_REPO_3 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_pw_activity'
IMG_REPO_4 = 'https://raw.githubusercontent.com/matthewlu2/gbm_small_data/main/dotplot_drug_score'

st.markdown("<h2 style='text-align: center; color: black;'>Metaprogram Maps</h1>", unsafe_allow_html=True)  
st.write("")


st.info("Visualize the spatial distribution of 14 transcriptional metaprograms within glioblastoma tissue samples. These metaprograms capture key malignant subtypes—such as mesenchymal, neural progenitor-like, and proliferative states—as well as important non-malignant populations, including immune, vascular, and glial cells. Use the interactive map to select and explore metaprograms, viewing their spatial localization alongside histology images.")
df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""

st.write(tabs_font_css, unsafe_allow_html=True)

option = st.selectbox(
    label='Sample',
    options=sample_list,
    key = persist("sample_id")
    ) 

c1,_,d1 = st.columns([ 0.47, 0.1, 0.5])


c1.markdown("<h4 style='text-align: center; color: black;'>H&E Stain</h4>", unsafe_allow_html=True)

d1.write("")
d1.markdown( f'<p style="font-family:sans-serif; color:black; font-size: 22px;  font-weight: bold">Sample {option}</p>',  unsafe_allow_html=True) 
_, c,_, d = st.columns([.007, .07, 0.04,.1])
c.image(f'{IMG_REPO}/he_stain/{option}.png')



d.write("")

sample_items = df_sample[df_sample['Sample-ID']== option].iloc[0]

for index, value in sample_items.items():
    d.markdown(f"**{index}** : {value}", True)




c2,d2 = st.columns([ 0.47, 0.6])         
c2.markdown("<h4 style='text-align: center; color: black;'>Metaprogram Proportion</h4>", unsafe_allow_html=True)
d2.markdown("<h4 style='text-align: center; color: black;'>Metaprogram</h4>", unsafe_allow_html=True)


c3, d3 = st.columns([.12, .12])
c3.image(f'{IMG_REPO}/pie_metaprogram/{option}.png')
d3.write("")
d3.write("")
d3.write("")
d3.write("")
d3.write("")
d3.image(f'{IMG_REPO}/metaprogram/{option}.png')


d_mp = get_sample_metaprograms("./data/sample_metaprograms.pkl")
l_mp = d_mp[option]

option_mp = st.selectbox(
    'Metaprogram',
    l_mp
)


b4, c4 = st.columns([0.2, 0.6])
c4.image(f'{IMG_REPO}/metaprogram_{option_mp}/{option}.png')


