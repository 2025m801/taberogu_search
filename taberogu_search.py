#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[14]:


merged_df = pd.read_csv("merged.csv")


# In[15]:


st.title("レストランサーチアプリ")
price_limit = st.slider(
    "価格の上限（円）",
    min_value=999,
    max_value=5000,
    step=100,
    value=2000  
)

score_limit = st.slider(
    "人気スコアの下限",
    min_value=2.0,
    max_value=24.0,
    step=0.5,
    value=7.5  
)


# In[16]:


filtered_df = merged_df[
(merged_df['price'] <= price_limit)&
(merged_df['pop_score'] >= score_limit)
]


# In[17]:


fig = px.scatter(
filtered_df,
x='pop_score',
y='price',
hover_data=['name', '場所','star', 'review'], 
title='人気スコアと最低カット価格の散布図'
)
st.plotly_chart(fig)


# In[19]:


selected_name = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['name'].tolist())

if selected_name:
    url = filtered_df[filtered_df['name'] == selected_name]['タイトルURL'].values[0]
    st.markdown(f"[{selected_name}のページへ移動]({url})", unsafe_allow_html=True)


# In[20]:


sort_key = st.selectbox(
"ランキング基準を選んでください",
("star", "pop_score", "review", "price")
)
ascending = True if sort_key == "price" else False


# In[21]:


st.subheader(f"{sort_key} によるサロンランキング（上位10件）")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
st.dataframe(ranking_df[["name", "price", "pop_score", "star", "review", "場所"]])


# In[ ]:




