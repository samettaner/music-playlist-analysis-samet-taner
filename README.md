# music-playlist-analysis-samet-taner

Proje amacı : Music Playlist Analizi sistemi

method acıklamaları : 

                    get_total_duration
        Bu method, şarkı listesindeki tüm şarkıların sürelerini toplar.
        Parametre olarak şarkı listesini alır (songs).
        Her şarkının "sure" değeri toplanarak toplam süre hesaplanır.
        Sonuç olarak toplam süre (int) geri döndürülür.

                    get_most_played_song           
         Bu method, en çok dinlenen şarkıyı bulur.
         Parametre olarak şarkı listesini alır (songs).
         Listedeki şarkılar "dinlenme" değerlerine göre karşılaştırılır.
         En yüksek dinlenme sayısına sahip şarkı bulunur.
         Sonuç olarak o şarkının sözlüğü (dictionary) geri döndürülür.

                    get_average_duration
           Bu method, şarkıların ortalama süresini hesaplar.
           Parametre olarak şarkı listesini alır (songs).
           Önce toplam süre get_total_duration methodu ile bulunur.
           Daha sonra toplam süre, şarkı sayısına bölünür.
           Sonuç olarak ortalama süre (float) geri döndürülür.

                    print_playlist
           Bu method, şarkı listesini düzenli bir şekilde ekrana yazdırır.
           Parametre olarak şarkı listesini alır (songs).
           Her şarkının adı, sanatçısı, süresi ve dinlenme sayısı gösterilir.
           Kullanıcıya okunabilir bir çıktı sunar.

                     main
           Bu method programın ana çalışma noktasıdır.
           Şarkı listesi burada oluşturulur (liste + sözlük yapısı).
           Diğer tüm methodlar burada çağrılır.
           Programın tüm işlemleri buradan başlatılır ve yönetilir.

calistirma bilgisi : Program Python dili ile yazılmıştır ve komut satırından çalıştırılmaktadır.57 komutsatırındakı songs(sarkılar) lıstelerine isterseniz yeni isterseniz zaten bulunan şarkıları degıstırebilirsiniz
