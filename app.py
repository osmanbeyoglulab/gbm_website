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

# max_width_str = f"max-width: {80}%;"

# st.markdown(f"""
#         <style>
#         .appview-container .main .block-container{{{max_width_str}}}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

define_layout(max_width='80%', padding_top='2rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem')

# st.markdown(f"""
#     <style>
#         .stSelectbox > label {{
#             # font-size:200%; 
#             font-size: 30px;
#             font-weight:bold; 
#             color: purple;
#         }}
#         .stMultiSelect > label {{
#             font-size:105%; 
#             font-weight:bold; 
#             color:black;
#         }}
#     </style>
#     """, unsafe_allow_html=True)

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

# home_page = st.Page(
#     page = "views/home.py",
#     title = "Home",
#     icon = "🏠",   #":material/chevron_right:"  ,
#     default= True,
# )

# datasets_page = st.Page(
#     page = "views/dataset.py",
#     title = "Dataset Explorer",
#     icon = "🗂️"  
# )

# metaprogram_page = st.Page(
#     page = "views/metaprogram.py",
#     title = "Metaprogram Maps",
#     icon = "🌀"    
# )

# metaprogram_feature_page = st.Page(
#     page = "views/metaprogram_feature.py",
#     title = "Metaprogram-Associated Features",
#     icon = "🧩"    
# )

# mp_specific_page = st.Page(
#     page = "views/metaprogram_centric.py",
#     title = "Metaprogram-Centric Comparison",  #Metaprogram
#     icon = "📊"   #🌀
# )

# drug2cell_page = st.Page(
#     page = "views/drug2cell.py",
#     title = "Drug2Cell Score Maps",
#     icon = "💊"
# )

# heatmap_gene_correlation_page = st.Page(
#     page = "views/Ligand–Receptor–TF–Pathway_Correlation.py",
#     title = "L-R-TF-Pathway-Drug Correlation Heatmap",  #Correlation heatmaps
#     icon = "🪢"
# )

# gene_page = st.Page(
#     page = "views/spatial_gene.py",
#     title = "Gene Expression Maps",
#     icon = "🧬"
# )

# s_tf_page = st.Page(
#     page = "views/spatial_tf.py",
#     title = "TF Activity Maps",
#     icon = "🎯"
# )

# s_pathway_page = st.Page(
#     page = "views/spatial_pathway.py",
#     title = "Pathway Activity Maps",
#     icon = "🔀"
# )


# contact_page = st.Page(
#     page = "views/contact.py",
#     title = "Contact us",
#     icon = "📨"
# )

# citation_page = st.Page(
#     page = "views/citation.py",
#     title = "Citation",
#     icon = "📚"
# )

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
    title = "Sample explore",
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

heatmap_gene_correlation_page = st.Page(
    page = "views/Ligand–Receptor–Pathway–TF_Correlation.py",
    title = "L-R-Pathway-TF-Drug Correlation Heatmap",  #Correlation heatmaps
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
        "Analysis of Individual Samples": [metaprogram_page, metaprogram_feature_page, gene_page, s_tf_page, s_pathway_page , drug2cell_page],
        "Comparison Across Samples": [mp_specific_page,  heatmap_gene_correlation_page], 
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


