import os
import re

# ==============================================================================
# MASTER CSS CONTENT (All CSS in one string for inline injection)
# This is the exact content from Step 1.
# ==============================================================================
MASTER_INLINE_CSS = r'''
/* --- MASTER INLINE STYLES --- */

/* --- 0. Base HTML and Body Setup (Crucial for full background) --- */
html, body {
    height: 100%; /* Ensure both html and body take full height of the viewport */
    margin: 0;
    padding: 0; /* Remove default browser padding/margin */
    overflow-x: hidden; /* Prevent horizontal scrollbar from overflow */
}

/* --- 1. Main Site Layout & Structure --- */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f4f4f9; /* Default light background */
    color: #333; /* Default light text color */
    transition: background-color 0.3s, color 0.3s;
}

.header-container, header { /* Styles for main headers on index and content pages */
    text-align: center;
    margin-bottom: 40px;
    padding: 25px 10px;
    font-size: 1.8em;
    font-weight: bold;
    color: white; /* Header text color in light mode (default) */
    /* Will be overridden by theme-specific header colors, but dark mode should revert to white */
}

.logo {
    max-width: 100%;
    height: auto;
    max-height: 80px;
}

.container { /* For the main index page cards */
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 25px;
    padding: 40px 20px; /* Padding for the main card container */
    box-sizing: border-box; /* Include padding in width/height calculation */
}

.card { /* For individual cards on the index page */
    background-color: #ffffff;
    padding: 20px;
    width: 280px;
    min-height: 80px;
    text-align: center;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    border-left: 5px solid transparent; /* For theme color accent */
}

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }

a {
    text-decoration: none;
    color: #333; /* Default link color in light mode */
    font-weight: 600;
    font-size: 1.1rem;
    transition: color 0.3s;
}

footer {
    margin-top: 50px;
    text-align: center;
    font-size: 14px;
    color: #777; /* Default footer text color in light mode */
    transition: color 0.3s;
}

/* Content Page Specific Styles (for sections like Benefits, Risks, etc.) */
.content-section {
    max-width: 720px;
    margin: 0 auto 40px;
    background: white; /* Default light background for content sections */
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transition: background-color 0.3s, box-shadow 0.3s;
}

.section-box { /* Individual boxes within content sections */
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    transition: background-color 0.3s, box-shadow 0.3s;
}

h2 {
    text-align: center;
    margin-bottom: 30px;
}

h3 {
    padding-left: 10px;
    margin-top: 20px;
    border-left-width: 5px;
    border-left-style: solid;
    transition: color 0.3s, border-color 0.3s;
}

ul {
    padding-left: 20px;
}

li {
    margin-bottom: 10px;
}

p {
    margin-bottom: 15px;
}

/* Styles for High-Yield/Full Script Toggle (labels above the switch) */
.toggle-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 30px;
    background-color: #f0f0f0; /* Light background for the wrapper */
    border-radius: 30px;
    padding: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    max-width: 350px; /* Constrain width to look better */
    margin-left: auto;
    margin-right: auto;
}

.toggle-label {
    padding: 10px 20px;
    cursor: pointer;
    font-weight: bold;
    color: #666; /* Default text color */
    transition: color 0.3s, background-color 0.3s;
    border-radius: 20px; /* For the highlighted effect */
    user-select: none; /* Prevent text selection on click */
    white-space: nowrap; /* Prevent wrapping */
}

    .toggle-label.active {
        color: white; /* Text color when active */
        background-color: #66bb6a; /* Default Green for active label (matches Medication theme) */
        box-shadow: 0 0 0 rgba(0,0,0,0); /* REMOVED STICKING OUT SHADOW */
    }

/* Switch styling itself */
.toggle-container {
    position: relative;
    width: 60px;
    height: 30px;
    margin: 0 15px; /* Space between labels and switch */
    flex-shrink: 0; /* Prevent shrinking on small screens */
}

    .toggle-container .switch {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc; /* Grey when off */
        transition: .4s;
        border-radius: 30px;
    }

        .toggle-container .switch:before {
            position: absolute;
            content: "";
            height: 22px;
            width: 22px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }

        .toggle-container .switch.active {
            background-color: #66bb6a; /* Default Green when on (matches Medication theme) */
        }

            .toggle-container .switch.active:before {
                transform: translateX(30px); /* Slide to the right */
            }

/* Styles for content sections being hidden/shown */
.content-section {
    display: none; /* Hidden by default */
}

    .content-section.active {
        display: block; /* Shown when active */
    }


/* --- 2. Color Themes for LIGHT Mode --- */
/* These define the specific colors for each station type when in LIGHT mode */

/* Blue Theme (Diagnosis)
   Primary: #0d47a1 (Dark Blue)
   Accent: #42a5f5 (Lighter Blue)
   Background: #e3f2fd (Very Light Blue) */
.theme-blue header, .theme-blue h1, .theme-blue h2, .theme-blue a {
    color: #0d47a1;
}

.theme-blue .section-box {
    background: #e3f2fd;
}

.theme-blue h3 {
    color: #0d47a1;
    border-color: #42a5f5;
}

.theme-blue .header-container, .theme-blue header {
    background: linear-gradient(to right, #42a5f5, #0d47a1);
}

.theme-blue .card {
    border-color: #29b6f6;
}
/* For cards on main page */
.theme-blue .toggle-label.active, .theme-blue .toggle-container .switch.active {
    background-color: #42a5f5;
}


/* Green Theme (Medication)
   Primary: #1b5e20 (Dark Green)
   Accent: #66bb6a (Medium Green)
   Background: #e8f5e9 (Very Light Green) */
.theme-green header, .theme-green h1, .theme-green h2, .theme-green a {
    color: #1b5e20;
}

.theme-green .section-box {
    background: #e8f5e9;
}

.theme-green h3 {
    color: #1b5e20;
    border-color: #66bb6a;
}

.theme-green .header-container, .theme-green header {
    background: linear-gradient(to right, #66bb6a, #1b5e20);
}

.theme-green .card {
    border-color: #66bb6a;
}
/* For cards on main page */
.theme-green .toggle-label.active, .theme-green .toggle-container .switch.active {
    background-color: #66bb6a;
}


/* Orange Theme (Procedure)
   Primary: #e65100 (Dark Orange)
   Accent: #ffb74d (Lighter Orange)
   Background: #fff3e0 (Very Light Orange) */
.theme-orange header, .theme-orange h1, .theme-orange h2, .theme-orange a {
    color: #e65100;
}

.theme-orange .section-box {
    background: #fff3e0;
}

.theme-orange h3 {
    color: #e65100;
    border-color: #ffb74d;
}

.theme-orange .header-container, .theme-orange header {
    background: linear-gradient(to right, #ffb74d, #e65100);
}

.theme-orange .card {
    border-color: #ffa726;
}
/* For cards on main page */
.theme-orange .toggle-label.active, .theme-orange .toggle-container .switch.active {
    background-color: #ffa726;
}


/* Purple Theme (Post-Procedure/Psychiatry-related Medication)
   Primary: #4a148c (Dark Purple)
   Accent: #ce93d8 (Lighter Purple)
   Background: #f3e5f5 (Very Light Purple) */
.theme-purple header, .theme-purple h1, .theme-purple h2, .theme-purple a {
    color: #4a148c;
}

.theme-purple .section-box {
    background: #f3e5f5;
}

.theme-purple h3 {
    color: #4a148c;
    border-color: #ce93d8;
}

.theme-purple .header-container, .theme-purple header {
    background: linear-gradient(to right, #ce93d8, #4a148c);
}

.theme-purple .card {
    border-color: #ab47bc;
}
/* For cards on main page */
.theme-purple .toggle-label.active, .theme-purple .toggle-container .switch.active {
    background-color: #ab47bc;
}


/* Red Theme (Surgery)
   Primary: #b71c1c (Dark Red)
   Accent: #ef5350 (Medium Red)
   Background: #ffebee (Very Light Red) */
.theme-red header, .theme-red h1, .theme-red h2, .theme-red a {
    color: #b71c1c;
}

.theme-red .section-box {
    background: #ffebee;
}

.theme-red h3 {
    color: #b71c1c;
    border-color: #ef5350;
}

.theme-red .header-container, .theme-red header {
    background: linear-gradient(to right, #ef5350, #b71c1c);
}

.theme-red .card {
    border-color: #ef5350;
}
/* For cards on main page */
.theme-red .toggle-label.active, .theme-red .toggle-container .switch.active {
    background-color: #ef5350;
}


/* Terracotta Theme (Community)
   Primary: #bf360c (Dark Terracotta)
   Accent: #ffab91 (Lighter Terracotta)
   Background: #fff3e0 (Very Light Peach) */
.theme-terracotta header, .theme-terracotta h1, .theme-terracotta h2, .theme-terracotta a {
    color: #bf360c;
}

.theme-terracotta .section-box {
    background: #fff3e0;
}

.theme-terracotta h3 {
    color: #bf360c;
    border-color: #ffab91;
}

.theme-terracotta .header-container, .theme-terracotta header {
    background: linear-gradient(to right, #ffab91, #bf360c);
}

.theme-terracotta .card {
    border-color: #ff7043;
}
/* For cards on main page */
.theme-terracotta .toggle-label.active, .theme-terracotta .toggle-container .switch.active {
    background-color: #ff7043;
}


/* Teal Theme (Respiratory)
   Primary: #004d40 (Dark Teal)
   Accent: #4db6ac (Medium Teal)
   Background: #e0f2f1 (Very Light Teal) */
.theme-teal header, .theme-teal h1, .theme-teal h2, .theme-teal a {
    color: #004d40;
}

.theme-teal .section-box {
    background: #e0f2f1;
}

.theme-teal h3 {
    color: #004d40;
    border-color: #4db6ac;
}

.theme-teal .header-container, .theme-teal header {
    background: linear-gradient(to right, #4db6ac, #004d40);
}

.theme-teal .card {
    border-color: #4db6ac;
}
/* For cards on main page */
.theme-teal .toggle-label.active, .theme-teal .toggle-container .switch.active {
    background-color: #4db6ac;
}


/* Pink Theme (Diabetes)
   Primary: #ad1457 (Dark Pink)
   Accent: #f06292 (Medium Pink)
   Background: #fce4ec (Very Light Pink) */
.theme-pink header, .theme-pink h1, .theme-pink h2, .theme-pink a {
    color: #ad1457;
}

.theme-pink .section-box {
    background: #fce4ec;
}

.theme-pink h3 {
    color: #ad1457;
    border-color: #f06292;
}

.theme-pink .header-container, .theme-pink header {
    background: linear-gradient(to right, #f06292, #ad1457);
}

.theme-pink .card {
    border-color: #f06292;
}
/* For cards on main page */
.theme-pink .toggle-label.active, .theme-pink .toggle-container .switch.active {
    background-color: #f06292;
}


/* --- 3. Dark Mode Styles --- */
/* These override the above themes when .dark-mode is active */
body.dark-mode {
    background: #1f2023;
    color: #e0e0e0;
}

.dark-mode .card, .dark-mode .content-section {
    background-color: #2f3136;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
}

.dark-mode .section-box {
    background-color: #2a2c30;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.dark-mode a {
    color: #e0e0e0;
}
/* Default link color in dark mode */
.dark-mode footer {
    color: #999;
}

.dark-mode h1, .dark-mode h2 {
    color: #e0e0e0;
}
/* Header text color in dark mode */
.dark-mode p, .dark-mode li {
    color: #cccccc;
}
/* Ensure text inside boxes is readable */
.dark-mode header {
    color: white;
}
/* Ensure main header text is white in dark mode */

/* Dark Mode Theme Overrides - Adjust header and border colors for contrast */
.dark-mode.theme-blue header, .dark-mode.theme-blue h3, .dark-mode.theme-blue a {
    color: #82b1ff;
}
/* Lighter blue */
.dark-mode.theme-blue .toggle-label.active, .dark-mode.theme-blue .toggle-container .switch.active {
    background-color: #82b1ff;
}

.dark-mode.theme-green header, .dark-mode.theme-green h3, .dark-mode.theme-green a {
    color: #a5d6a7;
}
/* Lighter green */
.dark-mode.theme-green .toggle-label.active, .dark-mode.theme-green .toggle-container .switch.active {
    background-color: #a5d6a7;
}

.dark-mode.theme-orange header, .dark-mode.theme-orange h3, .dark-mode.theme-orange a {
    color: #ffcc80;
}
/* Lighter orange */
.dark-mode.theme-orange .toggle-label.active, .dark-mode.theme-orange .toggle-container .switch.active {
    background-color: #ffcc80;
}

.dark-mode.theme-purple header, .dark-mode.theme-purple h3, .dark-mode.theme-purple a {
    color: #e1bee7;
}
/* Lighter purple */
.dark-mode.theme-purple .toggle-label.active, .dark-mode.theme-purple .toggle-container .switch.active {
    background-color: #e1bee7;
}

.dark-mode.theme-red header, .dark-mode.theme-red h3, .dark-mode.theme-red a {
    color: #ff8a80;
}
/* Lighter red */
.dark-mode.theme-red .toggle-label.active, .dark-mode.theme-red .toggle-container .switch.active {
    background-color: #ff8a80;
}

.dark-mode.theme-terracotta header, .dark-mode.theme-terracotta h3, .dark-mode.theme-terracotta a {
    color: #ffccbc;
}
/* Lighter terracotta */
.dark-mode.theme-terracotta .toggle-label.active, .dark-mode.theme-terracotta .toggle-container .switch.active {
    background-color: #ffccbc;
}

.dark-mode.theme-teal header, .dark-mode.theme-teal h3, .dark-mode.theme-teal a {
    color: #80cbc4;
}
/* Lighter teal */
.dark-mode.theme-teal .toggle-label.active, .dark-mode.theme-teal .toggle-container .switch.active {
    background-color: #80cbc4;
}

.dark-mode.theme-pink header, .dark-mode.theme-pink h3, .dark-mode.theme-pink a {
    color: #f48fb1;
}
/* Lighter pink */
.dark-mode.theme-pink .toggle-label.active, .dark-mode.theme-pink .toggle-container .switch.active {
    background-color: #f48fb1;
}


/* --- 4. Media Queries for Mobile-Friendly Layout --- */
@media screen and (max-width: 768px) {
    .container {
        padding: 20px;
    }
    /* Adjust padding for cards on smaller screens */
    .card {
        width: 45%;
    }

    .toggle-wrapper {
        flex-direction: column;
        gap: 10px;
        padding: 10px;
    }

    .toggle-label {
        width: 80%;
        text-align: center;
    }

    .toggle-container {
        margin: 10px 0;
    }
}

@media screen and (max-width: 480px) {
    .container {
        padding: 15px;
    }
    /* Adjust padding for cards on very small screens */
    .card {
        width: 100%;
    }

    .content-section {
        padding: 20px;
        margin: 0 auto 30px;
    }

    .section-box {
        padding: 15px;
        margin-bottom: 20px;
    }

    h2 {
        font-size: 1.5em;
        margin-bottom: 20px;
    }

    h3 {
        font-size: 1.1em;
    }
}
'''

