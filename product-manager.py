import streamlit as st
import os

# ================= Feature =================
class Feature:
    __feature_id_counter = 1

    def __init__(self, name, priority, status, expected_users):
        self.feature_id = Feature.__feature_id_counter
        Feature.__feature_id_counter += 1
        self.name = name
        self.priority = priority
        self.status = status
        self.expected_users = expected_users

# ================= Manager =================
class AdvancedProductManager:
    def __init__(self):
        self.features_list = []

    def add_feature(self, name, priority, status, users):
        self.features_list.append(
            Feature(name, priority, status, users)
        )

    def update_feature(self, fid, status):
        for f in self.features_list:
            if f.feature_id == fid:
                f.status = status
                return True
        return False

    def analyze_priorities(self):
        return {
            "عالية": len([f for f in self.features_list if f.priority == "عالية"]),
            "متوسطة": len([f for f in self.features_list if f.priority == "متوسطة"]),
            "منخفضة": len([f for f in self.features_list if f.priority == "منخفضة"]),
        }

    def save(self):
        with open("features.txt", "w", encoding="utf-8") as f:
            for fe in self.features_list:
                f.write(f"{fe.name},{fe.priority},{fe.status},{fe.expected_users}\n")

# ================= Streamlit UI =================
st.title("📦 Digital Product Manager")

if "manager" not in st.session_state:
    st.session_state.manager = AdvancedProductManager()

menu = st.sidebar.selectbox(
    "القائمة",
    ["إضافة ميزة", "عرض الميزات", "تحليل الأولويات", "حفظ في ملف"]
)

manager = st.session_state.manager

# ➕ Add Feature
if menu == "إضافة ميزة":
    name = st.text_input("اسم الميزة")
    priority = st.selectbox("الأولوية", ["عالية", "متوسطة", "منخفضة"])
    status = st.selectbox("الحالة", ["مخطط لها", "جاري العمل", "مكتملة"])
    users = st.number_input("المستخدمون المتوقعون", min_value=0)

    if st.button("إضافة"):
        manager.add_feature(name, priority, status, users)
        st.success("تمت إضافة الميزة")

# 📋 Display
elif menu == "عرض الميزات":
    for f in manager.features_list:
        st.write(
            f"ID:{f.feature_id} | {f.name} | {f.priority} | {f.status} | {f.expected_users}"
        )

# 📊 Analysis
elif menu == "تحليل الأولويات":
    data = manager.analyze_priorities()
    st.bar_chart(data)

# 💾 Save
elif menu == "حفظ في ملف":
    manager.save()
    st.success("تم حفظ البيانات")
