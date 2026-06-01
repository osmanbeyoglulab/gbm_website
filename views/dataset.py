import streamlit as st
import pandas as pd
from persist import update_widget_state

st.markdown("<h2 style='text-align: center; color: black;'>Dataset Explorer</h2>", unsafe_allow_html=True)
st.write("")

st.info("Explore samples by searching for specific entries. For individual samples, you will find clinical information, H&E stained images, metaprogram annotations, spatial mRNA expression, transcription factor (TF) and pathway activity visualizations as well as TF-pathway-ligand-receptor correlation heatmaps. For multiple samples, we offer comparative analysis for TF/pathway metaprogram associations and single gene expression correlations with TF and pathway activity across the samples.")

# -- SESSION STATE --
df_sample = st.session_state.df_sample.copy()
df_sample['Grade'] = df_sample['Grade'].astype('Int64')
for col in df_sample.columns:
    if df_sample[col].dtype != 'Int64':
        df_sample[col] = df_sample[col].fillna("")

sample_list = df_sample['Sample-ID'].values.tolist()
col_names = df_sample.columns.tolist()

def format_val(val):
    try:
        if pd.isna(val):
            return ""
    except (TypeError, ValueError):
        pass
    if str(val) in ("", "<NA>"):
        return ""
    return str(val)

# -- HANDLE NAVIGATION --
if "clicked_row" in st.session_state and st.session_state.clicked_row is not None:
    idx = st.session_state.clicked_row
    st.session_state.clicked_row = None
    update_widget_state('sample_id', sample_list[idx])
    st.switch_page("views/metaprogram.py")

ROW_HEIGHT = 48  # px

# ---------- CSS ----------
st.markdown(f"""
    <style>
        /* ========== OUTER TABLE ========== */
        .st-key-table_outer {{
            border: 1px solid #d0d0d0;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 8px;
        }}

        /* ========== NUCLEAR GAP REMOVAL ==========
           Every single div inside the table that is NOT a row or cell
           must have zero spacing. This includes all Streamlit wrappers:
           stVerticalBlockBorderWrapper, stVerticalBlock, stElementContainer,
           and any anonymous wrapper divs. */
        .st-key-table_outer div:not([data-testid="stHorizontalBlock"]):not([data-testid="stColumn"]) {{
            gap: 0 !important;
            row-gap: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            border: none !important;
            min-height: 0 !important;
        }}

        /* ========== ROWS ========== */
        .st-key-table_outer [data-testid="stHorizontalBlock"] {{
            border-bottom: 1px solid #d0d0d0 !important;
            margin: 0 !important;
            padding: 0 !important;
            gap: 0 !important;
            align-items: stretch !important;
            height: {ROW_HEIGHT}px;
            min-height: {ROW_HEIGHT}px;
            max-height: {ROW_HEIGHT}px;
        }}

        /* ========== CELLS ========== */
        .st-key-table_outer [data-testid="stColumn"] {{
            border-right: 1px solid #d0d0d0 !important;
            padding: 0 12px !important;
            margin: 0 !important;
            display: flex !important;
            align-items: center !important;
            height: {ROW_HEIGHT}px !important;
            min-height: {ROW_HEIGHT}px !important;
            max-height: {ROW_HEIGHT}px !important;
            overflow: hidden !important;
        }}
        .st-key-table_outer [data-testid="stColumn"]:last-child {{
            border-right: none !important;
        }}
        /* inner wrappers inside each cell need flex centering */
        .st-key-table_outer [data-testid="stColumn"] > div {{
            width: 100%;
            display: flex !important;
            align-items: center !important;
            height: 100% !important;
        }}

        /* ========== TEXT ========== */
        .st-key-table_outer p {{
            margin: 0 !important;
            padding: 0 !important;
            font-size: 14px;
            line-height: {ROW_HEIGHT}px;
        }}

        /* ========== HEADER ========== */
        .st-key-table_header [data-testid="stHorizontalBlock"] {{
            background-color: #f0f0f0 !important;
        }}
        .st-key-table_header p {{
            font-weight: 600 !important;
        }}

        /* ========== ZEBRA STRIPING ==========
           Target the main vertical block's direct children.
           Child 1 = header wrapper, children 2+ = data rows.
           Shade every other data row using multiple selector depths
           to handle varying Streamlit DOM nesting. */
        .st-key-table_outer > div [data-testid="stVerticalBlock"] > div:nth-child(2n+1):not(:first-child) [data-testid="stHorizontalBlock"] {{
            background-color: #f5f5f7 !important;
        }}

        /* ========== BUTTON ========== */
        .st-key-table_outer .stButton {{
            width: 100%;
            height: 100%;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }}
        .st-key-table_outer .stButton > button {{
            font-size: 13px !important;
            font-weight: bold !important;
            color: purple !important;
            background-color: transparent !important;
            border: 1.5px solid #d0a0d0 !important;
            border-radius: 6px !important;
            min-width: 110px !important;
            height: 34px !important;
            padding: 0 14px !important;
            margin: 0 !important;
            white-space: nowrap !important;
            overflow: visible !important;
        }}
        .st-key-table_outer .stButton > button p,
        .st-key-table_outer .stButton > button span,
        .st-key-table_outer .stButton > button div {{
            white-space: nowrap !important;
            overflow: visible !important;
            line-height: normal !important;
        }}
        .st-key-table_outer .stButton > button:hover {{
            background-color: #f5eef8 !important;
        }}
    </style>
""", unsafe_allow_html=True)

# ---------- TABLE ----------
# Button column is wider (4) than data columns (3)
ratios = [4] + [3] * len(col_names)

with st.container(key="table_outer"):

    # Header row
    with st.container(key="table_header"):
        header_cols = st.columns(ratios)
        header_cols[0].markdown("&nbsp;")
        for j, col in enumerate(col_names):
            header_cols[j + 1].markdown(f"**{col}**")

    # Data rows
    for i, row in df_sample.iterrows():
        cols = st.columns(ratios)
        if cols[0].button("Analysis", key=f"btn_{i}"):
            st.session_state.clicked_row = i
            st.rerun()
        for j, val in enumerate(row):
            cols[j + 1].markdown(format_val(val))