# ==============================================================================
# MASTER JAVASCRIPT CONTENT (All JS in one string for inline injection)
# This is the exact content from Step 2.
# ==============================================================================
MASTER_INLINE_JS = r'''
// --- MASTER INLINE JAVASCRIPT ---

document.addEventListener('DOMContentLoaded', () => {
    // Dark Mode Toggle Logic
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const themeKey = 'theme-preference';

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            if (darkModeToggle) darkModeToggle.checked = true;
        } else {
            body.classList.remove('dark-mode');
            if (darkModeToggle) darkModeToggle.checked = false;
        }
    };

    const savedTheme = localStorage.getItem(themeKey);
    if (savedTheme) {
        applyTheme(savedTheme);
    }

    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            const newTheme = darkModeToggle.checked ? 'dark' : 'light';
            applyTheme(newTheme);
            localStorage.setItem(themeKey, newTheme);
        });
    }

    // High-Yield / Full Script Toggle Logic (for content pages)
    // These functions need to be global or attached to window to be called from onclick attributes.
    window.toggleSwitch = function(switchEl) { // Make global
        const isActive = switchEl.classList.toggle('active');
        document.getElementById('highYieldLabel').classList.toggle('active', !isActive);
        document.getElementById('fullScriptLabel').classList.toggle('active', isActive);
        document.getElementById('highYield').classList.toggle('active', !isActive);
        document.getElementById('fullScript').classList.toggle('active', isActive);
    }

    window.showContent = function(id) { // Make global
        const highYieldContent = document.getElementById('highYield');
        const fullScriptContent = document.getElementById('fullScript');
        const highYieldLabel = document.getElementById('highYieldLabel');
        const fullScriptLabel = document.getElementById('fullScriptLabel');
        const switchEl = document.querySelector('.toggle-container .switch');

        if (id === 'highYield') {
            highYieldContent.classList.add('active');
            fullScriptContent.classList.remove('active');
            highYieldLabel.classList.add('active');
            fullScriptLabel.classList.remove('active');
            switchEl.classList.remove('active');
        } else { // id === 'fullScript'
            highYieldContent.classList.remove('active');
            fullScriptContent.classList.add('active');
            highYieldLabel.classList.remove('active');
            fullScriptLabel.classList.add('active');
            switchEl.classList.add('active');
        }
    }
});
'''

