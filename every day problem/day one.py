# # * وصف التاسك: برنامج تفاعلي يطلب من المستخدم بياناته الأساسية (الاسم، سنة الميلاد، المهنة، المهارات مفصولة بفواصل) ويقوم بطباعة "بطاقة تعريفية" بطريقة منظمة باستخدام Escape Characters و String Formatting، مع حساب العمر الحالي.
# * شكل النتيجة النهائية: 
# ========================================
#            USER PROFILE CARD
# ========================================
# Name       : Mostafa Naeem
# Age        : 23 Years Old
# Job        : Developer
# Skills     : Python | JS | Angular
# ========================================

# * إضافات بونص: 
# 1. تنظيف اسم المستخدم (إزالة المسافات الزائدة وتحويله لـ Capitalize).
# 2. تحويل سلسلة المهارات إلى List ثم إعادة تجميعها بشكل منظم باستعمال .join().






name = input ("Hello What 's Your Name ? ^.^ ").capitalize()

age = int(input ("How Old Are You ? ^.^ "))

job = input ("What 's Your Job ? °¥° ")

skills = input ("Please Mention Your Skills (: ... ").split()
askills = " | ".join(skills)

print ("=" * 40)
print (f"{name} Profile Card".center(40))
print ("=" * 40)

print (f"Name       : {name}")
print (f"Age        : {age} Years Old")
print (f"Job        : {job}")
print (f"Skills     : {askills}")


