# 2.Sorunun çözümü
while True:
    mail = input("Email adresinizi giriniz: ")
    et_ayrı = mail.split("@")
    
    if " " in mail:
        print("Mailiniz geçerli değildir.")
        continue
    if mail.count("@") != 1:
        print("Mailiniz geçerli değildir.")
        continue
    if mail.startswith("@") == 1:
        print("Mailiniz geçerli değildir.")
        continue
    if et_ayrı[1].count("..") == 1 or et_ayrı[1].count(".") > 2 or et_ayrı[1].count(".") == 0:
        print("Mailiniz geçerli değildir.")
        continue
    if et_ayrı[1].count(".") == 2 and et_ayrı[1].count(".tr") != 1:
        print("Mailiniz geçerli değildir.")
        continue
    if et_ayrı[1].endswith(".com") != 1 and et_ayrı[1].endswith(".com.tr") != 1 and et_ayrı[1].endswith(".edu.tr") != 1:
        print("Mailiniz geçerli değildir.")
        continue
    if et_ayrı[1].endswith(".com") == 1 or et_ayrı[1].endswith(".com.tr") == 1 or et_ayrı[1].endswith(".edu.tr") == 1:
        print("Mailiniz geçerlidir.")
        break
   