# ==============================================================================
# THEME MAPPING - This defines which theme class applies to which page.
# ==============================================================================
THEME_MAP = {
    # Blue for Diagnosis
    'diagnosis': 'theme-blue', 'atrial_fibrillation': 'theme-blue', 'bacterial_vaginosis': 'theme-blue',
    'chronic_kidney_disease': 'theme-blue', 'glaucoma': 'theme-blue', 'hypertension': 'theme-blue',
    'fibroadenoma': 'theme-blue', 'eczema': 'theme-blue', 'haemodialysis': 'theme-blue', 

    # Green for Medication
    'medication': 'theme-green', 'ace_inhibitor': 'theme-green', 'anticoagulant': 'theme-green',
    'direct_oral_anticoagulant': 'theme-green', 'gliclazide': 'theme-green', 'gtn_spray': 'theme-green',
    'iron_supplementation': 'theme-green', 'metformin': 'theme-green', 'opioid_analgesia': 'theme-green',
    'statin': 'theme-green', 'warfarin': 'theme-green',

    # Orange for Procedure
    'procedure': 'theme-orange', 'ascitic_drain': 'theme-orange', 'blood_transfusion': 'theme-orange',
    'colonoscopy': 'theme-orange', 'echocardiogram': 'theme-orange', 'endoscopy': 'theme-orange',
    'ercp': 'theme-orange',

    # Purple for Post-Procedure / Psychiatry-related Medication
    'post-procedure': 'theme-purple', 'post_stemi': 'theme-purple', 'post_stroke': 'theme-purple',
    'dnacpr': 'theme-purple', 'amitriptyline': 'theme-purple', 'ssri': 'theme-purple',

    # Red for Surgery
    'surgery': 'theme-red', 'appendicectomy': 'theme-red', 'cabg': 'theme-red', 'cholecystectomy': 'theme-red',
    'gastrectomy': 'theme-red',

    # Terracotta for Community
    'community': 'theme-terracotta', 'bowel_cancer_screening': 'theme-terracotta',
    'weight_loss': 'theme-terracotta', 'smoking_cessation': 'theme-terracotta', 'alcohol_cessation': 'theme-terracotta',

    # Teal for Respiratory
    'asthma': 'theme-teal', 'copd': 'theme-teal', 'inhaler': 'theme-teal', 'peak_flow': 'theme-teal',
    'bronchoscopy': 'theme-teal', 'chest_drain': 'theme-teal', 'tuberculosis_treatment': 'theme-teal',
    
    # Pink for Diabetes
    'diabetes': 'theme-pink', 'insulin': 'theme-pink', 'type1_diabetes': 'theme-pink', 'type2_diabetes': 'theme-pink',
}


