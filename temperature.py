import streamlit as st

st.title("🌡 Temperature Converter")

unit = st.radio(
    "Select the unit of temperature you want to enter:",
    ["Celsius", "Fahrenheit", "Kelvin"]
)

temp_value = st.number_input(f"Enter temperature in {unit}:", format="%.2f")

if st.button("Convert"):
    if unit == "Celsius":
        fahrenheit = (temp_value * 9/5) + 32
        kelvin = temp_value + 273.15
        st.success(f"🌡 Fahrenheit: {fahrenheit:.2f} °F")
        st.success(f"🌡 Kelvin: {kelvin:.2f} K")

    elif unit == "Fahrenheit":
        celsius = (temp_value - 32) * 5/9
        kelvin = (temp_value - 32) * 5/9 + 273.15
        st.success(f"🌡 Celsius: {celsius:.2f} °C")
        st.success(f"🌡 Kelvin: {kelvin:.2f} K")

    elif unit == "Kelvin":
        celsius = temp_value - 273.15
        fahrenheit = (temp_value - 273.15) * 9/5 + 32
        st.success(f"🌡 Celsius: {celsius:.2f} °C")
        st.success(f"🌡 Fahrenheit: {fahrenheit:.2f} °F")


