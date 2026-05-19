import streamlit as st
import streamlit.components.v1 as components

# footer="""
# <style>
  
#     .image 
#     { 
#         padding: 10px;
#         transition: transform .2s;
#     }


#     .image:hover {  
#         transform: scale(1.5);
#         transition: 0.2s;
#     }
    
#     .footer {
#         position: relative;
#         width: 100%;
#         left: 0;
#         bottom: 0;
#         background-color: white;
#         margin-top: auto;
#         color: black;
#         padding: 24px;
#         text-align: center;
#     }
# </style>

# <div class="footer">
# <p style="font-size:  13px">© 2026 Osmanbeyoglulab.com. All rights reserved.</p>
# <a href="https://hillman.upmc.com/"><img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7c7pXIkFgMPVM2csVE6MenUFLEsgF5beCeMJzogkPkXPC4xEo9OTHf6nVpqsb3PvisRk&usqp=CAU"alt="github" width="70" height=50"></a>
# <a href="https://www.pitt.edu/"><img class="image" src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/University_of_Pittsburgh_seal.svg/300px-University_of_Pittsburgh_seal.svg.png"alt="github" width="45" height="45"></a>
# <a href="https://github.com/osmanbeyoglulab"><img class="image" src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="github" width="45" height="45"></a>
# <a href="https://scholar.google.com/citations?user=YzCsmdgAAAAJ&hl=en&inst=7044483460239389945"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/512px-Google_Scholar_logo.svg.png"alt="github" width="45" height="45"></a>
# </div>

# """


# page_style = """
#     <style>
#         #MainMenu {visibility: hidden;} 
#         footer {visibility: hidden;} 
#     </style>
# """



footer = """
<style>
    .image { 
        padding: 10px;
        transition: transform .2s;
    }
    .image:hover {  
        transform: scale(1.5);
        transition: 0.2s;
    }
    .footer {
        position: relative;
        width: 100%;
        left: 0;
        bottom: 0;
        background-color: white;
        margin-top: auto;
        color: black;
        padding: 24px;
        text-align: center;
        font-family: sans-serif;
    }
</style>
<div class="footer">
    <p style="font-size: 13px">© 2026 Osmanbeyoglulab.com. All rights reserved.</p>

    <!-- UPMC: use their direct public logo -->
    <a href="https://hillman.upmc.com/">
        <img class="image" src="https://www.upmc.com/images/logos/upmc-logo.png" alt="UPMC" width="70" height="50"
             onerror="this.style.display='none'">
    </a>

    <!-- Pitt: use a CDN-hosted or public version -->
    <a href="https://www.pitt.edu/">
        <img class="image" src="https://upload.wikimedia.org/wikipedia/en/f/fb/University_of_Pittsburgh_seal.svg" alt="Pitt" width="45" height="45"
             onerror="this.style.display='none'">
    </a>

    <!-- GitHub: use GitHub's own CDN -->
    <a href="https://github.com/osmanbeyoglulab">
        <img class="image" src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="45" height="45">
    </a>

    <!-- Google Scholar: use official SVG -->
    <a href="https://scholar.google.com/citations?user=YzCsmdgAAAAJ&hl=en">
        <img class="image" src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" alt="Google Scholar" width="45" height="45"
             onerror="this.style.display='none'">
    </a>
</div>
"""

page_style = """
    <style>
        #MainMenu {visibility: hidden;} 
        footer {visibility: hidden;} 
    </style>
"""

st.markdown(page_style, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)
def define_layout(max_width='95%', padding_top='1rem', padding_right='2rem', padding_left='2rem', padding_bottom='0rem'):
   
    st.markdown(f"""
        <style>
        /* Target the main block container in wide mode */
        section.main > div {{
            max-width: {max_width};
            padding-top: {padding_top};
            padding-right: {padding_right};
            padding-left: {padding_left};
            padding-bottom: {padding_bottom};
        }}
        
        /* Alternative selector for block container */
        .block-container {{
            max-width: {max_width} !important;
            padding-top: {padding_top} !important;
            padding-right: {padding_right} !important;
            padding-left: {padding_left} !important;
            padding-bottom: {padding_bottom} !important;
        }}
        
        /* Ensure content doesn't exceed max width */
        section.main > div:has(> .block-container) {{
            max-width: {max_width};
            margin: 0 auto;
        }}
        
        /* Make all components responsive within the constrained width */
        .stAlert,
        .stDataFrame,
        .stPlotlyChart,
        div[data-testid="stAlert"],
        div[data-testid="stDataFrame"],
        div[data-testid="stPlotlyChart"] {{
            width: 100% !important;
        }}
        </style>
        """, unsafe_allow_html=True)