def get_theme_class(file_path):
    file_name_lower = os.path.basename(file_path).lower()
    
    # Check for main station listing pages first (these usually determine the category's overall theme)
    if 'pretty_diagnosis_stations' in file_name_lower: return 'theme-blue'
    if 'pretty_medication_stations' in file_name_lower: return 'theme-green'
    if 'pretty_procedure_stations' in file_name_lower: return 'theme-orange'
    if 'pretty_post-procedure__stations' in file_name_lower: return 'theme-purple'
    if 'pretty_surgery_stations' in file_name_lower: return 'theme-red'
    if 'pretty_community_stations' in file_name_lower: return 'theme-terracotta'
        
    # Then check for content pages using the more detailed THEME_MAP
    for keyword, theme in THEME_MAP.items():
        if keyword in file_name_lower:
            return theme
    return None # Return None if no theme matches

def process_html_file(html_path):
    try:
        with open(html_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()

        original_content = content

        # --- 1. Aggressive Cleaning Phase ---
        # Delete any existing <style>...</style> block
        content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        # Delete any existing <link rel="stylesheet" ...> lines
        content = re.sub(r'<link\s+rel="stylesheet".*?>', '', content, flags=re.IGNORECASE)
        # Delete any existing <script>...</script> blocks
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
        # Delete any old toggle HTML (labels, old toggle-container, old toggle-wrapper)
        content = re.sub(r'<div\s+class="labels">.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<div\s+class="toggle-container".*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<div\s+class="toggle-wrapper">.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)
        # Remove any existing <main> tags if present, we'll re-wrap
        content = re.sub(r'<main>.*?</main>', '', content, flags=re.DOTALL | re.IGNORECASE)


        # --- 2. Inject Inline CSS ---
        # Insert the full CSS content into the <head>
        if '</head>' in content:
            content = content.replace('</head>', f'    <style>{MASTER_INLINE_CSS}</style>\n</head>', 1)
        else: # Fallback if no </head> tag
            content = content.replace('<body>', f'<head>\n    <style>{MASTER_INLINE_CSS}</style>\n</head>\n<body>', 1)

        # --- 3. Inject Inline JavaScript ---
        # Insert the full JS content just before the closing </body> tag
        if '</body>' in content:
            content = content.replace('</body>', f'    <script>{MASTER_INLINE_JS}</script>\n</body>', 1)
        else: # Fallback if no </body> tag
            content += f'\n<script>{MASTER_INLINE_JS}</script>\n'


        # --- 4. Apply Theme Class to Body Tag ---
        theme_class = get_theme_class(html_path)
        if theme_class:
            # Remove any existing theme classes from the body tag
            content = re.sub(r'(<body\s+class=")([^"]*?)(\b(theme-blue|theme-green|theme-orange|theme-purple|theme-red|theme-terracotta|theme-teal|theme-pink)\b[^"]*)(".*?>)', r'\1\2\5', content, flags=re.IGNORECASE)
            content = re.sub(r'<body\s+class=""(.*?)>', r'<body\1>', content, flags=re.IGNORECASE) # Clean up empty class attribute if only theme was removed

            # Add the new theme class
            if re.search(r'<body\s+class="', content, re.IGNORECASE):
                current_class_value = re.search(r'<body\s+class="([^"]*)"', content, re.IGNORECASE).group(1)
                if theme_class not in current_class_value: # Only add if not already present
                    content = re.sub(r'(<body\s+class=")([^"]*)(".*?>)', fr'\1\2 {theme_class}\3', content, 1, re.IGNORECASE)
            else:
                content = re.sub(r'<body', f'<body class="{theme_class}"', content, 1, re.IGNORECASE)

        # --- 5. Inject High-Yield/Full Script Toggle HTML (for content pages only) ---
        # Detect if the page is a content page with highYield/fullScript divs
        # AND ensure it's not the index.html (which doesn't need this toggle)
        if '<div id="highYield"' in content and '<div id="fullScript"' in content and 'index.html' not in os.path.basename(html_path).lower():
            toggle_wrapper_html = r'''
    <div class="toggle-wrapper">
      <span id="highYieldLabel" class="toggle-label active" onclick="showContent('highYield')">High-Yield Notes</span>
      <span id="fullScriptLabel" class="toggle-label" onclick="showContent('fullScript')">Full Script</span>
      <div class="toggle-container">
        <div class="switch" onclick="toggleSwitch(this)">
          <div class="slider"></div>
        </div>
      </div>
    </div>
'''
            # Insert the toggle-wrapper right after the <header> tag or <body> if no header
            if '<header>' in content:
                content = re.sub(r'(<header.*?>.*?</header>)', fr'\1\n{toggle_wrapper_html}', content, 1, re.DOTALL | re.IGNORECASE)
            elif '<body>' in content:
                content = content.replace('<body>', f'<body>\n{toggle_wrapper_html}', 1)

            # Ensure 'active' class is on 'highYield' initially and removed from 'fullScript'
            content = re.sub(r'(<div\s+id="highYield"\s+class="content-section[^>]*?)(\sactive)?(")', r'\1 active\3', content, 1)
            content = re.sub(r'(<div\s+id="fullScript"\s+class="content-section[^>]*?)(\sactive)?(")', r'\1\3', content, 1)

        # --- 6. Wrap Main Content in <main> tag (Good Practice) ---
        # This will wrap the main content area (from header/toggle down to footer/scripts) in a <main> tag.
        if '<body>' in content: # Only process if a body tag exists
            # Define common starting and ending markers for content to wrap
            start_markers_regex = r'(<header.*?>.*?</header>|<div class="toggle-wrapper">.*?</div>|<div class="container">.*?</div>|<body[^>]*>)'
            end_markers_regex = r'(<footer>.*?</footer>|<script.*?>.*?</script>|</body>)'
            
            start_match = re.search(start_markers_regex, content, re.DOTALL | re.IGNORECASE)
            end_match = re.search(end_markers_regex, content, re.DOTALL | re.IGNORECASE)

            # Only wrap if content exists between markers and not already wrapped
            if start_match and end_match and '<main>' not in content[start_match.end():end_match.start()]:
                # Extract the content to wrap
                content_to_wrap = content[start_match.end():end_match.start()]
                
                # Exclude header/toggle/container from content_to_wrap if they were included as start_match
                # This logic is complex with regex; safer to use a more defined content area.
                # For simplicity, we'll wrap content between BODY and FOOTER/SCRIPT, or after HEADER/TOGGLE to FOOTER/SCRIPT.
                # Let's adjust to be very robust: wrap everything *between* the body and closing body/script/footer.

                # Find the actual content area after possible header/toggle-wrapper for pages that have them
                actual_content_start_index = start_match.end() if '<div class="toggle-wrapper">' in content or '<header>' in content else content.find('<body>') + len('<body>')
                actual_content_end_index = end_match.start()

                if actual_content_start_index < actual_content_end_index:
                    content_before_main = content[:actual_content_start_index]
                    content_after_main = content[actual_content_end_index:]
                    content_main_body = content[actual_content_start_index:actual_content_end_index]

                    if content_main_body.strip(): # Only wrap if there's actual content
                        # Remove existing main tags if they somehow got there for clean re-wrap
                        content_main_body = re.sub(r'<main>', '', content_main_body, flags=re.IGNORECASE)
                        content_main_body = re.sub(r'</main>', '', content_main_body, flags=re.IGNORECASE)

                        wrapped_content = f'\n<main>{content_main_body}</main>\n'
                        content = content_before_main + wrapped_content + content_after_main
            elif '<body>' in content and '<main>' not in content: # Simple fallback for very minimal pages
                content = content.replace('<body>', '<body>\n<main>\n', 1)
                content = content.replace('</body>', '\n</main>\n</body>', 1)


        # --- Write back if content changed ---
        if content != original_content:
            with open(html_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Processed and updated: {os.path.basename(html_path)} | Theme: {theme_class or 'None'}")
        else:
            print(f"Skipped (no changes needed): {os.path.basename(html_path)}")

    except Exception as e:
        print(f"Error processing {html_path}: {e}")

def main():
    root_directory = os.path.dirname(os.path.abspath(__file__))
    
    print("--- Starting Full HTML Automation ---")
    
    # Iterate through all HTML files
    for subdir, _, files in os.walk(root_directory):
        # Exclude .git and __pycache__ directories
        if '.git' in subdir or '__pycache__' in subdir:
            continue
        for file_name in files:
            if file_name.endswith('.html'):
                html_file_path = os.path.join(subdir, file_name)
                process_html_file(html_file_path)
                
    print("\n--- Automation Complete! ---")
    print("All HTML files have been processed with inline CSS and JS.")
    print("Please check your pages directly in the browser.")


if __name__ == '__main__':
    main()