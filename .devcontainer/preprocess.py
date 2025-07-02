import re, json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# 如果第一次运行，可能需要下载 NLTK 资源
nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def clean(text):
    t = re.sub(r"http\S+|@\w+|#","", text)
    t = re.sub(r"[^\w\s]", "", t)
    return [w for w in word_tokenize(t.lower()) if w not in stop_words]

if __name__ == "__main__":
    data = json.load(open("tweets.json", encoding="utf-8"))
    for item in data:
        item["tokens"] = clean(item["text"])
    with open("cleaned.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
