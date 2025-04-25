import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

def disegna_stanza(base, altezza, spessore):
    larghezza_porta = 90
    larghezza_finestra = 120
    altezza_finestra = 100
    larghezza_letto = 80
    lunghezza_letto = 200

    interno_x = [spessore, spessore + base, spessore + base, spessore, spessore]
    interno_y = [spessore, spessore, spessore + altezza, spessore + altezza, spessore]
    esterno_x = [0, base + 2*spessore, base + 2*spessore, 0, 0]
    esterno_y = [0, 0, altezza + 2*spessore, altezza + 2*spessore, 0]
    porta_x0 = spessore + base / 2 - larghezza_porta / 2
    porta_x1 = porta_x0 + larghezza_porta
    porta_y0 = 0
    porta_y1 = spessore
    finestra_x0 = spessore + base
    finestra_x1 = finestra_x0 + spessore
    finestra_y1 = spessore + altezza - 50
    finestra_y0 = finestra_y1 - altezza_finestra
    letto_x0 = spessore
    letto_x1 = letto_x0 + larghezza_letto
    letto_y1 = spessore + altezza - 30
    letto_y0 = letto_y1 - lunghezza_letto
    if letto_y0 < spessore:
        letto_y0 = spessore
        letto_y1 = spessore + lunghezza_letto

    fig, ax = plt.subplots(figsize=(8, 6))
    # Pareti esterne color pastello
    ax.fill(esterno_x, esterno_y, color='#FFDAB9', alpha=0.8)  # pesca chiaro
    # Spazio interno
    ax.fill(interno_x, interno_y, color='#FFFACD', alpha=1)    # giallo chiaro
    # Porta (azzurro vivace)
    ax.fill([porta_x0, porta_x1, porta_x1, porta_x0], [porta_y0, porta_y0, porta_y1, porta_y1], color='#40E0D0', label='🚪 Porta')
    # Finestra (blu cielo)
    ax.fill([finestra_x0, finestra_x1, finestra_x1, finestra_x0],
            [finestra_y0, finestra_y0, finestra_y1, finestra_y1], color='#87CEEB', label='🪟 Finestra')
    # Letto (verde pastello)
    ax.fill([letto_x0, letto_x1, letto_x1, letto_x0],
            [letto_y0, letto_y0, letto_y1, letto_y1], color='#90EE90', label='🛏️ Letto')
    # Contorni vivaci
    ax.plot(esterno_x, esterno_y, color='#FFA500', linewidth=4)
    ax.plot(interno_x, interno_y, color='#4682B4', linewidth=3, linestyle='--')
    # Etichette emoji
    ax.text((porta_x0 + porta_x1) / 2, (porta_y0 + porta_y1) / 2, '🚪', fontsize=28, ha='center', va='center')
    ax.text((finestra_x0 + finestra_x1) / 2, (finestra_y0 + finestra_y1) / 2, '🪟', fontsize=28, ha='center', va='center')
    ax.text((letto_x0 + letto_x1) / 2, (letto_y0 + letto_y1) / 2, '🛏️', fontsize=28, ha='center', va='center')
    ax.set_xlim(-spessore, base + 3 * spessore)
    ax.set_ylim(-spessore, altezza + 3 * spessore)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig

def fig_to_pdf(fig):
    buf = BytesIO()
    fig.savefig(buf, format="pdf", bbox_inches='tight')
    buf.seek(0)
    return buf

st.markdown(
    """
    <style>
    .main {background-color: #f5f7fa;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #b22222;'>🎨 Progetta la TUA stanza dei sogni! 🎨</h1>", unsafe_allow_html=True)
st.markdown("**Inserisci le dimensioni, scegli la fantasia, e scarica la tua creazione in PDF!**")
st.markdown("*Puoi spostare gli oggetti aggiungendo altri dettagli con la fantasia!*")

base = st.slider("Base interna stanza (cm)", 200, 800, 400, 10)
altezza = st.slider("Altezza interna stanza (cm)", 200, 600, 300, 10)
spessore = st.slider("Spessore parete (cm)", 10, 60, 30, 1)

fig = disegna_stanza(base, altezza, spessore)
st.pyplot(fig)

pdf_data = fig_to_pdf(fig)
st.download_button(
    label="✨ Scarica il PDF colorato! ✨",
    data=pdf_data,
    file_name="stanza_fantasia.pdf",
    mime="application/pdf"
)

st.info("Vuoi aggiungere altri arredi o dettagli? Scrivilo nei commenti!")
