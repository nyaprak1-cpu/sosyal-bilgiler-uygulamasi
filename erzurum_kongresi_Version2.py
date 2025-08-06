import streamlit as st
from PIL import Image

# Başlık
st.title("🧠 Yapay Zekâ Destekli Sosyal Bilgiler Uygulaması")
st.header("📜 Erzurum Kongresi - Atatürk Anlatıyor")

# Metin anlatımı
ataturk_text = """
Ben Mustafa Kemal. Erzurum Kongresi, 23 Temmuz 1919'da başladı.
Bu kongrede, milletin bağımsızlığını yine milletin azim ve kararı kurtaracaktır kararı alındı.
Ayrıca, manda ve himaye kesin olarak reddedildi.
Bu kararlar, Cumhuriyet'in temellerinin atıldığı yerlerdir.
"""

st.write(ataturk_text)

# Görsel gösterimi
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Erzurum_Kongresi_Delegeleri.jpg/640px-Erzurum_Kongresi_Delegeleri.jpg"

# PIL.Image.open doğrudan URL'den dosya açamaz. Bunun yerine, resmi önce indirip açmak gerekir.
import requests
from io import BytesIO

response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
st.image(image, caption='Erzurum Kongresi Delegeleri')

# Soru-Cevap bölümü
st.subheader("📝 Soru:")
soru = "Erzurum Kongresi'nde alınan hangi karar gelecekteki Türkiye Cumhuriyeti’nin temeli olarak görülmüştür?"

secenekler = [
    "Saltanatın devamı",
    "Manda ve himayenin kabulü",
    "Bağımsızlık kararı",
    "İngiltere ile ittifak"
]
cevap = st.radio(soru, secenekler)

if cevap:
    if cevap == "Bağımsızlık kararı":
        st.success("✅ Doğru cevap! Bağımsızlık kararı bu kongrede alınmıştır.")
    else:
        st.error("❌ Yanlış cevap. Doğru cevap: Bağımsızlık kararı.")