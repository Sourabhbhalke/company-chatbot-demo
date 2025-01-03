import streamlit as st

# Initialize session state for chat history and user parameters
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_data" not in st.session_state:
    st.session_state.user_data = {"name": None, "email": None, "language": None, "business_info": None}

# URLs based on language with hyperlinks
URLS = {
    "English": {
        "services": "[Our Services](https://digitalnewx.com/#services)",
        "values": "[Our Values](https://digitalnewx.com/#values)", 
        "team": "[Our Team](https://digitalnewx.com/#team)",
        "clients": "[Our Clients](https://digitalnewx.com/#clients)",
        "careers": "[Careers](https://digitalnewx.com/career/)",
        "contact": "[Contact Us](https://digitalnewx.com/#contact)"
    },
    "German": {
        "services": "[Unsere Dienstleistungen](https://digitalnewx.com/de/#services)",
        "values": "[Unsere Werte](https://digitalnewx.com/de/#values)",
        "team": "[Unser Team](https://digitalnewx.com/de/#team)", 
        "clients": "[Unsere Kunden](https://digitalnewx.com/de/#clients)",
        "careers": "[Karriere](https://digitalnewx.com/de/career/)",
        "contact": "[Kontakt](https://digitalnewx.com/de/#contact)"
    }
}

def reset_session():
    st.session_state.messages = []
    st.session_state.user_data = {"name": None, "email": None, "language": None, "business_info": None}

def get_language_specific_response(key, language="English"):
    responses = {
        "English": {
            "welcome": "Welcome to Digital NewX! May I have your name?",
            "email_prompt": "Thank you, {}. Could you please provide your email address?",
            "help_options": "How can I assist you today? Choose from:\n\na. Consulting Services\nb. Digital Services\nc. General Questions",
            "about_us": "We guide businesses through digital transformation. Learn more on our website.",
            "services": "We offer consulting and digital services tailored to your needs.",
            "values": "Our core values include trust, innovation, and data-driven technology.",
            "team": "Our team consists of digital enthusiasts committed to creating value.",
            "clients": "We’ve completed over 25 successful projects across industries.",
            "careers": f"Join our innovative team! View opportunities at {URLS['English']['careers']}",
            "invalid_email": "Please provide a valid email address with @ and domain name.",
            "business_info_consulting": f"We accompany you in digital transformation focusing on AI & Data Strategy. Contact us at {URLS['English']['contact']}. Learn more about our consulting services [here](https://digitalnewx.com/#services).",
            "business_info_digital": f"From ideation to scaling, we offer comprehensive digital services. Learn more at {URLS['English']['services']}.",
            "thank_you": "Thank you for your information. We've sent the requested materials to {} and will contact you shortly.",
            "help_more": f"Need more information? Visit our website {URLS['English']['services']} or ask about specific services.",
            "general_menu": "Please select an option to learn more:\n\n1. About Us\n2. Services\n3. Values\n4. Team\n5. Clients\n6. Careers"
        },
        "German": {
            "welcome": "Willkommen bei Digital NewX! Wie ist Ihr Name?",
            "email_prompt": "Danke, {}. Können Sie mir bitte Ihre E-Mail-Adresse mitteilen?",
            "help_options": "Wie kann ich Ihnen heute helfen? Wählen Sie aus:\n\na. Beratungsdienstleistungen\nb. Digitale Dienstleistungen\nc. Allgemeine Fragen",
            "about_us": "Wir führen Unternehmen durch die digitale Transformation. Erfahren Sie mehr auf unserer Website.",
            "services": "Wir bieten Beratungs- und digitale Dienstleistungen nach Ihren Bedürfnissen.",
            "values": "Unsere Kernwerte sind Vertrauen, Innovation und datengetriebene Technologie.",
            "team": "Unser Team besteht aus digitalen Enthusiasten, die sich der Wertschöpfung verschrieben haben.",
            "clients": "Wir haben über 25 erfolgreiche Projekte in verschiedenen Branchen abgeschlossen.",
            "careers": f"Werden Sie Teil unseres Teams! Stellenangebote unter {URLS['German']['careers']}",
            "invalid_email": "Bitte geben Sie eine gültige E-Mail-Adresse mit @ und Domainname ein.",
            "business_info_consulting": f"Wir begleiten Sie bei der digitalen Transformation mit Fokus auf KI & Datenstrategie. Kontaktieren Sie uns unter {URLS['German']['contact']}. Erfahren Sie mehr über unsere Beratungsdienstleistungen [hier](https://digitalnewx.com/de/#services).",
            "business_info_digital": f"Von der Ideenfindung bis zur Skalierung bieten wir umfassende digitale Dienstleistungen. Mehr unter {URLS['German']['services']}.",
            "thank_you": "Vielen Dank für Ihre Informationen. Wir haben die angeforderten Unterlagen an {} gesendet und werden uns in Kürze bei Ihnen melden.",
            "help_more": f"Benötigen Sie weitere Informationen? Besuchen Sie unsere Website {URLS['German']['services']} oder fragen Sie nach spezifischen Dienstleistungen.",
            "general_menu": "Bitte wählen Sie eine Option für weitere Informationen:\n\n1. Über Uns\n2. Dienstleistungen\n3. Werte\n4. Team\n5. Kunden\n6. Karriere"
        }
    }
    return responses[language][key]

