import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="Safety Detection System",
    page_icon="🛡️",
    layout="wide"
)

#CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Roboto:wght@300;400;500;700;900&display=swap');

:root {
    --primary-gradient: linear-gradient(145deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.95), rgba(51, 65, 85, 0.95));
    --accent-color: #FF6B35;
    --accent-gradient: linear-gradient(135deg, #FF6B35, #F7931E, #FFB020);
    --text-primary: #FFFFFF;
    --text-secondary: #E2E8F0;
    --text-muted: #94A3B8;
    --surface-glass: rgba(15, 23, 42, 0.9);
    --border-color: rgba(148, 163, 184, 0.2);
    --shadow-medium: 0 8px 32px rgba(0, 0, 0, 0.3);
    --turquoise-green: #40E0D0;
}

/* Smooth transitions for all elements */
* {
    transition: all 0.3s ease;
}

html, body, [data-testid="stAppViewContainer"] {
    background-image: linear-gradient(rgba(0, 15, 30, 0.7), rgba(0, 25, 50, 0.8)), url("https://hsseworld.com/wp-content/uploads/2021/01/wearables-safety-Tec.jpg");
    background-size: cover;
    background-attachment: fixed;
    background-repeat: no-repeat;
    background-position: center;
    color: SpanishGreen;
    font-family: 'Century', sans-serif;
    font-weight: 500;
    transition: all 0.5s ease;
}

[data-testid="stAppViewContainer"] > .main {
    padding: 2rem 3rem;
    max-width: 1200px;
    margin: 0 auto;
    transition: padding 0.3s ease;
}

/* Responsive padding for main container */
@media (max-width: 768px) {
    [data-testid="stAppViewContainer"] > .main {
        padding: 1rem 1.5rem;
    }
}

@media (max-width: 480px) {
    [data-testid="stAppViewContainer"] > .main {
        padding: 0.5rem 1rem;
    }
}

section[data-testid="stSidebar"] {
    background: var(--primary-gradient);
    backdrop-filter: blur(16px) saturate(150%);
    border-right: 1px solid var(--border-color);
    box-shadow: var(--shadow-medium);
    transition: all 0.4s ease;
}

/* Sidebar responsive behavior */
@media (max-width: 768px) {
    section[data-testid="stSidebar"] {
        width: 100% !important;
        position: fixed;
        z-index: 999;
        transform: translateX(-100%);
        transition: transform 0.3s ease;
    }
    
    section[data-testid="stSidebar"]:hover,
    section[data-testid="stSidebar"]:focus-within {
        transform: translateX(0);
    }
}

/* Enhanced Headers with TranslateX Effects and Responsive Design */
h1, h2, h3, h4, h5, h6 {
    color: #40E0D0 !important;
    font-family: 'Century', serif;
    transform: translateX(100px);
    transition: all 3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    opacity: 0;
    animation: headerSlideIn 2s ease-out forwards;
    position: relative;
    overflow: hidden;
}

