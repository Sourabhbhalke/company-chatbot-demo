# company-chatbot-demo
text
# Company Chatbot Template

This repository contains a **Streamlit-based chatbot template** designed for companies to assist their clients in multiple languages (English and German). The chatbot provides services such as consulting, digital transformation guidance, and general company information.

## Features

- **Multilingual Support**: Supports English and German languages.
- **Dynamic Responses**: Tailored responses based on user input and selected language.
- **Session State Management**: Maintains chat history and user information during the session.
- **Company Information**: Provides details about services, values, team, clients, careers, and more.
- **Interactive Menu**: Allows users to navigate through predefined options or ask custom questions.

## How It Works

1. **Language Selection**: Users can choose between English or German at the start of the conversation.
2. **User Information Collection**:
   - Collects user's name and email address for personalized responses.
3. **Service Inquiry**:
   - Offers options to inquire about consulting services, digital services, or general questions.
4. **Dynamic Response Handling**:
   - Based on user input, the chatbot provides relevant information or redirects to specific sections of the company website.

## Installation

1. Clone this repository:
git clone https://github.com/your-repo/company-chatbot-template.git
text
2. Navigate to the project directory:
cd company-chatbot-template
text
3. Install the required dependencies:
pip install -r requirements.txt
text
4. Run the application:
streamlit run app.py
text

## File Structure

- `app.py`: Main application file containing the chatbot logic.
- `requirements.txt`: List of Python dependencies required for the project.

## Usage

1. Launch the chatbot by running the Streamlit app.
2. Interact with the chatbot by typing your messages in the input box.
3. The chatbot will guide you through language selection, collecting your details, and providing relevant company information.

## Key Functionalities

### Language-Specific URLs
The chatbot includes hyperlinks to important company resources in both English and German:
- Services
- Values
- Team
- Clients
- Careers
- Contact Us

### Predefined Responses
The chatbot provides predefined responses for common queries such as:
- About Us
- Services Offered
- Core Values
- Team Details
- Client Portfolio
- Career Opportunities

### Reset Functionality
Users can reset the conversation at any time using the "Reset Conversation" button.

## Example Interactions

### English Interaction Example:
1. Bot: *Welcome to Digital NewX! May I have your name?*
2. User: *John Doe*
3. Bot: *Thank you, John Doe. Could you please provide your email address?*
4. User: *john.doe@example.com*
5. Bot: *How can I assist you today? Choose from: a. Consulting Services b. Digital Services c. General Questions*

### German Interaction Example:
1. Bot: *Willkommen bei Digital NewX! Wie ist Ihr Name?*
2. User: *Max Mustermann*
3. Bot: *Danke, Max Mustermann. Können Sie mir bitte Ihre E-Mail-Adresse mitteilen?*
4. User: *max.mustermann@example.com*
5. Bot: *Wie kann ich Ihnen heute helfen? Wählen Sie aus: a. Beratungsdienstleistungen b. Digitale Dienstleistungen c. Allgemeine Fragen*

## Dependencies

This project requires the following Python libraries:
- `streamlit`

Install them using:
pip install streamlit
text





---
