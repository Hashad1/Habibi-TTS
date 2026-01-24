dialect_id_map = {
    "MSA (Modern Standard Arabic)": "①",
    "SAU (Najdi, Hijazi, Gulf, etc.)": "②",
    "UAE (Emirati)": "③",
    "ALG (Algerian & Algerian Saharan)": "④",
    "IRQ (Mesopotamian & North Mesopotamian)": "⑤",
    "EGY (Egyptian, Saidi, etc.)": "⑥",
    "MAR (Moroccan or Darija)": "⑦",
    "OMN (Omani, Dhofari, etc.)": "⑧",
    "TUN (Tunisian)": "⑨",
    "LEV (Levantine)": "⑩",
    "SDN (Sudanese)": "⑪",
    "LBY (Libyan)": "⑫",
    "UNK (Unknown)": "⓪",
}  # use by infer_gradio (w/ full name) and infer_cli (w/ first three letter)


def text_list_formatter(text_list, dialect_id=None):
    final_text_list = []

    for text in text_list:
        if dialect_id is not None:
            text = f"{dialect_id}〈{text}〉"
        final_text_list.append(text)

    return final_text_list
