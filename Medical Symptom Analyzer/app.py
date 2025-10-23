import streamlit as st
import google.generativeai as genai
from gemini_api_key import GEMINI_API_KEY

# Configure the page
st.set_page_config(
    page_title="Medical Symptom Analyzer",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI/UX
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .credit-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .symptom-card {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
        color: #ffffff;
        font-weight: 500;
    }
    .result-box {
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 2px solid #667eea;
    }
    .category-header {
        color: #1f77b4;
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
        font-size: 1.1rem;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Configure Gemini API
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
except Exception as e:
    st.error(f"Error configuring Gemini API: {str(e)}")
    st.stop()

def validate_symptom(symptom):
    """Validate that a symptom is not empty and has reasonable length"""
    if not symptom or not symptom.strip():
        return False
    if len(symptom.strip()) < 2:
        return False
    if len(symptom.strip()) > 100:
        return False
    return True

def predict_disease(symptom1, symptom2, symptom3):
    """Send symptoms to Gemini API and get disease prediction"""
    try:
        prompt = f"""You are a medical diagnostic assistant. Based on the following three symptoms, provide:
1. The most likely disease or medical condition
2. A brief explanation (2-3 sentences)
3. A recommendation to consult a healthcare professional

Symptoms:
- {symptom1}
- {symptom2}
- {symptom3}

Important: This is for educational purposes only. Always emphasize the importance of professional medical consultation.

Format your response as:
**Predicted Condition:** [condition name]

**Explanation:** [brief explanation]

**Recommendation:** [medical consultation advice]"""

        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        raise Exception(f"API call failed: {str(e)}")

# Sidebar - Common Symptoms Guide
with st.sidebar:
    st.markdown("<div style='text-align: center; padding: 10px;'>", unsafe_allow_html=True)
    st.markdown("### 📚 Common Symptoms Guide")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Respiratory Symptoms
    st.markdown("<div class='category-header'>🫁 Respiratory</div>", unsafe_allow_html=True)
    st.markdown("""
    - Cough (dry/wet)
    - Shortness of breath
    - Wheezing
    - Chest pain
    - Sore throat
    - Runny nose
    - Congestion
    """)
    
    # Gastrointestinal Symptoms
    st.markdown("<div class='category-header'>🍽️ Gastrointestinal</div>", unsafe_allow_html=True)
    st.markdown("""
    - Nausea
    - Vomiting
    - Diarrhea
    - Constipation
    - Abdominal pain
    - Bloating
    - Loss of appetite
    """)
    
    # Neurological Symptoms
    st.markdown("<div class='category-header'>🧠 Neurological</div>", unsafe_allow_html=True)
    st.markdown("""
    - Headache
    - Dizziness
    - Confusion
    - Memory problems
    - Numbness/tingling
    - Weakness
    - Seizures
    """)
    
    # General Symptoms
    st.markdown("<div class='category-header'>🌡️ General</div>", unsafe_allow_html=True)
    st.markdown("""
    - Fever
    - Fatigue
    - Chills
    - Night sweats
    - Weight loss/gain
    - Weakness
    - Malaise
    """)
    
    # Musculoskeletal Symptoms
    st.markdown("<div class='category-header'>💪 Musculoskeletal</div>", unsafe_allow_html=True)
    st.markdown("""
    - Joint pain
    - Muscle aches
    - Back pain
    - Stiffness
    - Swelling
    - Limited mobility
    """)
    
    # Skin Symptoms
    st.markdown("<div class='category-header'>🩹 Skin</div>", unsafe_allow_html=True)
    st.markdown("""
    - Rash
    - Itching
    - Redness
    - Swelling
    - Bruising
    - Dryness
    - Lesions
    """)
    
    # Cardiovascular Symptoms
    st.markdown("<div class='category-header'>❤️ Cardiovascular</div>", unsafe_allow_html=True)
    st.markdown("""
    - Chest pain
    - Palpitations
    - Irregular heartbeat
    - Swelling in legs
    - Fatigue
    """)
    
    st.markdown("---")
    st.info("💡 Use these as reference when entering your symptoms")

# Main content
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div style='text-align: center;'><span class='credit-badge'>👨‍💻 Made by Suman Suhan</span></div>", unsafe_allow_html=True)

st.markdown("<div class='main-header'>🏥 Medical Symptom Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>AI-Powered Disease Prediction from Your Symptoms</div>", unsafe_allow_html=True)

st.warning("⚠️ **Important Disclaimer:** This tool uses AI for educational purposes only and should NOT replace professional medical advice, diagnosis, or treatment.")

# Create two columns for better layout
col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown("### 📝 Enter Your Symptoms")
    
    with st.form("symptom_form"):
        symptom1 = st.text_input(
            "🔴 Symptom 1",
            placeholder="e.g., persistent headache",
            help="Enter your primary symptom"
        )
        
        symptom2 = st.text_input(
            "🟠 Symptom 2",
            placeholder="e.g., high fever",
            help="Enter your second symptom"
        )
        
        symptom3 = st.text_input(
            "🟡 Symptom 3",
            placeholder="e.g., nausea",
            help="Enter your third symptom"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🔍 Analyze Symptoms")

with col_right:
    st.markdown("### 💡 Tips for Best Results")
    st.markdown("""
    <div class='symptom-card'>
    <b>✓ Be Specific</b><br>
    Instead of "pain", say "sharp chest pain" or "dull headache"
    </div>
    
    <div class='symptom-card'>
    <b>✓ Include Duration</b><br>
    Mention if symptoms are "persistent", "occasional", or "sudden"
    </div>
    
    <div class='symptom-card'>
    <b>✓ Note Severity</b><br>
    Use terms like "mild", "moderate", or "severe"
    </div>
    
    <div class='symptom-card'>
    <b>✓ Check Sidebar</b><br>
    Browse common symptoms organized by body system
    </div>
    """, unsafe_allow_html=True)

# Process form submission
if submitted:
    if not all([validate_symptom(symptom1), validate_symptom(symptom2), validate_symptom(symptom3)]):
        st.error("❌ Please enter all three valid symptoms (2-100 characters each)")
    else:
        with st.spinner("🤖 Analyzing your symptoms with AI... Please wait..."):
            try:
                prediction = predict_disease(symptom1, symptom2, symptom3)
                
                st.success("✅ Analysis Complete!")
                
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.markdown("### 📊 Your AI Diagnosis Report")
                st.markdown("---")
                
                col_a, col_b = st.columns([1, 3])
                with col_a:
                    st.markdown("**Symptoms Analyzed:**")
                with col_b:
                    st.markdown(f"• {symptom1}")
                    st.markdown(f"• {symptom2}")
                    st.markdown(f"• {symptom3}")
                
                st.markdown("---")
                st.markdown(prediction)
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("---")
                
                col_info1, col_info2 = st.columns(2)
                with col_info1:
                    st.info("🏥 **Next Steps:** Schedule an appointment with your healthcare provider for proper diagnosis")
                with col_info2:
                    st.warning("⚡ **Emergency?** Call emergency services immediately if symptoms are severe")
                
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("Please check your API key and internet connection, then try again.")

# Footer section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.markdown("#### 🎯 About")
    st.markdown("AI-powered symptom checker using Google Gemini")

with footer_col2:
    st.markdown("#### ⚠️ Disclaimer")
    st.markdown("For educational purposes only. Always consult a doctor.")

with footer_col3:
    st.markdown("#### 👨‍💻 Developer")
    st.markdown("**Suman Suhan**")

st.markdown(
    "<div style='text-align: center; color: #888; padding: 20px; font-size: 0.9rem;'>"
    "© 2024 Medical Symptom Analyzer | Powered by Google Gemini AI"
    "</div>",
    unsafe_allow_html=True
)