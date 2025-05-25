import streamlit as st

st.set_page_config(
    page_title="Ciudades del Mundo",
    layout="wide"
)
st.title("Ciudades del Mundo")
st.subheader("Imagenes y descripcion")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&h=800&fit=crop", caption="París.")
    with st.expander("París"):st.write("""Capital de Francia""")

with col2:
    st.image("https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800&h=800&fit=crop", caption="Nueva York.")
    with st.expander("Nueva York"):st.write("""La ciudad de los rascacielos""")

with col3:
    st.image("https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?w=800&h=800&fit=crop", caption="Venecia.")
    with st.expander("Venecia"):st.write("""La ciudad de los canales""")