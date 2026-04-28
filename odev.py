# ============================================
# ŞARKI PLAYLIST ANALİZ SİSTEMİ
# ============================================

# 1. TÜM ŞARKILARIN TOPLAM SÜRESİNİ HESAPLAR
def get_total_duration(songs):
    toplam = 0  # başlangıçta toplam süre 0

    # listedeki her şarkıyı tek tek geziyoruz
    for sarki in songs:
        toplam += sarki["sure"]
        # her şarkının "sure" değerini toplama ekliyoruz

    return toplam  # sonucu geri döndürüyoruz

# 2. EN ÇOK DİNLENEN ŞARKIYI BULUR
def get_most_played_song(songs):
    en_cok = songs[0]
    # karşılaştırmaya başlamak için ilk şarkıyı baz alıyoruz

    # listedeki tüm şarkıları geziyoruz
    for sarki in songs:
        # eğer mevcut şarkının dinlenmesi daha fazlaysa
        if sarki["dinlenme"] > en_cok["dinlenme"]:
            en_cok = sarki
            # en çok dinlenen şarkıyı güncelliyoruz

    return en_cok  # en çok dinlenen şarkıyı geri döndür

# 3. ORTALAMA ŞARKI SÜRESİNİ HESAPLAR
def get_average_duration(songs):
    # önce toplam süreyi hazır method ile alıyoruz
    toplam = get_total_duration(songs)

    # ortalama = toplam süre / şarkı sayısı
    ortalama = toplam / len(songs)
    return ortalama

# 4. PLAYLISTİ DÜZENLİ ŞEKİLDE YAZDIRIR
def print_playlist(songs):
    print("\n========== PLAYLIST ==========")

    # listedeki her şarkıyı tek tek yazdırıyoruz
    for sarki in songs:
        print("Şarkı Adı   :", sarki["ad"])
        print("Sanatçı     :", sarki["sanatci"])
        print("Süre (sn)   :", sarki["sure"])
        print("Dinlenme    :", sarki["dinlenme"])
        print("-----------------------------")

# 5. ANA FONKSİYON (PROGRAMIN ÇALIŞTIĞI YER)
def main():

    # Şarkı listesi oluşturuluyor
    # Her şarkı bir sözlük (dictionary)
    # Tüm şarkılar ise bir liste içinde tutuluyor
    songs = [
        {"ad": "Şarkı1", "sanatci": "Sanatçı1", "sure": 200, "dinlenme": 1500},
        {"ad": "Şarkı2", "sanatci": "Sanatçı2", "sure": 240, "dinlenme": 2000},
        {"ad": "Şarkı3", "sanatci": "Sanatçı3", "sure": 210, "dinlenme": 1700},
        {"ad": "Şarkı4", "sanatci": "Sanatçı4", "sure": 190, "dinlenme": 1200},
        {"ad": "Şarkı5", "sanatci": "Samet", "sure": 180, "dinlenme": 2200}
    ]

    # --- FONKSİYON ÇAĞRILARI ---

    # playlisti ekrana yazdır
    print_playlist(songs)

    # toplam süreyi hesapla ve yazdır
    toplam = get_total_duration(songs)
    print("\nToplam Süre:", toplam, "sn")

    # ortalama süreyi hesapla ve yazdır
    ortalama = get_average_duration(songs)
    print("Ortalama Süre:", ortalama, "sn")

    # en çok dinlenen şarkıyı bul ve yazdır
    en_cok = get_most_played_song(songs)
    print("\nEn Çok Dinlenen Şarkı:")
    print(en_cok["ad"], "-", en_cok["sanatci"], "-", en_cok["dinlenme"], "dinlenme")

# PROGRAMIN BAŞLANGIÇ NOKTASI
# Bu satır sayesinde dosya direkt çalıştırıldığında main() fonksiyonu çalışır
if __name__ == "__main__":
    main()

    