def handle_intent(user_input):
    language = st.session_state.user_data["language"]
    
    # Language selection
    if st.session_state.user_data["language"] is None:
        input_lower = user_input.lower()
        if any(word in input_lower for word in ["english", "eng", "en", "can we continue in english", "speak english"]):
            st.session_state.user_data["language"] = "English"
            return get_language_specific_response("welcome", "English")
        elif any(word in input_lower for word in ["german", "deutsch", "de", "auf deutsch", "sprich deutsch", "sprechen sie deutsch"]):
            st.session_state.user_data["language"] = "German"
            return get_language_specific_response("welcome", "German")
        else:
            return "Please select your preferred language: English or German / Bitte wählen Sie Ihre bevorzugte Sprache: Englisch oder Deutsch"

    # Name collection
    elif st.session_state.user_data["name"] is None:
        name = user_input.lower()
        name = name.replace("my name is", "").replace("i am", "").replace("i'm", "")
        name = name.replace("ich bin", "").replace("ich heiße", "").replace("mein name ist", "")
        name = name.strip()
        st.session_state.user_data["name"] = name.title()
        return get_language_specific_response("email_prompt", language).format(name.title())

    # Email collection
    elif st.session_state.user_data["email"] is None:
        if "@" in user_input and "." in user_input:
            st.session_state.user_data["email"] = user_input.strip()
            return get_language_specific_response("help_options", language)
        else:
            return get_language_specific_response("invalid_email", language)

    # Service and inquiry handling
    else:
        input_lower = user_input.lower()
        
        # Consulting services
        if any(word in input_lower for word in ["consulting", "beratung", "beratungsdienstleistungen", "strategy", "strategie", "a", "1"]):
            return get_language_specific_response("business_info_consulting", language)
        
        # Digital services
        elif any(word in input_lower for word in ["digital", "digitale dienstleistungen", "technical", "technisch", "implementation", "implementierung", "b", "2"]):
            return get_language_specific_response("business_info_digital", language)
        
        # General questions - show menu first
        elif any(word in input_lower for word in ["question", "frage", "fragen", "about", "über", "general", "allgemein", "allgemeine fragen", "c", "3"]):
            return get_language_specific_response("general_menu", language)
        
        # Handle responses to general menu options
        elif input_lower in ["1", "über uns", "about us"]:
            return get_language_specific_response("about_us", language)
        elif input_lower in ["2", "dienstleistungen", "services"]:
            return get_language_specific_response("services", language)
        elif input_lower in ["3", "werte", "values"]:
            return get_language_specific_response("values", language)
        elif input_lower in ["4", "team"]:
            return get_language_specific_response("team", language)
        elif input_lower in ["5", "kunden", "clients"]:
            return get_language_specific_response("clients", language)
        elif input_lower in ["6", "karriere", "careers"]:
            return get_language_specific_response("careers", language)
        
        # Business information collection
        elif st.session_state.user_data["business_info"] is None:
            st.session_state.user_data["business_info"] = user_input
            return get_language_specific_response("thank_you", language).format(st.session_state.user_data['email'])
        
        # Default response
        else:
            return get_language_specific_response("help_more", language)

# Streamlit app layout
st.title("Digital NewX Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here... / Geben Sie Ihre Nachricht hier ein..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = handle_intent(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Reset button
if st.button("Reset Conversation / Gespräch zurücksetzen"):
    reset_session()