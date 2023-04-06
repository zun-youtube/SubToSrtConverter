import os
import sys
import pysubs2
import tkinter as tk
from tkinter import filedialog
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def convert_sub_to_srt(input_file, output_folder):
    if not input_file.endswith('.sub'):
        raise ValueError("入力ファイルは .sub 形式である必要があります")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.sub', '.srt'))

    encoding = detect_encoding(input_file)
    subs = pysubs2.load(input_file, encoding=encoding)
    subs.save(output_file, format_='srt')

def main():
    root = tk.Tk()
    root.withdraw()

    filetypes = [('SUB ファイル', '*.sub')]
    input_file = filedialog.askopenfilename(title='入力ファイルを選択', filetypes=filetypes)

    if not input_file:
        print("入力ファイルが選択されませんでした")
        sys.exit(1)

    output_folder = filedialog.askdirectory(title='出力フォルダを選択')

    if not output_folder:
        print("出力フォルダが選択されませんでした")
        sys.exit(1)

    try:
        convert_sub_to_srt(input_file, output_folder)
        print(f"変換完了: {input_file} -> {output_folder}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()