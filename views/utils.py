import pandas as pd
import streamlit as st
import pickle


@st.cache_data
def get_sample_dataframe(filepath):
    df_sample = pd.read_csv(filepath)
    df_sample.index = df_sample.index + 1
    return(df_sample)

@st.cache_data
def get_sample_metaprograms(filepath):
    with open(filepath, 'rb') as f:
        d = pickle.load(f)
    return(d)

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
