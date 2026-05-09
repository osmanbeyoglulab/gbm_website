import streamlit as st
import pandas as pd
# from streamlit_option_menu import option_menu
# from streamlit_pdf_viewer import pdf_viewer

# IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data/main'
IMG_REPO = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/correlation_ren'

st.markdown("<h2 style='text-align: center; color: black;'>L-R-Pathway-TF-Drug Correlation Heatmap for validation dataset</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Explore spatial correlations between ligand expression, receptor expression, transcription factor activities, and pathway activities across validation glioblastoma samples. This helps reveal intercellular signaling and regulatory interactions shaping the tumor microenvironment. Interactive clustered heatmaps display Pearson correlation coefficients, allowing you to identify ligand–receptor–TF–pathway relationships that are conserved or variable across tumors. Use the search and filter options to select genes, TFs, pathways, or drugs, and explore their spatial correlations across different patients.")

tabs_font_css = """
<style>
div[class*="stSelectbox"] label {
  color: purple;
}
</style>
"""
st.write(tabs_font_css, unsafe_allow_html=True)


option = "tf"
df = pd.read_csv("text_files/correlation_per_tf_names_ren.csv", header=None)
tf_list = df[0].tolist()
option_tf = st.selectbox(
    'TF',
    tf_list) 
st.image(f'{IMG_REPO}/corr_with_{option}/{option_tf}.png')

st.write("")
option = "pathway"
file = open('text_files/correlation_per_pathway_names.txt', 'r')
list = file.read().splitlines()
option_pw = st.selectbox(
    'Pathway',
    list) 
st.image(f'{IMG_REPO}/corr_with_{option}/{option_pw}.png')

st.write("")
option = "drug"
df = pd.read_csv("text_files/correlation_per_drug_names_ren.csv", header=None)
drug_list = df[0].tolist()
option_drug = st.selectbox(
    'Drug',
    drug_list,
    format_func=lambda x: x.replace("_", "|")) 
st.image(f'{IMG_REPO}/corr_with_{option}/{option_drug}.png')

st.write("")
option = "gene"
df = pd.read_csv("text_files/correlation_per_gene_names_ren.csv", header=None)
gene_list = df[0].tolist()

option_gene = st.selectbox(
    'Gene',
    list) 
st.image(f'{IMG_REPO}/corr_with_{option}/{option_gene}.png')
# pdf_viewer(input = f'data/correlation_per_gene/{option}.pdf')



