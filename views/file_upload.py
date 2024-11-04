import streamlit as st
import time

if "ans_sheet" not in st.session_state:
    st.session_state['ans_sheet'] = 'not done'

col1,col2 = st.columns(2)

def change_ans_sheet_state():
    st.session_state['ans_sheet'] = 'done'

col1.markdown(' ## Upload Answer Sheet')
uploaded_file = col1.file_uploader('UPLOAD PDF', type="pdf", on_change = change_ans_sheet_state)
if st.session_state['ans_sheet'] == 'done':
    progress_bar = col1.progress(0)

    for perc_comp in range(100):
        time.sleep(0.005)
        progress_bar.progress(perc_comp+1)
    col1.write("--")
    col1.success('Answer sheet uploaded successfully')
#if uploaded_file is not None:
#   df = extract_data(uploaded_file)

