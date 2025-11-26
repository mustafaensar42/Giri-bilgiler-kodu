# 1. Kullanıcı Girişi
while True:
    kullanici_ismi = input('Kullanıcı ismi giriniz: ')
    kullanici_soyisim = input('Soy ismi giriniz: ')
    kullanici_sifre = input('Şifre giriniz: ')

    if kullanici_ismi == 'mustafa' and kullanici_soyisim == 'kayadibi' and kullanici_sifre == '123':
        print('Giriş başarılı! Lütfen 2. Kullanıcıya geçiniz\n')
        break
    else:
        print('Bilgiler yanlış veya eksik. Tekrar deneyiniz.\n')


# 2. Kullanıcı Girişi
while True:
    kullanici2_isim = input('2. kullanıcının ismini giriniz: ')
    kullanici2_soyisim = input('2. kullanıcının soy ismini giriniz: ')
    kullanici2_sifre = input('2. kullanıcının şifresini giriniz: ')

    if kullanici2_isim == 'ahmet' and kullanici2_soyisim == 'demir' and kullanici2_sifre == '321':
        print('2. kullanıcının girişi başarılı! Giriş yapılıyor...\n')
        break
    else:
        print('Giriş başarısız! Lütfen bilgileri tekrar giriniz.\n')
