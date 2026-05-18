import streamlit as st
from style import page_style, footer
import pandas as pd
from persist import load_widget_state, persist
from views.utils import get_sample_dataframe
from style import define_layout
# st.cache_data.clear()
# st.cache_resource.clear()

# --- PAGE SETUP ----

st.set_page_config(
        page_title='GBM',
        page_icon= "./logo/gbm_ribbon.png",
        initial_sidebar_state="expanded",
        # layout="wide" 
)

define_layout(max_width='80%', padding_top='2rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem')

# ---- start main ---

load_widget_state()

# df_sample = pd.read_csv('./data/dataset.csv')
# df_sample.index = df_sample.index + 1
# st.session_state['df_sample'] = df_sample
df_sample = get_sample_dataframe('./data/dataset.csv')
st.session_state['df_sample'] = df_sample
persist("sample_id")


samples_ren = ['Ren_GBM2', 'Ren_GBM3', 'Ren_GBM51']
samples_son = ['SNU16B',	 'SNU18A',	 'SNU18Afrozen',	 'SNU18B',	 'SNU21Afrozen',	 'SNU21B',	 'SNU21Dfrozen',	 'SNU24A',	 'SNU24B',	 'SNU25A',	 'SNU25B',	 'SNU27A',	 'SNU27B',	 'SNU43A',	 'SNU51A',	 'SNU51B']
if "samples_ren" not in st.session_state:
    st.session_state.samples_ren = samples_ren

if "samples_son" not in st.session_state:
    st.session_state.samples_son = samples_son
emoji = "🔹" #"🔸" #"💠" #"🔹" # # #

home_page = st.Page(
    page = "views/home.py",
    title = "Home",
    icon = emoji,   #":material/chevron_right:"  ,
    default= True,
)

datasets_page = st.Page(
    page = "views/dataset.py",
    title = "Dataset Explorer",
    icon = emoji
)

metaprogram_page = st.Page(
    page = "views/metaprogram.py",
    title = "Sample Explorer",
    icon = emoji   
)

metaprogram_feature_page = st.Page(
    page = "views/metaprogram_feature.py",
    title = "Metaprogram-Associated Features",
    icon = emoji 
)

mp_specific_page = st.Page(
    page = "views/metaprogram_centric.py",
    title = "Metaprogram-Centric Comparison",  #Metaprogram
    icon = emoji  
)

drug2cell_page = st.Page(
    page = "views/drug2cell.py",
    title = "Drug2Cell Score Maps",
    icon = emoji
)

discovery_correlation_page = st.Page(
    page = "views/correlation_discovery.py",
    title = "Regulatory Explorer — Discovery Cohort",  #Correlation heatmaps
    icon = emoji
)

validation_correlation_page = st.Page(
    page = "views/correlation_validation.py",
    title = "Regulatory Explorer — Validation Cohort",  #Correlation heatmaps
    icon = emoji
)

comb_correlation_page = st.Page(
    page = "views/correlation_comb.py",
    title = "Regulatory Explorer — Combined Cohorts",  #Correlation heatmaps
    icon = emoji
)

gene_page = st.Page(
    page = "views/spatial_gene.py",
    title = "Gene Expression Maps",
    icon = emoji
)

s_tf_page = st.Page(
    page = "views/spatial_tf.py",
    title = "TF Activity Maps",
    icon = emoji
)

s_pathway_page = st.Page(
    page = "views/spatial_pathway.py",
    title = "Pathway Activity Maps",
    icon = emoji
)


contact_page = st.Page(
    page = "views/contact.py",
    title = "Contact us",
    icon = emoji
)

citation_page = st.Page(
    page = "views/citation.py",
    title = "Citation",
    icon = emoji
)


# -- NAVIGATION --


pg = st.navigation(
    {
        "": [home_page, datasets_page],
        "Analysis of Individual Samples": [metaprogram_page, gene_page, s_tf_page, s_pathway_page , drug2cell_page, metaprogram_feature_page],
        "Comparison Across Samples": [mp_specific_page,  discovery_correlation_page,  validation_correlation_page, comb_correlation_page], 
        "Resources": [citation_page, contact_page]
    }
)

pg.run()


# -- SHARED ON ALL PAGES --
# st.sidebar.text("Made by Osmanbeyoglu Lab")

# -- RUN NAVIGATION --
# pg.run()
st.divider()
st.markdown(footer,unsafe_allow_html=True) 


