# import pandas as pd
# import streamlit as st
# import pickle
# import urllib.request

# @st.cache_data
# def get_sample_dataframe(filepath):
#     df_sample = pd.read_csv(filepath)
#     df_sample.index = df_sample.index + 1
#     return(df_sample)

# @st.cache_data
# def get_sample_metaprograms(filepath):
#     with open(filepath, 'rb') as f:
#         d = pickle.load(f)
#     return(d)

# def url_is_alive(url):
#     """
#     Checks that a given URL is reachable.
#     :param url: A URL
#     :rtype: bool
#     """
#     request = urllib.request.Request(url)
#     request.get_method = lambda: 'HEAD'
#     try:
#         urllib.request.urlopen(request)
#         return True
#     except urllib.request.HTTPError:
#         return False
import pandas as pd
import streamlit as st
import pickle
import ssl
import urllib.request
import urllib.error

# Shared fallback image shown when a remote figure is missing.
NA_IMAGE = "./logo/no_available_icon.png"

# Lenient SSL context: this is only a HEAD existence-check against a public
# CDN (raw.githubusercontent.com). Some Python installs (notably macOS) lack a
# usable CA bundle, which would otherwise make every check fail.
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE


# ----------------------------------------------------------------------------
# Data loading (cached)
# ----------------------------------------------------------------------------
@st.cache_data
def get_sample_dataframe(filepath):
    df_sample = pd.read_csv(filepath)
    df_sample.index = df_sample.index + 1
    return df_sample


@st.cache_data
def get_sample_metaprograms(filepath):
    with open(filepath, 'rb') as f:
        d = pickle.load(f)
    return d


@st.cache_data
def load_pickle(filepath):
    """Load any pickle file (cached)."""
    with open(filepath, 'rb') as f:
        return pickle.load(f)


@st.cache_data
def read_lines(filepath):
    """Read a text file into a list of stripped lines (cached)."""
    with open(filepath, 'r') as f:
        return f.read().splitlines()


@st.cache_data
def read_csv_column(filepath, column=0, header=None):
    """Read a single column of a CSV into a list (cached)."""
    return pd.read_csv(filepath, header=header)[column].tolist()


# ----------------------------------------------------------------------------
# Network helpers (cached)
# ----------------------------------------------------------------------------
@st.cache_data(ttl=3600, show_spinner=False)
def url_is_alive(url):
    """
    Check that a remote figure exists, via a HEAD request (cached for 1h).

    Fail-open: only a definitive "missing" response from the server (HTTP
    404/410) is treated as not-alive. Any other problem — SSL, timeout, DNS,
    transient network error — returns True so we never hide a valid image that
    the browser could otherwise load directly. The page never crashes either.
    """
    request = urllib.request.Request(url)
    request.get_method = lambda: 'HEAD'
    try:
        urllib.request.urlopen(request, timeout=10, context=_SSL_CTX)
        return True
    except urllib.error.HTTPError as e:
        return e.code not in (404, 410)
    except Exception:
        return True


# ----------------------------------------------------------------------------
# UI helpers
# ----------------------------------------------------------------------------
def page_header(title, info=None):
    """Render a consistent centered page title and optional info banner."""
    st.markdown(
        f"<h2 style='text-align:center; color:#2e4a72;'>{title}</h2>",
        unsafe_allow_html=True,
    )
    st.write("")
    if info:
        st.info(info)


def section_title(title, container=None):
    """Render a consistent centered section sub-heading."""
    target = container if container is not None else st
    target.markdown(
        f"<h3 style='text-align:center; color:#2e4a72;'>{title}</h3>",
        unsafe_allow_html=True,
    )


def show_image(target, url, caption=None, check=False, fallback=NA_IMAGE,
               spinner="Loading figure…"):
    """
    Display an image with a loading spinner and graceful fallback.

    - ``target``  : a Streamlit container (e.g. a column) or ``st``.
    - ``check``   : if True, verify a remote URL exists before loading and show
                    the fallback image (with a caption) when it is missing.
    """
    target = target if target is not None else st
    is_remote = isinstance(url, str) and url.startswith("http")
    with st.spinner(spinner):
        if check and is_remote and not url_is_alive(url):
            target.image(fallback, caption="Figure not available for this selection")
            return
        target.image(url, caption=caption)


def sample_label(samples_ren, samples_son):
    """Return a format_func that tags samples as discovery/validation."""
    validation = set(samples_ren) | set(samples_son)
    return lambda sample: (
        f"{sample} — validation" if sample in validation else f"{sample} — discovery"
    )
