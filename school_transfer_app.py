import streamlit as st
import pandas as pd
import os

# عنوان التطبيق
st.title("نظام إدارة مسارات الطلبة")

# تحديد اسم المسار أو الملف
file_name = "تنسيق الزيارات1.xlsx"

# التحقق من وجود الملف في مجلد المشروع
if os.path.exists(file_name):
    try:
        # قراءة ملف الإكسل مباشرة
        df = pd.read_excel(file_name)
        
        st.success(f"تم تحميل الملف '{file_name}' بنجاح!")
        
        # عرض البيانات أو جزء منها للتأكد
        st.subheader("بيانات الطلبة / الزيارات:")
        st.dataframe(df)
        
        # --- ضع هنا باقي كود المعالجة الخاص بك ---
        # مثال: عرض عدد الصفوف
        st.write(AnimateText := f"إجمالي عدد السجلات: {len(df)}")
        
    except Exception as e:
        st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
else:
    st.error(f"عذراً، لم يتم العثور على الملف '{file_name}' في مجلد المشروع.")
    st.info("يرجى التأكد من وضع ملف الإكسل في نفس المجلد الذي يحتوي على ملف كود البايثون.")