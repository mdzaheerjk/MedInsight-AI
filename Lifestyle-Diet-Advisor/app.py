import streamlit as st
import google.generativeai as genai
from gemini_api_key import GEMINI_API_KEY
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Lifestyle & Diet Advisor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for clean, simple UI
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background-color: #ffffff;
    }
    
    .main {
        background-color: #ffffff;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Simple header */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #000000 !important;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        text-align: center;
        color: #000000 !important;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Clean section headers */
    .section-header {
        font-size: 1.3rem;
        font-weight: 600;
        color: #000000 !important;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    /* Simple inputs */
    .stSelectbox label, .stMultiSelect label, .stSlider label, .stRadio label, 
    .stNumberInput label, .stTextArea label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #000000 !important;
    }
    
    /* All text elements */
    p, span, div, label, h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    /* Streamlit specific text */
    .stMarkdown, .stMarkdown p, .stMarkdown span, .stMarkdown div {
        color: #000000 !important;
    }
    
    /* Metric labels and values */
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    .stTextArea textarea,
    .stNumberInput input {
        border-radius: 8px;
        border: 1px solid #cbd5e0;
        background: white;
        color: #000000 !important;
    }
    
    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="input"] > div:hover,
    .stTextArea textarea:hover,
    .stNumberInput input:hover {
        border-color: #4299e1;
    }
    
    /* Simple button */
    .stButton>button {
        width: 100% !important;
        background-color: #48bb78 !important;
        color: white !important;
        font-weight: 700 !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        border: none !important;
        font-size: 1.1rem !important;
        margin-top: 2rem !important;
    }
    
    .stButton>button:hover {
        background-color: #38a169 !important;
    }
    
    .stButton>button:active {
        background-color: #2f855a !important;
    }
    
    /* Form submit button */
    .stFormSubmitButton>button {
        width: 100% !important;
        background-color: #48bb78 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        border: none !important;
    }
    
    .stFormSubmitButton>button:hover {
        background-color: #38a169 !important;
    }
    
    .stFormSubmitButton>button:active {
        background-color: #2f855a !important;
    }
    
    /* All button types */
    button[kind="primary"], button[kind="secondary"] {
        background-color: #48bb78 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border: none !important;
    }
    
    button[kind="primary"]:hover, button[kind="secondary"]:hover {
        background-color: #38a169 !important;
    }
    
    button[kind="primary"]:active, button[kind="secondary"]:active {
        background-color: #2f855a !important;
    }
    
    /* Score card */
    .score-card {
        padding: 2rem;
        border-radius: 12px;
        background: white;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    
    .score-card h3, .score-card h2 {
        color: #000000 !important;
    }
    
    .health-score {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    /* Metric cards */
    .metric-card {
        padding: 1.5rem;
        border-radius: 8px;
        background: white;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
    }
    
    /* Recommendation box */
    .recommendation-box {
        padding: 2rem;
        border-radius: 8px;
        background: white;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        color: #000000 !important;
        line-height: 1.8;
    }
    
    .recommendation-box * {
        color: #000000 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        background: white;
        border: 1px solid #e2e8f0;
        color: #000000 !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #f7fafc;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: #4299e1;
        color: white !important;
        border-color: #4299e1;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background-color: #4299e1;
    }
    
    /* Divider */
    .input-divider {
        height: 1px;
        background: #e2e8f0;
        margin: 1.5rem 0;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
    
    .stAlert * {
        color: #000000 !important;
    }
    
    /* Slider */
    .stSlider > div > div > div > div {
        background: #4299e1 !important;
    }
    
    /* Multiselect tags */
    .stMultiSelect [data-baseweb="tag"] {
        background-color: #4299e1;
        color: white !important;
    }
    
    /* Form container */
    [data-testid="stForm"] {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
    }
    
    /* Welcome card */
    .welcome-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border: 1px solid #e2e8f0;
        margin: 2rem 0;
    }
    
    .welcome-card * {
        color: #000000 !important;
    }
    
    /* Download button specific */
    .stDownloadButton > button {
        background-color: #48bb78 !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        padding: 0.75rem 2rem !important;
        border-radius: 8px !important;
        width: 100% !important;
        border: none !important;
    }
    
    .stDownloadButton > button:hover {
        background-color: #38a169 !important;
    }
    
    .stDownloadButton > button:active {
        background-color: #2f855a !important;
    }
    
    /* Ensure button text is always visible */
    button p, button span, button div, button * {
        color: white !important;
        font-weight: 700 !important;
        background: transparent !important;
    }
    
    /* Force all buttons to be green */
    button {
        background-color: #48bb78 !important;
        color: white !important;
    }
    
    button:hover {
        background-color: #38a169 !important;
    }
    
    button:active {
        background-color: #2f855a !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Gemini API
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
except Exception as e:
    st.error(f"⚠️ API Configuration Error: {str(e)}")

# Initialize session state
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'lifestyle_score' not in st.session_state:
    st.session_state.lifestyle_score = None
if 'show_form' not in st.session_state:
    st.session_state.show_form = True
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'score_breakdown' not in st.session_state:
    st.session_state.score_breakdown = {}

# Header
st.markdown('<h1 class="main-header">🌱 Lifestyle & Diet Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Get personalized health recommendations powered by AI</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #000000; font-size: 0.9rem; margin-top: -1rem; margin-bottom: 2rem;">Built by MD Zaheer JK</p>', unsafe_allow_html=True)

# Show form or recommendations based on state
if st.session_state.show_form:
    st.markdown("---")
    
    with st.form("lifestyle_form"):
        # Diet & Nutrition Section
        st.markdown('<div class="section-header">🍽️ Diet & Nutrition</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            diet_type = st.selectbox(
                "Primary Diet Type",
                ["Omnivore", "Vegetarian", "Vegan", "Pescatarian", "Keto", "Paleo", "Mediterranean"]
            )
        with col2:
            meals_per_day = st.slider("Meals per Day", 1, 6, 3)
        with col3:
            water_intake = st.slider("Water Intake (glasses/day)", 0, 15, 8)
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Sleep & Recovery Section
        st.markdown('<div class="section-header">💤 Sleep & Recovery</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            sleep_hours = st.slider("Average Sleep (hours/night)", 3, 12, 7)
        with col2:
            sleep_quality = st.select_slider(
                "Sleep Quality",
                options=["Very Poor", "Poor", "Fair", "Good", "Excellent"]
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Physical Activity Section
        st.markdown('<div class="section-header">🏃 Physical Activity</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            exercise_frequency = st.selectbox(
                "Exercise Frequency",
                ["Sedentary", "1-2 times/week", "3-4 times/week", "5-6 times/week", "Daily"]
            )
        with col2:
            exercise_type = st.multiselect(
                "Exercise Types",
                ["Cardio", "Strength Training", "Yoga", "Sports", "Walking", "Cycling", "Swimming"]
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Mental Health Section
        st.markdown('<div class="section-header">🧘 Mental Health & Wellness</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            stress_level = st.select_slider(
                "Stress Level",
                options=["Very Low", "Low", "Moderate", "High", "Very High"]
            )
        with col2:
            meditation = st.radio(
                "Do you meditate?", 
                ["Yes, regularly", "Sometimes", "No"]
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Lifestyle Habits Section
        st.markdown('<div class="section-header">🚭 Lifestyle Habits</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            smoking = st.radio(
                "Smoking Status", 
                ["Non-smoker", "Occasional", "Regular"]
            )
        with col2:
            alcohol = st.selectbox(
                "Alcohol Consumption",
                ["None", "Occasional (1-2/week)", "Moderate (3-5/week)", "Regular (daily)"]
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Personal Information Section
        st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=15, max_value=100, value=30)
        with col2:
            health_goals = st.text_area(
                "Health Goals (optional)",
                placeholder="e.g., Weight loss, Muscle gain, Better energy..."
            )
        
        submit_button = st.form_submit_button("✅ Get My Recommendations", use_container_width=True)

    if submit_button:
        with st.spinner("Analyzing your lifestyle..."):
            try:
                prompt = f"""
                As a professional health and lifestyle advisor, analyze the following user profile and provide comprehensive recommendations:

                User Profile:
                - Age: {age}
                - Diet Type: {diet_type}
                - Meals per Day: {meals_per_day}
                - Water Intake: {water_intake} glasses/day
                - Sleep: {sleep_hours} hours/night, Quality: {sleep_quality}
                - Exercise: {exercise_frequency}, Types: {', '.join(exercise_type) if exercise_type else 'None'}
                - Stress Level: {stress_level}
                - Meditation: {meditation}
                - Smoking: {smoking}
                - Alcohol: {alcohol}
                - Health Goals: {health_goals if health_goals else 'General wellness'}

                Please provide a comprehensive analysis with:

                1. LIFESTYLE HEALTH SCORE ANALYSIS:
                   - Provide an estimated score out of 100
                   - Break down the score by category (positive and negative aspects)
                   - Explain what impacts the score

                2. DETAILED RECOMMENDATIONS by category:
                   
                   **Diet & Nutrition:**
                   - Specific meal suggestions with timing and portions
                   - Foods to include and avoid
                   - Nutrient focus areas
                   
                   **Hydration:**
                   - Optimal water intake recommendations
                   - Best timing for hydration
                   
                   **Sleep Optimization:**
                   - Sleep hygiene tips
                   - Bedtime routine suggestions
                   - Environmental factors to improve sleep quality
                   
                   **Exercise Plan:**
                   - Specific activities suited to their lifestyle
                   - Duration and frequency recommendations
                   - Progressive plan to increase activity
                   
                   **Stress Management:**
                   - Practical stress-reduction techniques
                   - Mindfulness and relaxation practices
                   
                   **Habit Modifications:**
                   - Specific lifestyle changes needed
                   - Sustainable behavior modifications

                3. PERSONALIZED ACTION PLAN:
                   - 3-5 immediate steps to take this week
                   - Prioritized by impact and ease of implementation

                4. HEALTH RISKS & CONCERNS:
                   - Potential health risks based on current lifestyle
                   - Warning signs to watch for
                   - When to consult healthcare professionals

                Format the response with clear headings using **bold** for sections and bullet points for easy reading.
                Make it detailed, actionable, and personalized to their specific situation.
                """
                
                response = model.generate_content(prompt)
                recommendations_text = response.text
                
                # Calculate lifestyle score with detailed breakdown
                score = 0
                score_breakdown = {}
                
                # Water intake (max 40 points)
                water_score = min(water_intake * 5, 40)
                score += water_score
                score_breakdown['Water Intake'] = water_score
                
                # Sleep duration (max 35 points)
                sleep_duration_score = min(sleep_hours * 5, 35)
                score += sleep_duration_score
                score_breakdown['Sleep Duration'] = sleep_duration_score
                
                # Sleep quality (10 points)
                sleep_quality_score = 10 if sleep_quality in ["Good", "Excellent"] else 0
                score += sleep_quality_score
                score_breakdown['Sleep Quality'] = sleep_quality_score
                
                # Exercise frequency (15 points)
                exercise_score = 15 if exercise_frequency in ["3-4 times/week", "5-6 times/week", "Daily"] else 0
                score += exercise_score
                score_breakdown['Exercise'] = exercise_score
                
                # Stress management (10 points)
                stress_score = 10 if stress_level in ["Very Low", "Low"] else 0
                score += stress_score
                score_breakdown['Stress Management'] = stress_score
                
                # Smoking status (10 points)
                smoking_score = 10 if smoking == "Non-smoker" else 0
                score += smoking_score
                score_breakdown['Non-smoking'] = smoking_score
                
                # Alcohol consumption (5 points)
                alcohol_score = 5 if alcohol in ["None", "Occasional (1-2/week)"] else 0
                score += alcohol_score
                score_breakdown['Alcohol Moderation'] = alcohol_score
                
                # Meditation bonus (5 points)
                meditation_score = 5 if meditation == "Yes, regularly" else 0
                score += meditation_score
                score_breakdown['Meditation'] = meditation_score
                
                score = min(score, 100)
                
                st.session_state.recommendations = recommendations_text
                st.session_state.lifestyle_score = score
                st.session_state.score_breakdown = score_breakdown
                st.session_state.user_data = {
                    'age': age,
                    'diet_type': diet_type,
                    'meals_per_day': meals_per_day,
                    'water_intake': water_intake,
                    'sleep_hours': sleep_hours,
                    'sleep_quality': sleep_quality,
                    'exercise_frequency': exercise_frequency,
                    'exercise_type': exercise_type,
                    'stress_level': stress_level,
                    'meditation': meditation,
                    'smoking': smoking,
                    'alcohol': alcohol,
                    'health_goals': health_goals
                }
                st.session_state.show_form = False
                st.rerun()
                
            except Exception as e:
                st.error(f"⚠️ Unable to fetch recommendations. Please check your API key and try again.")
                st.error(f"Error details: {str(e)}")

else:
    # Display recommendations
    st.markdown("---")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        score = st.session_state.lifestyle_score
        
        if score >= 80:
            level = "Excellent"
            color = "#48bb78"
            emoji = "🌟"
        elif score >= 60:
            level = "Good"
            color = "#4299e1"
            emoji = "✅"
        elif score >= 40:
            level = "Fair"
            color = "#ed8936"
            emoji = "⚠️"
        else:
            level = "Needs Improvement"
            color = "#f56565"
            emoji = "🔔"
        
        st.markdown(f"""
        <div class="score-card">
            <h3 style="margin: 0; color: #000000;">Your Lifestyle Score</h3>
            <div class="health-score" style="color: {color};">{score}</div>
            <h2 style="margin: 0; color: #000000;">{emoji} {level}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(score / 100)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display recommendations in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🥗 Nutrition", "💪 Fitness", "🧠 Wellness"])
    
    with tab1:
        st.markdown('<h3 style="color: #000000;">Your Personalized Recommendations</h3>', unsafe_allow_html=True)
        st.markdown(f'<div class="recommendation-box" style="color: #000000 !important;">{st.session_state.recommendations}</div>', 
                   unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<h3 style="color: #000000;">Nutrition Guidelines</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Current Diet", st.session_state.user_data.get('diet_type', 'N/A'))
            st.metric("Meals/Day", st.session_state.user_data.get('meals_per_day', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Water Intake", f"{st.session_state.user_data.get('water_intake', 0)} glasses")
            st.metric("Recommended", "8-10 glasses")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.info("💡 Balance your meals throughout the day and stay hydrated")
    
    with tab3:
        st.markdown('<h3 style="color: #000000;">Activity Overview</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Exercise Frequency", st.session_state.user_data.get('exercise_frequency', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            exercise_types = st.session_state.user_data.get('exercise_type', [])
            st.metric("Activities", ", ".join(exercise_types) if exercise_types else "None")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("🎯 Aim for 150 minutes of moderate activity per week")
    
    with tab4:
        st.markdown('<h3 style="color: #000000;">Mental Wellness</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Sleep Duration", f"{st.session_state.user_data.get('sleep_hours', 0)} hours")
            st.metric("Sleep Quality", st.session_state.user_data.get('sleep_quality', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Stress Level", st.session_state.user_data.get('stress_level', 'N/A'))
            st.metric("Meditation", st.session_state.user_data.get('meditation', 'N/A'))
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.warning("🌙 Aim for 7-9 hours of quality sleep each night")
    
    # Download Report and New Assessment Buttons
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Create downloadable report with score breakdown
    score_breakdown = st.session_state.get('score_breakdown', {})
    breakdown_text = "\n".join([f"{category}: {score} points" for category, score in score_breakdown.items()])
    
    report_content = f"""
LIFESTYLE & DIET ADVISOR - HEALTH REPORT
{'='*50}

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

LIFESTYLE SCORE: {st.session_state.lifestyle_score}/100

SCORE BREAKDOWN:
{breakdown_text}

USER PROFILE:
{'='*50}
Age: {st.session_state.user_data.get('age', 'N/A')}
Diet Type: {st.session_state.user_data.get('diet_type', 'N/A')}
Meals per Day: {st.session_state.user_data.get('meals_per_day', 'N/A')}
Water Intake: {st.session_state.user_data.get('water_intake', 'N/A')} glasses/day
Sleep Hours: {st.session_state.user_data.get('sleep_hours', 'N/A')} hours/night
Sleep Quality: {st.session_state.user_data.get('sleep_quality', 'N/A')}
Exercise Frequency: {st.session_state.user_data.get('exercise_frequency', 'N/A')}
Exercise Types: {', '.join(st.session_state.user_data.get('exercise_type', [])) if st.session_state.user_data.get('exercise_type') else 'None'}
Stress Level: {st.session_state.user_data.get('stress_level', 'N/A')}
Meditation: {st.session_state.user_data.get('meditation', 'N/A')}
Smoking: {st.session_state.user_data.get('smoking', 'N/A')}
Alcohol: {st.session_state.user_data.get('alcohol', 'N/A')}
Health Goals: {st.session_state.user_data.get('health_goals', 'N/A')}

PERSONALIZED RECOMMENDATIONS:
{'='*50}
{st.session_state.recommendations}

{'='*50}
Disclaimer: This report provides general wellness guidance. 
Always consult healthcare professionals for medical advice.
"""
    
    # Buttons in same row
    col1, col2 = st.columns([1, 1])
    with col1:
        st.download_button(
            label="📥 Download Report",
            data=report_content,
            file_name=f"health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True,
            type="primary"
        )
    with col2:
        if st.button("🔄 New Assessment", use_container_width=True, type="primary"):
            st.session_state.show_form = True
            st.session_state.recommendations = None
            st.session_state.lifestyle_score = None
            st.session_state.user_data = {}
            st.session_state.score_breakdown = {}
            st.rerun()

# Welcome screen
if st.session_state.show_form and st.session_state.recommendations is None:
    st.markdown("---")
    st.markdown("""
    <div class="welcome-card">
        <h3 style="color: #000000;">👋 Welcome!</h3>
        <p style="color: #000000; margin: 1rem 0;">
            Fill out the form above to receive personalized health and lifestyle recommendations powered by AI.
        </p>
        <p style="color: #000000;">
            Our system analyzes your lifestyle habits and provides tailored advice for:
        </p>
        <ul style="color: #000000; text-align: left; margin: 1rem 0;">
            <li>Diet and nutrition planning</li>
            <li>Exercise recommendations</li>
            <li>Sleep optimization tips</li>
            <li>Stress management techniques</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #000000; padding: 1rem 0;'>
    <p><strong>Lifestyle & Diet Advisor</strong> | Powered by Google Gemini AI</p>
    <p style='font-size: 0.9rem;'>⚠️ This tool provides general wellness guidance. Consult healthcare professionals for medical advice.</p>
</div>
""", unsafe_allow_html=True)
