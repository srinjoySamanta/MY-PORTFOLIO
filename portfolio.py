import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

# --- 1. SETUP & CONFIGURATION ---
st.set_page_config(
    page_title="Srinjoy Samanta",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CUSTOM CSS (The "Lovable" Look) ---
st.markdown("""
    <style>
    /* HIDE STREAMLIT DEFAULT UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* GLOBAL STYLES */
    .stApp {
        background-color: #09090b; /* Deep Dark Background */
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* TYPOGRAPHY */
    h1 {
        font-size: 60px !important;
        font-weight: 800;
        letter-spacing: -2px;
        margin-bottom: 10px;
    }
    h2 {
        font-size: 35px !important;
        font-weight: 700;
        margin-top: 50px;
        margin-bottom: 30px;
        border-left: 4px solid #8b5cf6;
        padding-left: 15px;
    }
    h3 {
        font-size: 22px !important;
        font-weight: 600;
    }
    p {
        font-size: 18px;
        color: #a1a1aa; /* Muted text */
        line-height: 1.6;
    }
    
    /* GRADIENT TEXT */
    .gradient-text {
        background: linear-gradient(to right, #8b5cf6, #d946ef, #f43f5e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* GLASSMORPHISM CARDS */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .glass-card:hover {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(139, 92, 246, 0.5);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px -10px rgba(139, 92, 246, 0.3);
    }
    
    /* BADGES */
    .badge {
        display: inline-block;
        padding: 5px 12px;
        background: rgba(139, 92, 246, 0.15);
        color: #c4b5fd;
        border-radius: 9999px;
        font-size: 14px;
        font-weight: 500;
        margin-right: 8px;
        margin-bottom: 8px;
        border: 1px solid rgba(139, 92, 246, 0.3);
    }
    
    /* BUTTONS */
    .custom-button {
        display: inline-block;
        background: white;
        color: black;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        margin-right: 15px;
        transition: 0.3s;
    }
    .custom-button:hover {
        background: #e4e4e7;
    }
    .outline-button {
        display: inline-block;
        background: transparent;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        text-decoration: none;
        border: 1px solid rgba(255,255,255,0.2);
        transition: 0.3s;
    }
    .outline-button:hover {
        background: rgba(255,255,255,0.1);
        border-color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HERO SECTION ---
col1, col2, col3 = st.columns([1, 8, 1])

with col2:
    st.markdown('<div style="margin-top: 60px;"></div>', unsafe_allow_html=True)
    
    hero_img, hero_text = st.columns([1, 3]) 
    
    with hero_img:
        try:
            # Make sure profile.jpg is in the same folder
            st.image("profile.jpg", caption="", width=200) 
        except:
            st.warning("⚠️ Image not found. Add 'profile.jpg' to this folder.")
            
    with hero_text:
        st.markdown('<span class="badge">Available for Work</span>', unsafe_allow_html=True)
        st.markdown('<h1>Hi, I\'m <span class="gradient-text">Srinjoy Samanta</span></h1>', unsafe_allow_html=True)
        st.markdown("""
        <p style="font-size: 20px;">
        A <b>Computer Science Engineer</b> (B.Tech 4th Year) passionate about <b>AI, Cloud, and Software Engineering</b>. 
        Currently building cool projects and completed internship at <b>IBM SkillBuild</b> via (edunet foundation).
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="margin-top: 20px;">
            <a href="mailto:srinjoysamanta73@gmail.com" class="custom-button">Get in Touch</a>
            <a href="https://github.com" class="outline-button">View GitHub</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div style="margin-top: 80px;"></div>', unsafe_allow_html=True)

# --- 4. TECH STACK ---
with col2:
    st.markdown("<h2>Tech Stack</h2>", unsafe_allow_html=True)
    skills = ["Python", "Java", "C++", "Streamlit", "IBM Cloud", "Artificial Intelligence", "UML Design", "Compiler Design", "Video Editing"]
    skill_html = ""
    for s in skills:
        skill_html += f'<span class="badge">{s}</span>'
    st.markdown(f'<div>{skill_html}</div>', unsafe_allow_html=True)

# --- 5. PROJECTS SECTION ---
with col2:
    st.markdown("<h2>Featured Projects</h2>", unsafe_allow_html=True)
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🍃 Leaf Disease Detection</h3>
            <p>An AI-powered system to detect diseases in plants using image processing. Built during my December 2025 project cycle.</p>
            <div style="margin-top: 15px;">
                <span class="badge">Python</span>
                <span class="badge">AI/ML</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with p_col2:
        st.markdown("""
        <div class="glass-card">
            <h3>🎁 Dynamic Wish Generator</h3>
            <p>A web app that creates personalized, animated greeting cards (like the one for Jayanti & Twisha) with a single link.</p>
            <div style="margin-top: 15px;">
                <span class="badge">Streamlit</span>
                <span class="badge">Automation</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    p_col3, p_col4 = st.columns(2)
    with p_col3:
        st.markdown("""
        <div class="glass-card">
            <h3>🎨 Retro Image Gen</h3>
            <p>Exploring 90s Bollywood aesthetics using generative AI tools. Focusing on image editing and style transfer.</p>
            <div style="margin-top: 15px;">
                <span class="badge">GenAI</span>
                <span class="badge">Design</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with p_col4:
        st.markdown("""
        <div class="glass-card">
            <h3>📋 IBM SkillBuild Internship</h3>
            <p>Currently working on AI and Cloud technologies. Learning practical industrial management and deployment.</p>
            <div style="margin-top: 15px;">
                <span class="badge">Cloud</span>
                <span class="badge">IBM</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- 6. ABOUT SECTION ---
with col2:
    st.markdown("<h2>About Me</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <p>
        I am a 4thyear B.Tech student based in <b>Kharagpur</b>. My journey started with a curiosity for how software is built, leading me to learn <b>Java and Python</b>.
        </p>
        <p>
        I enjoy solving problems, whether it's creating a complex <b>Data Flow Diagram (DFD)</b> for a college assignment or editing creative videos with CapCut.
        I am always looking for new challenges, like my recent preparation for the Woodrock Group interview.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- 7. CONTACT & EMAIL SECTION ---
st.markdown("---")
st.markdown('<div style="margin-top: 50px;"></div>', unsafe_allow_html=True)

contact_col1, contact_col2 = st.columns([1, 1])

# Left Column: Info
with contact_col1:
    st.markdown("<h2>Get in Touch</h2>", unsafe_allow_html=True)
    st.markdown("""
    <p>I'm always excited to work on new projects and collaborate with amazing people. 
    Whether you have a project in mind or just want to chat about web development, feel free to reach out!</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .contact-card {
        background-color: #18181b; 
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        border: 1px solid #27272a;
        display: flex;
        align-items: center;
    }
    .icon-box {
        width: 50px;
        height: 50px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin-right: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-card">
        <div class="icon-box" style="background-color: rgba(239, 68, 68, 0.2); color: #ef4444;">📧</div>
        <div>
            <div style="font-weight: bold; color: white;">Email</div>
            <div style="color: #a1a1aa;">srinjoysamanta73@gmail.com</div>
        </div>
    </div>
    <div class="contact-card">
        <div class="icon-box" style="background-color: rgba(34, 197, 94, 0.2); color: #22c55e;">📞</div>
        <div>
            <div style="font-weight: bold; color: white;">Phone</div>
            <div style="color: #a1a1aa;">+91 7586948359</div>
        </div>
    </div>
    <div class="contact-card">
        <div class="icon-box" style="background-color: rgba(59, 130, 246, 0.2); color: #3b82f6;">📍</div>
        <div>
            <div style="font-weight: bold; color: white;">Location</div>
            <div style="color: #a1a1aa;">Kaushallya, Kharagpur, Paschim Medinipur</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Right Column: The Form (SMTP Method)
with contact_col2:
    st.markdown("""
    <div style="background-color: #18181b; padding: 30px; border-radius: 15px; border: 1px solid #27272a;">
    <h3 style="margin-top: 0;">Send a Message</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form"):
        name = st.text_input("Your Name", placeholder="Enter your full name")
        email = st.text_input("Email Address", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Tell me about your project or just say hello!")
        
        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
        
        if submitted:
            if not name or not email or not message:
                st.error("Please fill in all fields.")
            else:
                # --- EMAIL CONFIGURATION ---
                my_email = "srinjoysamanta73@gmail.com"
                my_app_password = "lyrq iwgo jhrs iizt" # <--- YOUR PASSWORD
                
                # Create the email structure
                msg = MIMEMultipart()
                msg['From'] = my_email
                msg['To'] = my_email
                msg['Subject'] = f"New Portfolio Message from {name}"
                
                body = f"""
                You have received a new message from your Portfolio Website.
                
                Name: {name}
                Email: {email}
                
                Message:
                {message}
                """
                msg.attach(MIMEText(body, 'plain'))
                
                try:
                    # ALTERNATIVE: Use SMTP_SSL on Port 465 (More reliable on some networks)
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    # No need for starttls() with SMTP_SSL
                    
                    server.login(my_email, my_app_password)
                    server.send_message(msg)
                    server.quit()
                    
                    st.success("Message sent! Check your 'Sent' folder in Gmail.")
                    st.balloons()
                    
                    # Print to console so you can see it working
                    print(f"SUCCESS: Email sent to {my_email}")
                    
                except Exception as e:
                    st.error(f"Error sending email: {e}")
                    # Print exact error to console
                    print(f"FAILED: {e}")

# --- 8. FOOTER ---
st.markdown("""
<br><br>
<div style="text-align: center; color: #52525b; padding: 20px;">
    Built by Srinjoy Samanta • 2026
</div>
""", unsafe_allow_html=True)