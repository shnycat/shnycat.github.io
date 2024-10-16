+++
title = 'Limit Soal Cerita'
date = 2024-10-16T13:10:00Z
+++
Berikut adalah 5 soal cerita tentang limit beserta jawabannya:

### 1. **Soal: Kecepatan Perjalanan**
Sebuah mobil bergerak dari kota A ke kota B dengan kecepatan yang semakin bertambah secara linear dari 40 km/jam hingga 80 km/jam dalam waktu 2 jam. Berapakah limit kecepatan rata-rata mobil saat mobil mendekati titik 2 jam?

**Jawaban**:
Kecepatan rata-rata dihitung sebagai perubahan jarak dibagi dengan perubahan waktu. Secara matematis, jika kecepatan bertambah linear dari 40 km/jam ke 80 km/jam selama 2 jam, maka kita dapat menggunakan rumus limit untuk menghitung kecepatan rata-rata saat mendekati 2 jam:

$$
\text{Kecepatan rata-rata} = \lim_{t \to 2} \frac{s(t)}{t}
$$

Di mana $ s(t) $ adalah jarak yang ditempuh pada waktu $ t $. Namun, karena kecepatan bertambah secara linear, kecepatan rata-rata saat $ t \to 2 $ mendekati 80 km/jam.

### 2. **Soal: Pertumbuhan Populasi**
Populasi sebuah kota diperkirakan bertambah setiap tahun menurut fungsi $ P(t) = 1000e^{0,05t} $, dengan $ P(t) $ adalah jumlah populasi dalam ribuan setelah $ t $ tahun. Berapakah populasi kota tersebut saat $ t \to \infty $?

**Jawaban**:
Kita menghitung limit fungsi populasi saat $ t \to \infty $:

$$
\lim_{t \to \infty} P(t) = \lim_{t \to \infty} 1000e^{0,05t} = \infty
$$

Karena eksponensial $ e^{0,05t} $ akan terus bertambah tanpa batas, maka populasi kota akan tumbuh tanpa batas seiring waktu.

### 3. **Soal: Pengurangan Suhu**
Suhu air panas menurun secara eksponensial sesuai rumus $ T(t) = 100e^{-0,1t} + 20 $, dengan $ T(t) $ adalah suhu dalam derajat Celcius pada waktu $ t $ menit. Berapakah suhu air setelah waktu yang sangat lama (ketika $ t \to \infty $)?

**Jawaban**:
Kita mencari limit suhu air saat $ t \to \infty $:

$$
\lim_{t \to \infty} T(t) = \lim_{t \to \infty} \left( 100e^{-0,1t} + 20 \right) = 20
$$

Saat $ t \to \infty $, eksponensial $ e^{-0,1t} \to 0 $, sehingga suhu air mendekati 20°C.

### 4. **Soal: Produksi Pabrik**
Sebuah pabrik menghasilkan barang dengan biaya produksi rata-rata per barang $ C(x) = \frac{500 + 200x}{x} $, di mana $ x $ adalah jumlah barang yang diproduksi. Berapakah biaya produksi rata-rata ketika jumlah barang yang diproduksi sangat besar ($ x \to \infty $)?

**Jawaban**:
Kita menghitung limit biaya produksi rata-rata saat $ x \to \infty $:

$$
\lim_{x \to \infty} C(x) = \lim_{x \to \infty} \frac{500 + 200x}{x} = \lim_{x \to \infty} \left( \frac{500}{x} + 200 \right) = 200
$$

Jadi, biaya produksi rata-rata akan mendekati 200 satuan uang per barang saat jumlah barang yang diproduksi sangat besar.

### 5. **Soal: Tinggi Bola yang Dipantulkan**
Sebuah bola dilempar ke atas dengan kecepatan awal, dan setiap kali bola memantul, tingginya berkurang sebesar 60% dari tinggi sebelumnya. Jika tinggi awal bola adalah 10 meter, berapakah tinggi bola setelah sangat banyak pantulan (ketika jumlah pantulan mendekati tak hingga)?

**Jawaban**:
Tinggi bola setelah $ n $ pantulan dinyatakan sebagai deret geometri:

$$
h_n = 10 \times (0,6)^n
$$

Kita menghitung limit tinggi bola saat jumlah pantulan $ n \to \infty $:

$$
\lim_{n \to \infty} h_n = \lim_{n \to \infty} 10 \times (0,6)^n = 0
$$

Jadi, setelah jumlah pantulan yang sangat banyak, tinggi bola akan mendekati 0 meter.

Jika ada yang ingin dijelaskan lebih lanjut, silakan bertanya!
