import streamlit as st
from datetime import datetime, timezone
import string

from utils.json_tools import format_json, validate_json


# =========================================================
# العنوان
# =========================================================

st.title("🔧 أدوات المطورين")

st.write("أدوات مفيدة للمبرمجين 👨‍💻")


# =========================================================
# 1️⃣ أدوات JSON
# =========================================================

st.header("📋 أدوات JSON")

json_text = st.text_area(
    "ضع JSON هنا:",
    height=250,
    placeholder='{"name": "Ahmed", "age": 14}'
)

col1, col2 = st.columns(2)

with col1:
    if st.button("✅ فحص JSON", use_container_width=True):
        if validate_json(json_text):
            st.success("JSON صحيح ✅")
        else:
            st.error("JSON غير صحيح ❌")

with col2:
    if st.button("✨ تنسيق JSON", use_container_width=True):
        try:
            formatted = format_json(json_text)
            st.code(formatted, language="json")

        except ValueError:
            st.error("الـ JSON غير صحيح ❌")


st.divider()


# =========================================================
# 2️⃣ ⏱️ محوّل التوقيت
# =========================================================

st.header("⏱️ محوّل التوقيت")

mode = st.radio(
    "اختر العملية:",
    [
        "توقيت Unix → تاريخ",
        "تاريخ → توقيت Unix"
    ],
    horizontal=True
)


if mode == "توقيت Unix → تاريخ":

    timestamp = st.number_input(
        "أدخل توقيت Unix:",
        value=int(datetime.now(timezone.utc).timestamp()),
        step=1
    )

    if st.button(
        "🔄 تحويل إلى تاريخ",
        use_container_width=True
    ):

        try:

            result = datetime.fromtimestamp(
                timestamp,
                tz=timezone.utc
            )

            st.success(
                f"التاريخ والوقت UTC:\n\n{result.isoformat()}"
            )

        except Exception:

            st.error("توقيت Unix غير صحيح ❌")


else:

    selected_date = st.date_input(
        "اختر التاريخ:"
    )

    if st.button(
        "🔄 تحويل إلى Unix",
        use_container_width=True
    ):

        result = datetime.combine(
            selected_date,
            datetime.min.time(),
            tzinfo=timezone.utc
        )

        st.success(
            f"توقيت Unix:\n\n{int(result.timestamp())}"
        )


st.divider()


# =========================================================
# 3️⃣ 🎨 محوّل الألوان
# =========================================================

st.header("🎨 محوّل الألوان")

hex_color = st.text_input(
    "أدخل لون HEX:",
    "#6366F1",
    placeholder="#FF0000"
)


if st.button(
    "🎨 تحويل اللون",
    use_container_width=True
):

    value = hex_color.strip().lstrip("#")

    if len(value) == 6 and all(
        char in string.hexdigits
        for char in value
    ):

        r = int(value[0:2], 16)
        g = int(value[2:4], 16)
        b = int(value[4:6], 16)

        st.success("تم تحويل اللون بنجاح ✅")

        col1, col2 = st.columns(2)

        with col1:

            st.write("### RGB")

            st.code(
                f"rgb({r}, {g}, {b})"
            )

        with col2:

            st.write("### القيم")

            st.code(
                f"R = {r}\n"
                f"G = {g}\n"
                f"B = {b}"
            )

        st.color_picker(
            "👁️ معاينة اللون",
            f"#{value}",
            disabled=True
        )

    else:

        st.error(
            "❌ كود HEX غير صحيح.\n\n"
            "مثال صحيح: #6366F1"
        )


st.divider()


# =========================================================
# 4️⃣ 🔢 محوّل أنظمة الأرقام
# =========================================================

st.header("🔢 محوّل أنظمة الأرقام")

number = st.text_input(
    "أدخل الرقم:",
    placeholder="مثال: 255"
)


number_base = st.selectbox(
    "النظام الحالي:",
    [2, 8, 10, 16],

    format_func=lambda base: {

        2: "🔵 ثنائي (Binary)",

        8: "🟢 ثماني (Octal)",

        10: "🟡 عشري (Decimal)",

        16: "🟣 سداسي عشر (Hexadecimal)"

    }[base]
)


if st.button(
    "🔄 تحويل الرقم",
    use_container_width=True
):

    if not number.strip():

        st.warning("⚠️ أدخل رقمًا أولًا.")

    else:

        try:

            value = int(
                number.strip(),
                number_base
            )

            st.success(
                "تم التحويل بنجاح ✅"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("### الأنظمة")

                st.write(
                    f"🔵 **ثنائي:** `{bin(value)[2:]}`"
                )

                st.write(
                    f"🟢 **ثماني:** `{oct(value)[2:]}`"
                )

            with col2:

                st.write("### الأنظمة")

                st.write(
                    f"🟡 **عشري:** `{value}`"
                )

                st.write(
                    f"🟣 **سداسي عشر:** "
                    f"`{hex(value)[2:].upper()}`"
                )

        except ValueError:

            st.error(
                "❌ الرقم لا يتوافق مع النظام المختار."
            )