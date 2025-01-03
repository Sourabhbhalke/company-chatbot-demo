
# Company Chatbot Demo

![image](https://github.com/user-attachments/assets/60d55e37-5f9b-4303-98b2-a6469fa28458)

## Table of Contents
1. [Commits](#1-commits)
   - [Commits 28-12-2024](#11-commits-28-12-2024)
   - [Commits 23-12-2024](#12-commits-23-12-2024)
2. [Company Chatbot Template](#2-company-chatbot-template)
3. [Features](#3-features)
4. [How It Works](#4-how-it-works)
5. [Installation](#5-installation)
6. [File Structure](#6-file-structure)
7. [Usage](#7-usage)
8. [Key Functionalities](#8-key-functionalities)
   - [Language-Specific URLs](#81-language-specific-urls)
   - [Predefined Responses](#82-predefined-responses)
   - [Reset Functionality](#83-reset-functionality)
9. [Example Interactions](#9-example-interactions)
   - [English Interaction Example](#91-english-interaction-example)
   - [German Interaction Example](#92-german-interaction-example)
10. [Dependencies](#10-dependencies)

---

## 1. Commits
### 1.2 Commits 03-01-2025
- Added Updated architecture diagrams with mermaid
### 1.1 Commits 28-12-2024
- Added promotional video - YouTube link: https://youtu.be/NEB1mRpBAcM (unlisted - internal use only).  
#### 🎥 YouTube Demo  
Check out our project demo on YouTube:  
[![YouTube Video](https://img.youtube.com/vi/NEB1mRpBAcM/0.jpg)](https://www.youtube.com/watch?v=NEB1mRpBAcM)  

### 1.2 Commits 23-12-2024
- Added promotional video-related content such as SSML files and synthesized voice, in line with the business plan of promoting this as a service through social media and website.

---

## 2. Company Chatbot Template

This repository contains a **Streamlit-based chatbot template** designed for companies to assist their clients in multiple languages (English and German). The chatbot provides services such as consulting, digital transformation guidance, and general company information.

---

## 3. Features

- **Multilingual Support**: Supports English and German languages.
- **Dynamic Responses**: Tailored responses based on user input and selected language.
- **Session State Management**: Maintains chat history and user information during the session.
- **Company Information**: Provides details about services, values, team, clients, careers, and more.
- **Interactive Menu**: Allows users to navigate through predefined options or ask custom questions.

---

## 4. How It Works

1. **Language Selection**: Users can choose between English or German at the start of the conversation.
2. **User Information Collection**:
   - Collects user's name and email address for personalized responses.
3. **Service Inquiry**:
   - Offers options to inquire about consulting services, digital services, or general questions.
4. **Dynamic Response Handling**:
   - Based on user input, the chatbot provides relevant information or redirects to specific sections of the company website.

---

## 5. Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-repo/company-chatbot-template.git
   ```
2. Navigate to the project directory:
   ```
   cd company-chatbot-template
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   streamlit run app.py
   ```

---

## 6. File Structure

- `app.py`: Main application file containing the chatbot logic.
- `requirements.txt`: List of Python dependencies required for the project.

---

## 7. Usage

1. Launch the chatbot by running the Streamlit app.
2. Interact with the chatbot by typing your messages in the input box.
3. The chatbot will guide you through language selection, collecting your details, and providing relevant company information.

---

## 8. Key Functionalities

### 8.1 Language-Specific URLs
The chatbot includes hyperlinks to important company resources in both English and German:
- Services
- Values
- Team
- Clients
- Careers
- Contact Us

### 8.2 Predefined Responses
The chatbot provides predefined responses for common queries such as:
- About Us
- Services Offered
- Core Values
- Team Details
- Client Portfolio
- Career Opportunities

### 8.3 Reset Functionality
Users can reset the conversation at any time using the "Reset Conversation" button.

---

## 9. Example Interactions

### 9.1 English Interaction Example:
1. Bot: *Welcome to Digital NewX! May I have your name?*
2. User: *John Doe*
3. Bot: *Thank you, John Doe. Could you please provide your email address?*
4. User: *john.doe@example.com*
5. Bot: *How can I assist you today? Choose from: a. Consulting Services b. Digital Services c. General Questions*

### 9.2 German Interaction Example:
1. Bot: *Willkommen bei Digital NewX! Wie ist Ihr Name?*
2. User: *Max Mustermann*
3. Bot: *Danke, Max Mustermann. Können Sie mir bitte Ihre E-Mail-Adresse mitteilen?*
4. User: *max.mustermann@example.com*
5. Bot: *Wie kann ich Ihnen heute helfen? Wählen Sie aus: a. Beratungsdienstleistungen b. Digitale Dienstleistungen c. Allgemeine Fragen*

---

## 10. Dependencies

This project requires the following Python libraries:
- `streamlit`

Install them using:
```
pip install streamlit
```
```

