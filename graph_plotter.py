import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import io

st.header('Graph the plots!')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    data.dropna()
    st.header('Graph the plots!')
    unique_labels = [fire for fire in data.fireFlag.unique()]
    cols = [col for col in data.columns]

    fires = st.selectbox(
        'Select the fire you want to analyse', unique_labels)

    plot_items = st.multiselect('Select the items you want to plot ', cols)

    if st.button('Submit'):

        m = data[data['fireFlag'] == fires].first_valid_index()
        n = data[data['fireFlag'] == fires].last_valid_index()
        graph_data = data.iloc[m:n,:]

        ax = data.plot(kind='line',
                       x='datetime',
                       y=plot_items,
                       figsize=(20, 10),
                       xlim=(m - 10000, n + 10000),
                       title=fires)
        ax.axvline(x=m, color='green', linestyle='--')
        ax.axvline(x=n, color='red', linestyle='--')

        # convert plot to image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # display image
        from PIL import Image
        img = Image.open(buf)
        st.image(img, caption='Line plot with vertical lines', use_column_width=True)





