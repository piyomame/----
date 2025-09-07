import streamlit as st

if 'option' not in st.session_state:
    st.session_state.option = ""

# 基本的なドロップダウンリスト
st.session_state.option = st.multiselect(
    "本のジャンル（複数回答可）",
    ["ミステリーホラー", "ホラーアドベンチャー", "伝奇アドベンチャー", "サイコホラー"]
)

# 選択された項目がそのままoptionに格納されるよ
if st.session_state.option:
    st.write(f"あなたが選んだ本のジャンル: {', '.join(st.session_state.option)} 📖")
else:
    st.write("ジャンルを選んでね")

