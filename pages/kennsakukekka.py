import streamlit as st

if "サイコホラー" in st.session_state.option:
    st.header("殺戮の天使")
    st.subheader("")
if "ミステリーホラー" in st.session_state.option:
    st.header("虚白の夢")
    st.subheader("")
if "ホラーアドベンチャー" in st.session_state.option:
    st.header("徒花の館")
    st.subheader("")
if "伝奇アドベンチャー" in st.session_state.option:
    st.header("被虐のノエル")
    st.subheader("")
if "アクションファンタジー" in st.session_state.option:
    st.header("鹿の王")
    st.subheader("")
if "ハイファンタジー" in st.session_state.option:
    st.header("獣の奏者")
    st.subheader("")
if "学園ダークファンタジー" in st.session_state.option:
    st.header("七つの魔剣が支配する")
    st.subheader("")

