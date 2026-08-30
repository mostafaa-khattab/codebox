import streamlit as st


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="CodeBox",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# CSS
# ==================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        opacity: 0.75;
        margin-bottom: 35px;
    }

    .welcome-box {
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 25px;
    }

    .tool-card {
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 20px;
        min-height: 155px;
    }

    .tool-title {
        font-size: 25px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .tool-description {
        font-size: 16px;
        opacity: 0.75;
    }

    .section-title {
        font-size: 30px;
        font-weight: 750;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">💻 CodeBox</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">'
    'مجموعة أدوات ذكية للمبرمجين والمستخدمين في مكان واحد 🚀'
    '</div>',
    unsafe_allow_html=True,
)

st.divider()


# ==================================================
# WELCOME
# ==================================================

st.markdown(
    '<div class="section-title">👋 أهلاً بك في CodeBox</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="welcome-box">

    <h3>🚀 CodeBox</h3>

    <p>
    CodeBox عبارة عن مجموعة أدوات مفيدة للمبرمجين
    والمستخدمين في مكان واحد.
    </p>

    <p>
    يمكنك استخدام أدوات البرمجة، الذكاء الاصطناعي،
    الألوان، النصوص والمزيد.
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# TOOLS
# ==================================================

st.markdown(
    '<div class="section-title">🛠️ الأدوات</div>',
    unsafe_allow_html=True,
)


# ==================================================
# ROW 1
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# Calculator
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🧮 Calculator
        </div>

        <div class="tool-description">
        حاسبة للعمليات الحسابية الأساسية.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Calculator",
        key="open_calculator",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/calculator.py"
        )


# --------------------------------------------------
# Password Generator
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🔐 Password Generator
        </div>

        <div class="tool-description">
        إنشاء كلمات مرور عشوائية وقوية.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Password Generator",
        key="open_password",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/password_generator.py"
        )


# ==================================================
# ROW 2
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# Converter
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🔄 Converter
        </div>

        <div class="tool-description">
        تحويل بين الوحدات والقيم المختلفة.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Converter",
        key="open_converter",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/converter.py"
        )


# --------------------------------------------------
# Developer Tools
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🔧 Developer Tools
        </div>

        <div class="tool-description">
        أدوات للمطورين مثل JSON Formatter.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Developer Tools",
        key="open_developer_tools",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/developer_tools.py"
        )


# ==================================================
# ROW 3
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# Color Mixer
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🎨 Color Mixer
        </div>

        <div class="tool-description">
        ادمج لونين واحصل على اللون الناتج
        مع HEX و RGB.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Color Mixer",
        key="open_color_mixer",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/color_mixer.py"
        )


# --------------------------------------------------
# Home Color Advisor
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🏠 Home Color Advisor
        </div>

        <div class="tool-description">
        اختر ألوانًا مناسبة للبيت والديكور.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Home Color Advisor",
        key="open_home_color",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/home_color_advisor.py"
        )


# ==================================================
# ROW 4
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# AI Code Generator
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🤖 AI Code Studio
        </div>

        <div class="tool-description">
        إنشاء الكود وشرحه وتحسينه واكتشاف الأخطاء
        باستخدام الذكاء الاصطناعي.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح AI Code Studio",
        key="open_ai_code",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/ai_code_generator.py"
        )


# --------------------------------------------------
# Personal Assistant
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🤖 Personal Assistant
        </div>

        <div class="tool-description">
        مساعد شخصي ذكي للكتابة والتحدث والإجابة
        على الأسئلة.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Personal Assistant",
        key="open_assistant",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/personal_assistant.py"
        )


# ==================================================
# ROW 5
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# Text Analyzer
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        📝 Text Analyzer
        </div>

        <div class="tool-description">
        تحليل النصوص وحساب الكلمات والحروف
        والأسطر والأرقام.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Text Analyzer",
        key="open_text_analyzer",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/text_analyzer.py"
        )


# ==================================================
# ROW 6
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# Base64 Tool
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🔤 Base64 Tool
        </div>

        <div class="tool-description">
        تشفير وفك ترميز النصوص باستخدام Base64.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Base64 Tool",
        key="open_base64",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/base64_tool.py"
        )


# --------------------------------------------------
# Hash Generator
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🔐 Hash Generator
        </div>

        <div class="tool-description">
        إنشاء Hash باستخدام SHA-256 و SHA-512
        وغيرها.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Hash Generator",
        key="open_hash",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/hash_generator.py"
        )


# ==================================================
# ROW 7
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# URL Encoder
# --------------------------------------------------

with col1:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🌐 URL Encoder
        </div>

        <div class="tool-description">
        ترميز وفك ترميز الروابط والنصوص.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح URL Encoder",
        key="open_url_encoder",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/url_encoder.py"
        )


# --------------------------------------------------
# Timestamp Converter
# --------------------------------------------------

with col2:

    st.markdown(
        """
        <div class="tool-card">

        <div class="tool-title">
        🕒 Timestamp Converter
        </div>

        <div class="tool-description">
        تحويل Unix Timestamp إلى تاريخ والعكس.
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "فتح Timestamp Converter",
        key="open_timestamp",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/timestamp_converter.py"
        )


# ==================================================
# QUICK ACCESS
# ==================================================

st.divider()

st.markdown(
    '<div class="section-title">⚡ وصول سريع</div>',
    unsafe_allow_html=True,
)


q1, q2, q3 = st.columns(3)


with q1:

    if st.button(
        "🎨 Colors",
        key="quick_colors",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/color_mixer.py"
        )


with q2:

    if st.button(
        "🤖 AI Code",
        key="quick_ai",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/ai_code_generator.py"
        )


with q3:

    if st.button(
        "🤖 Assistant",
        key="quick_assistant",
        use_container_width=True,
    ):

        st.switch_page(
            "pages/personal_assistant.py"
        )


# ==================================================
# FEATURES
# ==================================================

st.divider()

st.markdown(
    '<div class="section-title">✨ مميزات CodeBox</div>',
    unsafe_allow_html=True,
)


f1, f2, f3 = st.columns(3)


with f1:

    st.info(
        """
        🤖 **AI Tools**

        مساعد شخصي وAI Code Studio
        لمساعدتك في البرمجة.
        """
    )


with f2:

    st.info(
        """
        🛠️ **Developer Tools**

        JSON وHash وBase64
        وأدوات أخرى للمطورين.
        """
    )


with f3:

    st.info(
        """
        🎨 **Creative Tools**

        Color Mixer وأدوات الألوان
        والديكور.
        """
    )


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "🚀 CodeBox — Built with Python & Streamlit"
)