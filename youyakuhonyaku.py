import tkinter as tk
from tkinter import messagebox
import deepl
import spacy

translator = deepl.Translator('a8544d4c-ee06-41b8-9076-40396f80ea2e:fx')

nlp = spacy.load("ja_core_news_sm")


def translate(text):#日本語に翻訳
    try:
        
        result = translator.translate_text(text, target_lang="JA")
        return result.text
    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました。: {e}")
        return None

def summarize(text):#翻訳された文章を要約
    try:
        # spaCyで要約
        doc = nlp(text)
        sentences = list(doc.sents)
        summary = " ".join([str(sent) for sent in sentences[:2]]) 
        return summary
    except Exception as e:
        messagebox.showerror("エラー", f"エラーが発生しました: {e}")
        return None

def translatebutton():#ボタンを押したとき
    english_text = entry.get()
    if not english_text:
        messagebox.showwarning("警告", "翻訳したい文章を入力してください。")
        return
    
    translated_text = translate(english_text)#DeepLで英語から日本語に翻訳
    
    if translated_text:
    
        summary = summarize(translated_text)#spacyで翻訳文を要約
        
        output_text.delete(1.0, tk.END)  
        output_text.insert(tk.END, summary)  


root = tk.Tk()
root.title("翻訳と要約")

entry_label = tk.Label(root, text="英語の文章を入力してください")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

translate_button = tk.Button(root, text="翻訳と要約", command=translatebutton)
translate_button.pack(pady=10)

output_label = tk.Label(root, text="要約された日本語の文章")
output_label.pack(pady=5)

output_text = tk.Text(root, width=50, height=10)
output_text.pack(pady=5)

root.mainloop()
