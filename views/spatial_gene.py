import streamlit as st
from persist import persist
from views.utils import read_lines, read_csv_column, page_header, show_image, sample_label

IMG_REPO = 'https://raw.githubusercontent.com/matthewlu2/plot_spatial/main'
IMG_REPO_2 = 'https://raw.githubusercontent.com/matthewlu2/plot_violin/main'
IMG_REPO_ren = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/ren_mrna'
IMG_REPO_son = 'https://raw.githubusercontent.com/osmanbeyoglulab/gbm_data_v2/main/sonpatki_mrna'

page_header(
    "Gene Expression Maps",
    "Explore the spatial patterns of individual gene expression within glioblastoma tissue sections. "
    "Visualize how any gene of interest is localized across the tumor microenvironment, highlighting "
    "expression in malignant cells, immune populations, or stromal regions. Use the search box to enter "
    "gene symbols and the sample selector to navigate different patient tumors.",
)

gene_ravi = read_lines('text_files/spatial_gene_names.txt')
gene_ren = read_csv_column('text_files/gene_list_ren.csv')
gene_son = read_csv_column('text_files/gene_list_sonpatki.csv')

df_sample = st.session_state.df_sample
sample_list = df_sample['Sample-ID'].values.tolist()

samples_ren = st.session_state.get("samples_ren", [])
samples_son = st.session_state.get("samples_son", [])

a, b = st.columns(2)

option = a.selectbox(
    label='Sample',
    options=sample_list,
    format_func=sample_label(samples_ren, samples_son),
    key=persist("sample_id"),
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
    gene_options,
    key=f"gene_{option}",
)

if option not in samples_ren + samples_son:
    show_image(a, f"{IMG_REPO}/{option2}/{option}.png", caption="Spatial expression", check=True)
    show_image(b, f"{IMG_REPO_2}/{option2}/{option}.png", caption="Expression by metaprogram", check=True)
else:
    repo = IMG_REPO_ren if option in samples_ren else IMG_REPO_son
    _, c, _ = st.columns([1, 2, 1])
    show_image(c, f"{repo}/{option2}/{option}.png", check=True)
