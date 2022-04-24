import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')
st.write('Dataframe')
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)


#表の縦横のサイズを指定できるのがDataframe。列を指定するときaxis0,行を指定するときaxis1
#st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)

#動的な表を作成したいときはDataframe。静的な表はtable
#st.table(df.style.highlight_max(axis=0))

if st.checkbox('start get tradeData'):#checkboxクリック時開始
    #折れ線グラフ
    st.line_chart(df)

