import streamlit as st
import pandas as pd
from persist import update_widget_state
# from st_aggrid import AgGrid, GridOptionsBuilder

st.markdown("<h2 style='text-align: center; color: black;'>Dataset Explorer</h1>", unsafe_allow_html=True)  
st.write("")

st.info("Explore samples by searching for specific entries. For individual samples, you will find clinical information, H&E stained images, metaprogram annotations, spatial mRNA expression, transcription factor (TF) and pathway activity visualizations as well as TF-pathway-ligand-receptor correlation heatmaps. For multiple samples, we offer comparative analysis for TF/pathway metaprogram associations and single gene expression correlations with TF and pathway activity across the samples.")

a, b = st.columns([2.3, 20])



# -- TABLE --
df_sample = st.session_state.df_sample
st.markdown("""
    <style>
        .stTable tr {
            height: 56px; # use this to adjust the height
        }
    </style>
""", unsafe_allow_html=True)

df_sample['Grade'] = df_sample['Grade'].astype('Int64')

b.table(df_sample)        


st.markdown(f"""
    <style>
        .stButton > button {{
            font-size:100%;
            font-weight:bold; 
            width: 85px;
            color:purple;
        }}
    </style>
""", unsafe_allow_html=True)


sample_list = df_sample['Sample-ID'].values.tolist()
a.text("")
a.text("")
a.text("")
a.text("")
for i in range(45):
    if a.button("Analysis", i):
        update_widget_state('sample_id', sample_list[i])
        st.switch_page("views/metaprogram.py")






# grid_builder = GridOptionsBuilder.from_dataframe(df)
# grid_options = grid_builder.build()

# grid_options['columnDefs'][0]['checkboxSelection'] = True

# AgGrid(data=df, gridOptions=grid_options, key='grid1')
