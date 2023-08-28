import streamlit as st
import sqlite3

# データベース接続
conn = sqlite3.connect('code_storage.db')
cursor = conn.cursor()

# テーブル作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS code_snippets (
    id INTEGER PRIMARY KEY,
    title TEXT,
    code TEXT
)
''')
conn.commit()

# コード保存アプリのStreamlitコード
def main():
    st.title("コード保存アプリ")

    # 新しいコードの保存
    st.header("新しいコードの保存")
    title = st.text_input("タイトル")
    code = st.text_area("コード")
    if st.button("保存"):
        cursor.execute("INSERT INTO code_snippets (title, code) VALUES (?, ?)", (title, code))
        conn.commit()
        st.success("コードが保存されました！")

    # 保存されたコードの表示
    st.header("保存されたコード一覧")
    saved_codes = cursor.execute("SELECT title, code FROM code_snippets").fetchall()
    for i, (title, code) in enumerate(saved_codes):
        st.write(f"## コード {i+1}: {title}")
        st.code(code)

# アプリの実行
if __name__ == '__main__':
    main()
