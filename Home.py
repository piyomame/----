import streamlit as st
import base64

# 画像ファイルを読み込む
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 画像ファイルのパスを指定
image_file_path = r"C:\Users\Owner\Pictures\Screenshots\スクリーンショット 2025-06-15 175105.png"  # ここに画像ファイルのパスを入れてね

# 画像をbase64にエンコード
base64_image = get_base64_of_bin_file(image_file_path)

# CSSを使って背景画像とテキストのスタイルを設定
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: top;
        background-attachment: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }}
    .title {{
        color: #006400;  /* 濃い緑色 */
        font-size: 3em;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# タイトルを中央に配置
st.markdown('<div class="title">背景画像付きアプリ</div>', unsafe_allow_html=True)