/* Paragraph styling - Added this section */
p {
    font-size: clamp(0.95rem, 2vw, 1.1rem);
    line-height: 1.8;
    color: var(--text-secondary);
    margin: 1.5rem 0;
    padding: 0 1rem;
    max-width: 100%;
    text-align: justify;
    transition: all 0.3s ease;
    opacity: 0;
    animation: fadeIn 0.8s ease 0.4s forwards;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Responsive paragraph styling */
@media (max-width: 768px) {
    p {
        font-size: clamp(0.9rem, 2.5vw, 1rem);
        padding: 0 0.5rem;
        margin: 1.2rem 0;
    }
}

@media (max-width: 480px) {
    p {
        font-size: clamp(0.85rem, 3vw, 0.95rem);
        padding: 0;
        margin: 1rem 0;
        line-height: 1.7;
    }
}

/* Header slide-in animation */
@keyframes headerSlideIn {
    0% {
        transform: translateX(100px);
        opacity: 0;
    }
    100% {
        transform: translateX(0);
        opacity: 1;
    }
}

/* Individual header responsiveness and effects */
h1 {
    font-size: clamp(2rem, 5vw, 3.5rem);
    animation-delay: 0.2s;
    transition: all 3s ease, transform 0.5s ease;
}

h1:hover {
    transform: translateX(20px) scale(1.05);
    text-shadow: 0 0 20px rgba(64, 224, 208, 0.6);
    filter: brightness(1.2);
}

h2 {
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    animation-delay: 0.4s;
    transition: all 3s ease, transform 0.5s ease;
}

h2:hover {
    transform: translateX(15px) scale(1.03);
    text-shadow: 0 0 15px rgba(64, 224, 208, 0.5);
}

h3 {
    font-size: clamp(1.3rem, 3.5vw, 2rem);
    animation-delay: 0.6s;
    transition: all 3s ease, transform 0.5s ease;
}

h3:hover {
    transform: translateX(12px) scale(1.02);
    text-shadow: 0 0 12px rgba(64, 224, 208, 0.4);
}

h4 {
    font-size: clamp(1.1rem, 3vw, 1.5rem);
    animation-delay: 0.8s;
    transition: all 3s ease, transform 0.5s ease;
}

h4:hover {
    transform: translateX(10px) scale(1.01);
    text-shadow: 0 0 10px rgba(64, 224, 208, 0.3);
}

h5 {
    font-size: clamp(1rem, 2.5vw, 1.3rem);
    animation-delay: 1s;
    transition: all 3s ease, transform 0.5s ease;
}

h5:hover {
    transform: translateX(8px);
    text-shadow: 0 0 8px rgba(64, 224, 208, 0.2);
}

h6 {
    font-size: clamp(0.9rem, 2vw, 1.1rem);
    animation-delay: 1.2s;
    transition: all 3s ease, transform 0.5s ease;
}

h6:hover {
    transform: translateX(6px);
    text-shadow: 0 0 6px rgba(64, 224, 208, 0.1);
}

/* Responsive header adjustments for mobile */
@media (max-width: 768px) {
    h1, h2, h3, h4, h5, h6 {
        transform: translateX(50px);
        transition: all 2s ease;
    }
    
    @keyframes headerSlideIn {
        0% {
            transform: translateX(50px);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover {
        transform: translateX(10px) scale(1.02);
    }
}

@media (max-width: 480px) {
    h1, h2, h3, h4, h5, h6 {
        transform: translateX(30px);
        transition: all 1.5s ease;
    }
    
    @keyframes headerSlideIn {
        0% {
            transform: translateX(30px);
            opacity: 0;
        }
        100% {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    h1:hover, h2:hover, h3:hover, h4:hover, h5:hover, h6:hover {
        transform: translateX(5px) scale(1.01);
    }
}

/* Special header effects for Streamlit components */
div[data-testid="stMarkdown"] h1,
div[data-testid="stMarkdown"] h2,
div[data-testid="stMarkdown"] h3,
div[data-testid="stMarkdown"] h4,
div[data-testid="stMarkdown"] h5,
div[data-testid="stMarkdown"] h6 {
    position: relative;
    overflow: visible;
}

div[data-testid="stMarkdown"] h1::before,
div[data-testid="stMarkdown"] h2::before,
div[data-testid="stMarkdown"] h3::before {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, #40E0D0, #00FFFF);
    transition: width 1s ease-out 3.2s;
    border-radius: 2px;
}

div[data-testid="stMarkdown"] h1:hover::before,
div[data-testid="stMarkdown"] h2:hover::before,
div[data-testid="stMarkdown"] h3:hover::before {
    width: 100%;
    transition: width 0.5s ease-out;
}

/* Load animation trigger */
div[data-testid="stMarkdown"]:hover h1,
div[data-testid="stMarkdown"]:hover h2,
div[data-testid="stMarkdown"]:hover h3,
div[data-testid="stMarkdown"]:hover h4,
div[data-testid="stMarkdown"]:hover h5,
div[data-testid="stMarkdown"]:hover h6 {
    animation: none;
}

/* Page load header sequence */
.header-sequence-1 { animation-delay: 0.2s; }
.header-sequence-2 { animation-delay: 0.6s; }
.header-sequence-3 { animation-delay: 1.0s; }
.header-sequence-4 { animation-delay: 1.4s; }
.header-sequence-5 { animation-delay: 1.8s; }

/* Title without box - with responsive scaling and enhanced effects - UPDATED WITH BETTER SPACING AND GRADIENT SHADOW */
.title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 900;
    color: var(--turquoise-green);
    text-align: center;
    font-family: 'Century', serif;
    letter-spacing: -0.5px;
    line-height: 1.1;
    margin: 3rem auto 2rem; /* INCREASED SPACING: top margin from 2rem to 3rem, bottom from 0.5rem to 2rem */
    transform: translateX(150px);
    transition: all 3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    opacity: 0;
    animation: titleSlideIn 2.5s ease-out forwards;
    position: relative;
    /* ADDED GRADIENT SHADOW BEHIND TITLE */
    text-shadow: 
        0 0 20px rgba(64, 224, 208, 0.8),
        0 0 40px rgba(64, 224, 208, 0.6),
        0 0 80px rgba(64, 224, 208, 0.4),
        2px 2px 0px rgba(0, 0, 0, 0.8);
}

/* ENHANCED GRADIENT SHADOW BACKGROUND */
.title::before {
    content: '';
    position: absolute;
    top: -10px;
    left: -20px;
    right: -20px;
    bottom: -10px;
    background: linear-gradient(
        135deg,
        rgba(64, 224, 208, 0.1) 0%,
        rgba(0, 255, 255, 0.05) 50%,
        rgba(64, 224, 208, 0.1) 100%
    );
    border-radius: 15px;
    z-index: -1;
    opacity: 0;
    transition: opacity 0.5s ease;
}

.title:hover::before {
    opacity: 1;
}

@keyframes titleSlideIn {
    0% {
        opacity: 0;
        transform: translateX(150px) rotateY(45deg);
    }
    70% {
        transform: translateX(-10px) rotateY(0deg);
    }
    100% {
        opacity: 1;
        transform: translateX(0) rotateY(0deg);
    }
}

.title:hover {
    transform: translateX(25px) scale(1.05);
    text-shadow: 
        0 0 30px rgba(64, 224, 208, 1),
        0 0 60px rgba(64, 224, 208, 0.8),
        0 0 100px rgba(64, 224, 208, 0.6),
        3px 3px 0px rgba(0, 0, 0, 0.9);
    filter: brightness(1.3);
}

/* Responsive title scaling */
@media (max-width: 768px) {
    .title {
        font-size: clamp(1.8rem, 6vw, 2.5rem);
        margin: 2rem auto 1.5rem; /* ADJUSTED FOR MOBILE */
        transform: translateX(80px);
    }
    
    @keyframes titleSlideIn {
        0% {
            opacity: 0;
            transform: translateX(80px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .title:hover {
        transform: translateX(15px) scale(1.03);
    }
}

@media (max-width: 480px) {
    .title {
        font-size: clamp(1.5rem, 7vw, 2rem);
        margin: 1.5rem auto 1rem; /* ADJUSTED FOR SMALL MOBILE */
        transform: translateX(50px);
    }
    
    .title:hover {
        transform: translateX(8px) scale(1.02);
    }
}

/* New subtitle styling */
.title-subtitle {
    font-size: clamp(1rem, 3vw, 1.25rem);
    font-weight: 600;
    color: white !important;
    text-align: center;
    margin: 0.5rem auto 2.5rem; /* INCREASED BOTTOM MARGIN from 1.5rem to 2.5rem for better spacing */
    letter-spacing: 0.3px;
    font-family: 'Roboto', sans-serif;
    transition: all 0.4s ease;
    opacity: 0;
    animation: subtitleFadeIn 1s ease 0.5s forwards;
    transform: translateY(20px);
}

@keyframes subtitleFadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.title-subtitle:hover {
    color: #E2E8F0 !important;
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
    
}

/* Responsive title subtitle */
@media (max-width: 768px) {
    .title-subtitle {
        margin: 0.25rem auto 2rem; /* INCREASED BOTTOM MARGIN */
        font-size: clamp(0.9rem, 3.5vw, 1.1rem);
    }
}

@media (max-width: 480px) {
    .title-subtitle {
        margin: 0.15rem auto 1.5rem; /* INCREASED BOTTOM MARGIN */
        padding: 0 1rem;
    }
}

    /* Professional Subtitle - white */
    .subtitle {
        font-size: 28px;
        color: #0EA5E9;
        font-weight: 600;
        text-shadow: 0 2px 8px rgba(14, 165, 233, 0.4), 0 1px 3px rgba(0, 0, 0, 0.6);
        margin-bottom: 30px;
        text-align: center;
        font-family: 'Century', serif;
        letter-spacing: 0.5px;
        line-height: 1.3;
        background: linear-gradient(135deg, #0EA5E9 0%, #3B82F6 50%, #6366F1 100%);
        #-webkit-background-clip: text;
        #-webkit-text-fill-color: transparent;
        background-clip: text;
    }
/* Responsive subtitle */
@media (max-width: 768px) {
    .subtitle {
        margin-bottom: 2rem; /* INCREASED from 1.5rem to 2rem */
        font-size: clamp(0.9rem, 3.5vw, 1.1rem);
    }
}

@media (max-width: 480px) {
    .subtitle {
        margin-bottom: 1.5rem; /* INCREASED from 1rem to 1.5rem */
        padding: 0 1rem;
    }
}

/* Cards - responsive with enhanced transitions - UPDATED WITH HOVER ANIMATIONS */
.card-row {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    margin-top: 3rem; /* INCREASED from 2rem to 3rem for better spacing */
    transition: all 0.3s ease;
}

/* Responsive card row */
@media (max-width: 768px) {
    .card-row {
        gap: 1.5rem;
        margin-top: 2rem; /* INCREASED from 1.5rem to 2rem */
    }
}

@media (max-width: 480px) {
    .card-row {
        gap: 1rem;
        margin-top: 1.5rem; /* INCREASED from 1rem to 1.5rem */
        flex-direction: column;
        align-items: center;
    }
}

.card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: var(--shadow-medium);
    border-radius: 1rem;
    padding: 1.5rem;
    width: 280px;
    max-width: 100%;
    color: white;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    opacity: 0;
    transform: translateY(30px);
    animation: cardFadeIn 0.6s ease forwards;
    position: relative;
    overflow: hidden;
}

/* ENHANCED HOVER ANIMATIONS FOR MISSION/VISION CARDS */
.card:hover {
    transform: translateY(-12px) scale(1.03); /* ENHANCED: more lift and scale */
    box-shadow: 
        0 20px 60px rgba(0, 0, 0, 0.7),
        0 0 40px rgba(64, 224, 208, 0.3); /* ADDED: turquoise glow */
    border-color: rgba(64, 224, 208, 0.5);
    background: rgba(255, 255, 255, 0.1); /* ENHANCED: brighter background on hover */
}

/* ADDED: Animated background effect on hover */
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(64, 224, 208, 0.1),
        transparent
    );
    transition: left 0.6s ease;
    z-index: 0;
}

.card:hover::before {
    left: 100%;
}

/* ENSURE TEXT STAYS ON TOP */
.card > * {
    position: relative;
    z-index: 1;
}

@keyframes cardFadeIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive cards */
@media (max-width: 768px) {
    .card {
        width: calc(50% - 1rem);
        min-width: 250px;
        padding: 1.25rem;
    }
}

@media (max-width: 480px) {
    .card {
        width: 100%;
        max-width: 350px;
        padding: 1rem;
    }
}

.card h3 {
    margin-top: 0;
    color: #40E0D0;
    font-size: clamp(1.2rem, 2.5vw, 1.5rem);
    transition: all 0.3s ease; /* ENHANCED transition */
}

.card:hover h3 {
    color: #00FFFF;
    text-shadow: 0 0 15px rgba(0, 255, 255, 0.7); /* ENHANCED glow */
    transform: translateY(-2px); /* ADDED: slight lift on hover */
}

.card p {
    font-size: clamp(0.85rem, 2vw, 0.95rem);
    width: 100vw;
    height: 100vh;                
    line-height: 1.6;
    color: var(--text-secondary);
    transition: all 0.3s ease; /* ENHANCED transition */
}

.card:hover p {
    color: var(--text-primary);
    transform: translateX(5px); /* ADDED: slight shift on hover */
}

/* About card responsive styling */
/* Card entrance animation */
@keyframes cardFadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/*  About Card Styling */
/* Entrance animation */
@keyframes cardFadeIn {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Ultra Slim Card Styling */
/* Card entrance animation */
@keyframes cardFadeIn {
    0% {
        opacity: 0;
        transform: translateY(10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Ultra-slim About Card Styling */
/* Card entrance animation */
@keyframes cardFadeIn {
    0% {
        opacity: 0;
        transform: translateY(10px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Ultra-slim About Card with SteelBlue background */
.about-card {
    background: SteelBlue; /* Your requested color */
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    height: 18px; /* Slim height */
    padding: 0 0.75rem; /* Only side padding */
    margin: 1rem 0;
    transition: all 0.3s ease;
    opacity: 0;
    transform: translateY(10px);
    animation: cardFadeIn 0.5s ease forwards;

    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

/* Hover effect */
.about-card:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    border-color: rgba(64, 224, 208, 0.2);
}

/* Responsive tweaks for smaller screens */
@media (max-width: 768px) {
    .about-card {
        height: 16px;
        padding: 0 0.5rem;
        margin: 0.75rem 0;
    }
}

@media (max-width: 480px) {
    .about-card {
        padding: 1rem;
        margin: 0.75rem 0;
    }
}

/* Streamlit component responsiveness */
div[data-testid="column"] {
    transition: all 0.3s ease;
}

/* Responsive columns */
@media (max-width: 768px) {
    div[data-testid="column"] {
        width: 100% !important;
        margin-bottom: 1rem;
    }
}

/* Button hover effects */
button[kind="primary"] {
    transition: all 0.3s ease !important;
}

button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
}

/* File uploader responsiveness */
div[data-testid="stFileUploader"] {
    transition: all 0.3s ease;
}

@media (max-width: 768px) {
    div[data-testid="stFileUploader"] {
        margin-bottom: 1rem;
    }
}

/* Image display responsiveness */
div[data-testid="stImage"] {
    transition: all 0.3s ease;
}

div[data-testid="stImage"]:hover {
    transform: scale(1.02);
}

/* Slider responsiveness */
div[data-testid="stSlider"] {
    transition: all 0.3s ease;
}

/* Detection stats styling */
.detection-stats {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 1rem;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.4s ease;
    animation: cardFadeIn 0.6s ease forwards;
}

.detection-stats:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
}

/* Responsive detection stats */
@media (max-width: 768px) {
    .detection-stats {
        padding: 1rem;
    }
}

@media (max-width: 480px) {
    .detection-stats {
        padding: 0.75rem;
        margin: 0.5rem 0;
    }
}

/* Smooth page transitions */
.main > div {
    animation: pageTransition 0.5s ease-in-out;
}

@keyframes pageTransition {
    from {
        opacity: 0;
        transform: translateX(20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* Loading spinner enhancement */
div[data-testid="stSpinner"] {
    transition: all 0.3s ease;
}

/* Responsive text sizing */
@media (max-width: 768px) {
    p, div, span {
        font-size: clamp(0.85rem, 2.5vw, 1rem) !important;
    }
}

@media (max-width: 480px) {
    p, div, span {
        font-size: clamp(0.8rem, 3vw, 0.9rem) !important;
    }
}

/* Enhanced selectbox styling */
div[data-baseweb="select"] {
    transition: all 0.3s ease;
}

div[data-baseweb="select"]:hover {
    transform: translateY(-1px);
}

/* Enhanced dataframe styling */
div[data-testid="stDataFrame"] {
    transition: all 0.3s ease;
    border-radius: 0.5rem;
    overflow: hidden;
}

div[data-testid="stDataFrame"]:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}

/* Mobile navigation enhancement */
@media (max-width: 768px) {
    section[data-testid="stSidebar"] > div:first-child::before {
        content: "☰ Menu";
        position: fixed;
        top: 1rem;
        left: 1rem;
        background: var(--primary-gradient);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-size: 0.9rem;
        z-index: 1000;
        cursor: pointer;
        transition: all 0.3s ease;
    }
}

/* Progress bar styling */
div[data-testid="stProgress"] {
    transition: all 0.3s ease;
}

/* Alert styling */
div[data-testid="stAlert"] {
    transition: all 0.3s ease;
    border-radius: 0.5rem;
}

div[data-testid="stAlert"]:hover {
    transform: translateY(-1px);
}

/* Metric styling */
div[data-testid="metric-container"] {
    transition: all 0.3s ease;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-2px);
}

</style>
""", unsafe_allow_html=True)



# Navigation
def main():
    # Add page transition wrapper
    st.markdown('<div class="page-transition-wrapper">', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["About Us", "Safety Detection App"])
    
    # Add gradient bar after title
    st.markdown('<div class="gradient-bar"></div>', unsafe_allow_html=True)
    
    if page == "About Us":
        show_about_page()
    elif page == "Safety Detection App":
        show_detection_app()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_about_page():
    # App header
    st.markdown("<div class='title'> 🦺 Safety Detection System</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Ensuring Safety Through AI-Powered Detection</div>", unsafe_allow_html=True)
    
    # About Us content
    st.markdown("<div class='about-card'>", unsafe_allow_html=True)
    #Wst.markdown("##  👥 About Our Project")
    st.markdown("""
    Welcome to the Safety Detection System - an innovative solution that leverages artificial intelligence 
    to enhance workplace safety through automated detection of personal protective equipment (PPE).
    
    Our system uses state-of-the-art YOLO (You Only Look Once) deep learning technology to identify 
    and verify the presence of essential safety equipment in real-time, helping organizations maintain 
    compliance with safety regulations and protect their workforce.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
    
  
    # Technology Stack
    st.markdown("<div class='about-card'>", unsafe_allow_html=True)
    # st.markdown("### 🛠️ Technology Stack")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        **Machine Learning**
        - YOLO (Ultralytics)
        - OpenCV
        - PIL/Pillow
        """)
    
    with tech_col2:
        st.markdown("""
        **Web Framework**
        - Streamlit
        - Python
        - Pandas
        """)
    
    with tech_col3:
        st.markdown("""
        **Visualization**
        - Matplotlib
        - NumPy
        - CSS Styling
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # How to Use Section
    st.markdown("<div class='about-card'>", unsafe_allow_html=True)
    # st.markdown("### 📋 About the Application")
    st.markdown("""
    This application uses a YOLO model trained for safety equipment detection.
    
    **How to use:**
    1. Enter the path to your trained model
    2. Upload an image
    3. Adjust confidence threshold if needed
    4. Click 'Run Detection'
    5. View results and statistics
    """)
    st.markdown("</div>", unsafe_allow_html=True)

def show_detection_app():
    # Import required libraries for detection app
    import os
    import tempfile
    from PIL import Image
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from ultralytics import YOLO
    import cv2
    import warnings
    warnings.filterwarnings("ignore")

    # CSS with all requested changes
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

:root {
    --turquoise-green: #40E0D0;
    --section-bg: #1E293B;
    --button-primary: #3B82F6;
    --button-hover: #2563EB;
    --button-secondary: #94A3B8;
    --button-secondary-hover: #64748B;
}

/* Apply Inter font to all elements */
html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif !important;
}

/* Title styling */
.title {
    font-size: clamp(2rem, 5vw, 3.5rem);
    font-weight: 900;
    color: var(--turquoise-green);
    text-align: center;
    margin-top: 0rem;
    margin-bottom: 1.5rem;
    transform: translateX(150px);
    opacity: 0;
    animation: titleSlideIn 2.5s ease-out forwards;
    text-shadow: 0 0 20px rgba(64, 224, 208, 0.8),
                 0 0 40px rgba(64, 224, 208, 0.6);
    padding-top: 0 !important;
    position: relative;
    z-index: 1;
}

/* Subtitle styling */
.subtitle {
    font-size: 1.25rem;
    text-align: center;
    color: #94A3B8;
    margin-bottom: 2rem;
    opacity: 0;
    animation: fadeIn 1.2s ease-out 0.4s forwards;
}

/* Section boxes styling */
.st-emotion-cache-1vbkxwb, .st-emotion-cache-1p1nwyz {
    background-color: var(--section-bg);
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
}

/* File uploader section */
.st-emotion-cache-1vbkxwb p {
    color: white !important;
    text-align: center !important;
    margin-bottom: 1rem !important;
}

/* Buttons styling */
div.stButton > button:first-child {
    font-family: 'Inter', sans-serif !important;
    height: 40px !important;
    width: 100% !important;
    padding: 0 20px !important;
    color: white !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    border: none !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* Primary button (Run Detection) */
div.stButton > button:first-child {
    background-color: var(--button-primary) !important;
}

div.stButton > button:first-child:hover {
    background-color: var(--button-hover) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
}

/* File uploader button */
.st-emotion-cache-13ln4jf {
    background-color: var(--button-secondary) !important;
}

.st-emotion-cache-13ln4jf:hover {
    background-color: var(--button-secondary-hover) !important;
}

/* Center all text in sections */
.st-emotion-cache-16idsys p, 
.st-emotion-cache-16idsys h1, 
.st-emotion-cache-16idsys h2, 
.st-emotion-cache-16idsys h3, 
.st-emotion-cache-16idsys h4, 
.st-emotion-cache-16idsys h5, 
.st-emotion-cache-16idsys h6 {
    text-align: center !important;
}

/* Title animation */
@keyframes titleSlideIn {
    0% { transform: translateX(150px); opacity: 0; }
    100% { transform: translateX(0); opacity: 1; }
}

/* Fade-in animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Detection results section */
.detection-stats {
    background-color: var(--section-bg);
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 1rem;
}

/* Spacing between sections */
.st-emotion-cache-1q7spjk {
    margin: 30px 0 !important;
}
</style>
""", unsafe_allow_html=True)

    # --- Display the custom title and optional subtitle ---
    st.markdown("<div class='title'>🦺 Safety Detection System</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Upload an image for safety equipment detection</div>", unsafe_allow_html=True)

    # Function to load the model
    @st.cache_resource
    def load_model(model_path):
        return YOLO(model_path)

    # Model path
    model_path = st.sidebar.text_input(
        "Model Path",
        value="best.pt",
        help="Enter the path to your trained YOLO model"
    )

    # Load model
    try:
        with st.spinner("Loading YOLO model..."):
            model = load_model(model_path)
        st.sidebar.success("Model Imported!")
    except Exception as e:
        st.sidebar.error(f"Error loading model: {e}")
        model = None

    # Confidence threshold slider
    conf_threshold = st.sidebar.slider(
        "Detection Confidence Threshold",
        min_value=0.1,
        max_value=1.0,
        value=0.25,
        step=0.05,
    )

    # Create two columns for input and output
    col1, spacer, col2 = st.columns([4, 1, 4])
    
    # File uploader section
    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png", "webp"])

        if uploaded_file is not None:
            # Create a temporary file to save the uploaded image
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                temp_file_path = tmp_file.name

            # Display original image
            image = Image.open(uploaded_file)
            st.image(image, caption="Original Image", use_container_width=True)

    # Spacer between sections
    st.markdown("<div style='margin: 30px 0;'></div>", unsafe_allow_html=True)

    # Process and display results
    with col2:
        st.subheader("Detection Results")
        
        if uploaded_file is not None and model is not None:
            if st.button("Run Detection"):
                with st.spinner("Processing..."):
                    # Run the model on the uploaded image
                    results = model.predict(
                        source=temp_file_path,
                        conf=conf_threshold,
                        save=True
                    )

                    # Display detected image
                    for r in results:
                        # Get the plotting array
                        im_array = r.plot()
                        im = Image.fromarray(im_array[..., ::-1])  # RGB to BGR
                        st.image(im, caption="Detected Objects", use_container_width=True)

                        # Extract and display detection statistics
                        boxes = r.boxes

                        if len(boxes) > 0:
                            # Create dataframe for detections
                            detections_data = []
                            class_names = model.names

                            # Count detections by class
                            class_counts = {}
                            for box in boxes:
                                cls_id = int(box.cls[0].item())
                                cls_name = class_names[cls_id]
                                conf = box.conf[0].item()

                                if cls_name in class_counts:
                                    class_counts[cls_name] += 1
                                else:
                                    class_counts[cls_name] = 1

                                # Add detection to data list
                                x1, y1, x2, y2 = [int(i) for i in box.xyxy[0].tolist()]
                                detections_data.append({
                                    "Class": cls_name,
                                    "Confidence": f"{conf:.2f}",
                                    "Coordinates": f"({x1}, {y1}, {x2}, {y2})"
                                })

                            # Display statistics
                            st.markdown("<div class='detection-stats'>", unsafe_allow_html=True)
                            st.subheader("Detection Statistics")

                            # Total detections count
                            total_detections = len(boxes)
                            st.markdown(f"**Total detections:** {total_detections}")

                            # Class distribution
                            st.markdown("**Class distribution:**")

                            # Create a horizontal bar chart for class distribution
                            if class_counts:
                                fig, ax = plt.subplots(figsize=(8, max(3, len(class_counts) * 0.5)))
                                classes = list(class_counts.keys())
                                counts = list(class_counts.values())

                                y_pos = np.arange(len(classes))
                                ax.barh(y_pos, counts, align='center')
                                ax.set_yticks(y_pos)
                                ax.set_yticklabels(classes)
                                ax.invert_yaxis()  # Labels read top-to-bottom
                                ax.set_xlabel('Count')
                                ax.set_title('Detection Class Distribution')

                                st.pyplot(fig)

                            # Show detailed detection information
                            if detections_data:
                                st.markdown("**Detailed Detections:**")
                                st.dataframe(pd.DataFrame(detections_data))

                            st.markdown("</div>", unsafe_allow_html=True)
                        else:
                            st.warning("No objects detected in the image.")

                    # Clean up the temporary file
                    os.unlink(temp_file_path)


if __name__ == "__main__":
    main()