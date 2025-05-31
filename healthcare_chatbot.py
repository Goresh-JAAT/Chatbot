import streamlit as st

st.set_page_config(page_title="Healthcare Chatbot", page_icon="💬")

st.title("🏥 Healthcare Chatbot")
st.markdown("Ask me any health-related question!")

def get_health_response(user_input):
    user_input = user_input.lower()

    if "fever" in user_input:
        return "It sounds like you have a fever. Rest, hydrate, and monitor your temperature. If it exceeds 102°F (39°C), consult a doctor."
    elif "headache" in user_input:
        return "Headaches can be due to many causes. Rest, hydration, or mild medication might help. If persistent, consult a doctor."
    elif "cough" in user_input:
        return "A mild cough could be a sign of a cold or allergy. Drink warm fluids and rest."
    elif "first aid" in user_input:
        return "Clean the wound with water, apply antiseptic, and bandage. For burns, use cool water."
    elif "diet" in user_input:
        return "A balanced diet includes fruits, veggies, proteins, and whole grains. Avoid processed foods."
    elif "exercise" in user_input:
        return "30 minutes of moderate exercise daily is great! Walking, yoga, or light cardio are good options."
    elif "covid" in user_input:
        return "For COVID-19 symptoms (fever, cough, loss of taste/smell), isolate and get tested."
    elif "emergency" in user_input:
        return "⚠️ Please call emergency services or go to the nearest hospital immediately."
    else:
        return "I'm not sure. Please consult a doctor for medical advice."

user_query = st.text_input("💬 Your Question", "")

if user_query:
    response = get_health_response(user_query)
    st.markdown(f"**🤖 Chatbot:** {response}")
