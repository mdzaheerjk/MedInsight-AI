# 🏥 Medical Symptom Analyzer

An AI-powered web application that predicts potential diseases based on three symptoms using Google Gemini AI.

![Made by Suman Suhan](https://img.shields.io/badge/Made%20by-Suman%20Suhan-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## ✨ Features

- 🤖 **AI-Powered Diagnosis** - Uses Google Gemini AI for intelligent disease prediction
- 📚 **Common Symptoms Guide** - Comprehensive sidebar with symptoms organized by body system
- 🎨 **Modern UI/UX** - Beautiful gradient design with responsive layout
- ✅ **Input Validation** - Ensures proper symptom format and length
- 🔒 **Secure API Management** - API key stored separately for security
- ⚠️ **Safety Disclaimers** - Clear warnings about educational use only
- 💡 **User Tips** - Helpful guidance for entering effective symptoms

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API Key
- Internet connection

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone <your-repository-url>
cd medical-symptom-analyzer
```

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in with your Google account
   - Click "Create API Key"
   - Copy the generated API key
   - Open `gemini_api_key.py` and replace `"your_api_key_here"` with your actual API key

4. **Create a `.gitignore` file:**
```bash
echo "gemini_api_key.py
__pycache__/
*.pyc
.env
*.log" > .gitignore
```

## 🎯 Usage

1. **Run the application:**
```bash
streamlit run app.py
```

2. **Open your browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

3. **Use the app:**
   - Browse common symptoms in the sidebar for reference
   - Enter three symptoms in the input fields
   - Click "Analyze Symptoms" to get AI predictions
   - Review the diagnosis report and recommendations

## 📁 Project Structure

```
medical-symptom-analyzer/
│
├── app.py                    # Main Streamlit application
├── gemini_api_key.py         # API key configuration (DO NOT COMMIT!)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore               # Git ignore file
```

## 🔐 Security Notes

- **NEVER** commit `gemini_api_key.py` to version control
- Always add it to `.gitignore`
- Keep your API key private and secure
- Regenerate your API key if accidentally exposed

## 📚 Symptom Categories

The app includes a comprehensive guide for:
- 🫁 Respiratory symptoms
- 🍽️ Gastrointestinal symptoms
- 🧠 Neurological symptoms
- 🌡️ General symptoms
- 💪 Musculoskeletal symptoms
- 🩹 Skin symptoms
- ❤️ Cardiovascular symptoms

## ⚠️ Important Disclaimers

- This application is for **educational purposes only**
- It should **NOT replace professional medical advice**
- Always consult a qualified healthcare provider for proper diagnosis
- In case of emergency, contact emergency services immediately

## 🛠️ Technologies Used

- **Streamlit** - Web framework for Python
- **Google Gemini AI** - AI model for disease prediction
- **Python 3.8+** - Programming language

## 📝 Tips for Best Results

- ✓ **Be Specific** - Instead of "pain", say "sharp chest pain"
- ✓ **Include Duration** - Mention if symptoms are "persistent" or "sudden"
- ✓ **Note Severity** - Use terms like "mild", "moderate", or "severe"
- ✓ **Check Sidebar** - Browse organized symptom categories

## 🐛 Troubleshooting

**Error: "Error configuring Gemini API"**
- Check that your API key is correctly set in `gemini_api_key.py`
- Ensure you have an active internet connection
- Verify your API key is valid at Google AI Studio

**Error: "Please enter all three valid symptoms"**
- Each symptom must be 2-100 characters long
- All three symptom fields must be filled
- Avoid special characters

**App not loading?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)
- Try clearing Streamlit cache: `streamlit cache clear`

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Developer

**Suman Suhan**

---

## 🌟 Acknowledgments

- Google Gemini AI for the powerful language model
- Streamlit for the amazing web framework
- Medical professionals for symptom classification guidance

---

<div align="center">
Made with ❤️ by Suman Suhan
</div>

---

## 📞 Support

If you encounter any issues or have questions, please open an issue in the repository.

**Remember:** This is an educational tool. Always seek professional medical advice for health concerns! 🏥