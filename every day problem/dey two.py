# Smart Email Slicer & Formatter 
# * اسم الريبو: py-02-email-slicer
# * وصف التاسك: أداة تستقبل البريد الإلكتروني من المستخدم، وتقوم باستخراج اسم المستخدم (Username) والنطاق (Domain) والدومين الرئيسي (TLD)، مع فحص صحة الإدخال الأساسية.
# * شكل النتيجة النهائية: 
# Enter your email: dev.mostafa@gmail.com

# [+] Username : dev.mostafa
# [+] Domain   : gmail
# [+] TLD      : com

# * إضافات بونص: 
# 1. التأكد إن الإيميل يحتوي على @ و . باستخدام Membership Operators قبل التقطيع.
# 2. طباعة رسالة تشفير جزئي للإيميل مثل: d***a@gmail.com.


email = input("Please Enter Your E-mail ^.^")
if "@" in email :
    if "." in email :                
        print(email[0:email.index("@")])
        print(email[email.index("@")+1:email.rindex(".")])
        print(email[email.rindex(".")+1:])
        print(email[0] + "*" * len((email[1:email.index("@")-1])) + email[email.index("@")-1])
else :
     print("Invalid E-Mail -_- Please Enter A Valid Mail ... ")






# طباعة رسالة التشفير 