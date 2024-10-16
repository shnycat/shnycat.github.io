+++
title = 'Rangkuman Limit'
date = 2024-10-16T12:50:07Z
+++
**Limit** adalah konsep dalam matematika yang menggambarkan nilai yang didekati oleh suatu fungsi atau urutan saat variabel mendekati titik tertentu. Meski fungsi atau nilai tidak pernah benar-benar mencapai titik itu, limit membantu kita memahami apa yang terjadi “saat mendekati” titik tersebut.

### Rangkuman Konsep Limit:

1. **Limit dari Fungsi**: 
   Limit mengukur apa yang terjadi pada nilai suatu fungsi saat variabelnya mendekati angka tertentu.
   - Jika $ f(x) $ adalah fungsi, maka limit $ x \to a $ dari $ f(x) $ (ditulis $ \lim_{x \to a} f(x) $) adalah nilai yang mendekati fungsi $ f(x) $ saat $ x $ mendekati $ a $.

2. **Limit dari Kiri dan Kanan**:
   - **Limit kiri**: Limit saat variabel mendekati dari sisi kiri (ditulis $ \lim_{x \to a^-} f(x) $).
   - **Limit kanan**: Limit saat variabel mendekati dari sisi kanan (ditulis $ \lim_{x \to a^+} f(x) $).
   Jika kedua limit ini sama, maka limit fungsi di titik itu ada.

3. **Limit Tak Hingga**:
   Limit bisa menuju ke tak hingga (∞) ketika nilai fungsi menjadi sangat besar atau sangat kecil saat variabel mendekati nilai tertentu.

### Contoh Mudah:

1. **Contoh 1** (Limit Sederhana):
   Misalkan $ f(x) = 2x + 1 $. Mari kita cari $ \lim_{x \to 3} f(x) $.

   Saat $ x $ mendekati 3, $ f(x) = 2(3) + 1 = 7 $. Jadi, $ \lim_{x \to 3} (2x + 1) = 7 $.

2. **Contoh 2** (Fungsi Tidak Terdefinisi di Titik Itu):
   Pertimbangkan $ f(x) = \frac{x^2 - 1}{x - 1} $. Pada $ x = 1 $, fungsi ini tidak terdefinisi karena hasilnya nol dibagi nol. Namun, kita bisa mencari limit $ \lim_{x \to 1} f(x) $.

   Sederhanakan fungsi:
   $$
   f(x) = \frac{(x - 1)(x + 1)}{x - 1} = x + 1 \quad (\text{untuk } x \neq 1)
   $$
   Jadi, $ \lim_{x \to 1} f(x) = 1 + 1 = 2 $.

### Intinya:
- Limit membantu kita mengetahui *nilai mendekati* ketika fungsi tidak terdefinisi di suatu titik, atau saat ingin memahami bagaimana fungsi berperilaku saat variabel mendekati suatu nilai.
- Contoh nyata: Jika kamu ingin tahu kecepatanmu tepat *sebelum* mobil berhenti (tapi tidak di saat berhenti), limit adalah alat yang digunakan untuk menghitungnya.
