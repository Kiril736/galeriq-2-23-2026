import streamlit as st

st.title("galeriq na lubimi jivotni")

if "animals" not in st.session_state:
    st.session_state.animals = []

st.header("dobavi novo jivotno")
name = st.text_input("ime na jivotno")
description = st.text_area("opisanie")
image_url = st.text_input("URL na kartinata")

if st.button("dobavi"):
    if name and description and image_url:
        st.session_state.animals.append({
            "ime": name,
            "opisanie": description,
            "kartina": image_url
        })
        st.success(f"{name} e dobaveno!")
    else:
        st.warning("Populnete vsichki poleta")

if st.session_state.animals:
    st.header("premahni jivotno")

    names = []
    for a in st.session_state.animals:
        names.append(a["ime"])

    remove_name = st.selectbox("izberi jivotno za premahvane", names)

    if st.button("Premahvane"):
        for a in st.session_state.animals:
            if a["ime"] == remove_name:
                st.session_state.animals.remove(a)
                break
        st.success(f"{remove_name} e premahnato")

st.header("galeriq")
if st.session_state.animals:
    cols = st.columns(3)
    for idx, animal in enumerate(st.session_state.animals):
        with cols[idx % 3]:
            st.subheader(animal["ime"])
            st.image(animal["kartina"], use_column_width=True)
            st.write(animal["opisanie"])
else:
    st.info("galeriq e prazna. dobavete jivotni")
  
    
