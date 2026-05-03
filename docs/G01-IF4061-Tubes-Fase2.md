**IF4061 - Visualisasi Data**
**Dosen Pengampu:** Dessi Puji Lestari, S.T, M.Eng., Ph.D.

***Tugas Besar 1 - Fase 2***
**Visualisasi Data Statik:**

*Penentuan Tujuan, Persiapan Data, Fokus Editorial, Konsep Desain, Konstruksi dan Evaluasi*

Disusun oleh - Kelompok 01:

**13523004**    Razi Rachman Widyadhana
**13523006**    William Andrian Dharma T
**13523086**    Bob Kunanda
**13523103**    Steven Owen Liauw
**13523109**    Haegen Quinston

Prodi Teknik Informatika
Sekolah Teknik Elektro dan Informatika
Institut Teknologi Bandung
Semester Genap Tahun Akademik 2025/2026

---

# Daftar Isi {#daftar-isi}

[Langkah 1: Define Purpose and Parameters](#langkah-1)

[1.1 Topic](#1.1-topic)

[1.2 Purpose](#1.2-purpose)

[1.3 Users](#1.3-users)

[1.4 Tone](#1.4-tone)

[Langkah 2: Eksplorasi dan Persiapan Data](#langkah-2)

[2.1 Data Acquisition](#2.1-data-acquisition)

[2.2 Data Examination](#2.2-data-examination)

[2.3 Data Type Identification](#2.3-data-type-identification)

[2.4 Data Cleaning & Quality Improvement](#2.4-data-cleaning)

[2.5 Data Transformation for Analysis](#2.5-data-transformation)

[2.5.1 Pipeline ppo: Penggabungan Lima Tahun ke Format Wide](#2.5-data-transformation)

[2.5.2 Pipeline jabar: Penggabungan Tiga Indikator](#2.5-data-transformation)

[2.5.3 Pipeline jabar: Penambahan Kolom Turunan](#2.5-data-transformation)

[2.5.4 Penentuan Wilayah Anomali](#2.5-data-transformation)

[2.5.5 Penghitungan Peringkat](#2.5-data-transformation)

[2.6 Data Consolidation](#2.6-data-consolidation)

[Langkah 3: Formulasi Pertanyaan dan Fokus Editorial](#langkah-3)

[3.1 Analytical Question](#3.1-analytical-question)

[3.2 Editorial Focus](#3.2-editorial-focus)

[3.3 Reasoning](#3.3-reasoning)

[3.4 Narrative](#3.4-narrative)

[3.5 Genre](#3.5-genre)

[3.6 Narrative Tactics](#3.6-narrative-tactics)

[Langkah 4: Konsep Desain](#langkah-4)

[4.1 Data Representation](#4.1-data-representation)

[4.2 Data Presentation](#4.2-data-presentation)

[Langkah 5: Konstruksi dan Evaluasi](#langkah-5)

[5.1 Tools yang Digunakan](#5.1-tools)

[5.2 Evaluasi Visualisasi](#5.2-evaluasi)

[5.3 Feedback Pengguna](#5.3-feedback)

[5.4 Refleksi](#5.4-refleksi)

[Daftar Pustaka](#daftar-pustaka)

[Pembagian Tugas](#pembagian-tugas)

---

## **Langkah 1: *Define Purpose and Parameters*** {#langkah-1}

---

### **1.1 *Topic*** {#1.1-topic}

Topik yang dianalisis adalah pola kemiskinan di Jawa Barat pada 2025, dengan fokus khusus pada hubungan antara tingkat pengangguran terbuka (TPT) dan angka kemiskinan di level kabupaten/kota. Jawa Barat merupakan provinsi berpenduduk terbesar di Indonesia dengan lebih dari 48 juta jiwa, namun angka kemiskinan agregatnya menyembunyikan disparitas yang tajam antara koridor industri di utara dan kawasan pertanian di selatan serta timur.

Angka kemiskinan agregat yang sering dikutip dalam laporan nasional tidak mengungkap dinamika di dalam provinsi itu sendiri. Disparitas antarwilayah dan pola yang tidak sepenuhnya linear antara pengangguran dan kemiskinan mengindikasikan adanya faktor struktural yang perlu ditelusuri lebih dalam melalui data tingkat kabupaten/kota.

Analisis ini menggunakan data BPS untuk tahun 2025 pada level kabupaten/kota serta data tren kemiskinan lima tahun (2021-2025) di enam provinsi Pulau Jawa sebagai konteks komparatif.

### **1.2 *Purpose*** {#1.2-purpose}

Visualisasi ini dibuat untuk mengungkap bahwa status "bekerja" tidak selalu berarti terbebas dari kemiskinan. Di sejumlah kabupaten Jawa Barat yang diindikasikan didominasi sektor pertanian, tingkat pengangguran sangat rendah, namun angka kemiskinan justru termasuk tertinggi se-provinsi. Kondisi ini mengindikasikan bahwa upah yang diperoleh belum mencukupi untuk melampaui garis kemiskinan setempat, dan tidak akan tertangkap apabila hanya membaca angka pengangguran sebagai proksi tunggal kesejahteraan.

Tujuan yang lebih dalam adalah mendorong pembaca untuk mempertanyakan asumsi bahwa pengangguran merupakan satu-satunya penyebab kemiskinan. Kualitas pekerjaan, bukan hanya ketersediaannya, menjadi faktor penentu yang sering luput dari diskusi kebijakan tingkat daerah. Visualisasi ini hadir sebagai argumen berbasis data yang menjembatani gap antara statistik agregat dan realitas struktural di lapangan.

### **1.3 *Users*** {#1.3-users}

Target pengguna adalah **pembaca terdidik** yang mengikuti isu pembangunan dan kesejahteraan daerah. Profil ini mencakup mahasiswa ilmu sosial dan kebijakan publik, jurnalis data, serta pembuat kebijakan di tingkat provinsi maupun kabupaten yang terbiasa membaca laporan BPS dan media seperti Katadata, Tirto, atau *Our World in Data*. Pengguna tidak harus berlatar belakang analisis data kuantitatif, namun perlu terbuka untuk membaca visualisasi yang membangun argumen secara bertahap.

Dalam konteks tugas ini, audiens utama adalah sesama mahasiswa dan dosen pengampu yang akan mengevaluasi ketepatan pemilihan visualisasi dan kejelasan narasi.

### **1.4 *Tone*** {#1.4-tone}

Visualisasi ini berada pada kutub ***pragmatic*** dalam kerangka Kirk (2012), di mana kepentingan utama adalah kejelasan pesan dan efektivitas komunikasi informasi. Dalam ranah *pragmatic* tersebut, gaya yang dipilih bersifat **analitis-persuasif** dengan sudut pandang investigatif, yakni ada sesuatu yang tersembunyi di balik angka yang tampak wajar, dan posisi itu harus terasa melalui cara visual ini disusun.

Nada ini diwujudkan melalui judul yang tegas, anotasi yang bersifat editorial, serta urutan narasi yang membangun ketegangan dari gambaran umum menuju temuan yang mengejutkan. Visualisasi dirancang untuk memancing refleksi tanpa menghakimi wilayah atau kelompok masyarakat tertentu secara eksplisit.

---

## **Langkah 2: Eksplorasi dan Persiapan Data** {#langkah-2}

---

### **2.1 *Data Acquisition*** {#2.1-data-acquisition}

#### **2.1.1 Sumber *Dataset***

Seluruh data statistik bersumber dari Badan Pusat Statistik (BPS) Republik Indonesia melalui portal resmi di https://open.bps.go.id. Dua kelompok data digunakan dengan cakupan yang berbeda.

Kelompok pertama adalah data tren kemiskinan tingkat provinsi, yaitu lima file tahunan berisi persentase penduduk miskin di seluruh provinsi Indonesia, masing-masing untuk tahun 2021 hingga 2025, dengan nama file `ppo_indonesia_{tahun}.csv`. Kelompok kedua adalah data kabupaten/kota Jawa Barat tahun 2025, yaitu tiga file indikator terpisah (persentase penduduk miskin, tingkat pengangguran terbuka/TPT, dan garis kemiskinan per kapita per bulan).

Data batas wilayah (poligon kabupaten/kota) diperoleh dari GADM (*Global Administrative Areas*) versi 4.1 Level 2 untuk Indonesia, tersedia di https://gadm.org, sebagai dasar pembuatan peta koropleth.

#### **2.1.2 Cara Memperoleh**

Seluruh file BPS diunduh dalam format CSV melalui mekanisme ekspor tabel pada portal BPS. File indikator jabar menggunakan format yang seragam, yaitu empat baris header non-data di bagian atas, diikuti baris data dengan dua kolom utama (nama wilayah dan nilai indikator). File ppo tahunan menggunakan format yang lebih kompleks dengan sepuluh kolom, yaitu satu kolom nama provinsi dan sembilan kolom nilai yang terbagi dalam tiga kelompok (perkotaan, perdesaan, dan total/Jumlah), masing-masing berisi nilai Semester 1, Semester 2, dan rata-rata tahunan. File GeoJSON GADM diunduh dalam format terkompresi (.zip) dari portal resmi GADM.

#### **2.1.3 Lisensi dan Etika Penggunaan Data**

BPS mempublikasikan seluruh data statistik resmi sebagai data publik yang dapat digunakan untuk keperluan akademik, penelitian, dan non-komersial. Atribusi kepada BPS RI disertakan dalam setiap visualisasi. Data GADM tersedia untuk penggunaan akademik dan non-komersial dengan atribusi kepada sumber. Tidak ada isu privasi individual karena seluruh data merupakan agregat tingkat kabupaten/kota atau provinsi.

### **2.2 *Data Examination*** {#2.2-data-examination}

Pemeriksaan dilakukan secara terpisah pada dua kelompok data.

**Dataset ppo tahunan (tren Pulau Jawa).** Setiap file `ppo_indonesia_{tahun}.csv` berisi data seluruh provinsi Indonesia dengan lima baris header diikuti sepuluh kolom data. Kolom pertama (indeks 0) berisi nama provinsi, kemudian diikuti tiga kelompok nilai (perkotaan, perdesaan, dan total/Jumlah) yang masing-masing memuat subkolom Semester 1, Semester 2, dan rata-rata tahunan. Pipeline menggunakan kolom indeks 0, 1, dan 2, yaitu nama provinsi serta kemiskinan perkotaan Semester 1 dan Semester 2. Pemeriksaan mengonfirmasi bahwa nilai Semester 2 perkotaan konsisten tersedia untuk enam provinsi Pulau Jawa di seluruh tahun, kecuali beberapa kasus di tahun tertentu yang hanya tersedia nilai Semester 1. Nama provinsi menggunakan huruf kapital penuh (misalnya *JAWA BARAT*, *DKI JAKARTA*) dan memerlukan pencocokkan eksak saat filter.

![][image1]

**Gambar 2.2.1** Pratinjau Baris Pertama File `ppo_indonesia_{tahun}.csv` Mentah.

**Dataset kabupaten/kota Jawa Barat.** Setiap file indikator berisi satu kolom nama wilayah dan satu kolom nilai. Pemeriksaan mengidentifikasi adanya baris agregat provinsi yang disisipkan di antara baris kabupaten/kota, serta satu baris dengan nilai *NaN* pada kolom nama wilayah sebagai artefak dari format header BPS. Kedua kondisi ini harus ditangani sebelum penggabungan.

![][image2]

**Gambar 2.2.2** Pratinjau File Indikator BPS Kabupaten/Kota Jawa Barat (salah satu dari tiga file).

**Dataset GADM.** Pemeriksaan pada properti GeoJSON menemukan bahwa atribut *NAME_1* menggunakan format tanpa spasi (*JawaBarat*) dan atribut *NAME_2* untuk wilayah bertipe Kota tidak menyertakan spasi setelah prefiks "Kota" (misalnya *KotaBandung*, *KotaDepok*). Kondisi ini memerlukan normalisasi sebelum penggabungan dengan data BPS.

![][image3]

**Gambar 2.2.3** Pemeriksaan Nilai Unik Atribut *NAME_1* dan *NAME_2* pada GeoJSON GADM 4.1.

### **2.3 *Data Type Identification*** {#2.3-data-type-identification}

**Tabel 2.3.1** Identifikasi Tipe Data - Dataset ppo Tahunan (per file, 10 kolom setelah `skiprows=4`)

| Indeks | Nama Kolom | Tipe Asli | Digunakan | Keterangan |
| ----: | :---- | :---- | :----: | :---- |
| 0 | Provinsi | *object* | Ya | Nama provinsi huruf kapital, *key* filter |
| 1 | Perkotaan S1 | *object* | Ya | Kemiskinan perkotaan Semester 1 (Maret), dikonversi ke numerik |
| 2 | Perkotaan S2 | *object* | Ya | Kemiskinan perkotaan Semester 2 (September), nilai acuan utama |
| 3 | Perkotaan Tahunan | *object* | Tidak | Rata-rata tahunan perkotaan |
| 4 | Perdesaan S1 | *object* | Tidak | Kemiskinan perdesaan Semester 1 (Maret) |
| 5 | Perdesaan S2 | *object* | Tidak | Kemiskinan perdesaan Semester 2 (September) |
| 6 | Perdesaan Tahunan | *object* | Tidak | Rata-rata tahunan perdesaan |
| 7 | Jumlah S1 | *object* | Tidak | Total kemiskinan Semester 1 (Maret) |
| 8 | Jumlah S2 | *object* | Tidak | Total kemiskinan Semester 2 (September) |
| 9 | Jumlah Tahunan | *object* | Tidak | Rata-rata tahunan total |

**Tabel 2.3.2** Identifikasi Tipe Data - `Persentase_Penduduk_Miskin_Menurut_Kabupaten_Kota_di_Jawa_Barat_2025.csv`

| Indeks | Nama dalam Pipeline | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----: | :---- | :---- | :---- | :---- |
| 0 | region | *object* | *Categorical* | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | poverty_rate | *object* | Float64 | Persentase penduduk miskin, dikonversi ke numerik |

**Tabel 2.3.3** Identifikasi Tipe Data - `Tingkat_Pengangguran_Terbuka_Menurut_Kabupaten_Kota_2025.csv`

| Indeks | Nama dalam Pipeline | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----: | :---- | :---- | :---- | :---- |
| 0 | region | *object* | *Categorical* | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | unemployment_rate | *object* | Float64 | TPT dalam persen, dikonversi ke numerik |

**Tabel 2.3.4** Identifikasi Tipe Data - `Garis_Kemiskinan_Menurut_Kabupaten_Kota_2025.csv`

| Indeks | Nama dalam Pipeline | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----: | :---- | :---- | :---- | :---- |
| 0 | region | *object* | *Categorical* | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | poverty_level | *object* | Float64 | Garis kemiskinan dalam Rp/kapita/bulan, dikonversi ke numerik |

Ketiga file dibaca dengan `header=None` karena tidak memiliki baris header standar. Kolom kedua (indeks 1) diberi nama berbeda sesuai indikatornya dalam pipeline, kemudian digabungkan menjadi satu tabel (lihat Bagian 2.5.2).

### **2.4 *Data Cleaning & Quality Improvement*** {#2.4-data-cleaning}

#### **2.4.1 Pipeline ppo: Filter Provinsi dan Seleksi Nilai Semester**

Dari setiap file tahunan, hanya enam baris yang merepresentasikan provinsi Pulau Jawa yang dipertahankan melalui filter nama eksak (*JAWA BARAT*, *JAWA TENGAH*, *JAWA TIMUR*, *DKI JAKARTA*, *BANTEN*, *DI YOGYAKARTA*). Nilai Semester 2 digunakan sebagai acuan utama karena mencerminkan kondisi akhir tahun. Apabila nilai Semester 2 tidak tersedia (*NaN*), nilai Semester 1 digunakan sebagai *fallback*. Perlakuan ini memastikan tidak ada titik data yang hilang pada rentang 2021-2025.

![][image4]

**Gambar 2.4.1** Dataset ppo Setelah Filter Enam Provinsi Pulau Jawa (satu tahun sebagai contoh).

#### **2.4.2 Pipeline jabar: Penghapusan Baris Tidak Relevan**

Baris dengan nilai *NaN* pada kolom *region* dibuang karena merupakan artefak dari format header BPS. Baris yang mengandung kata "Provinsi" pada kolom *region* dibuang karena merepresentasikan agregat provinsi yang tidak relevan untuk analisis level kabupaten/kota.

![][image5]

**Gambar 2.4.2** Dataset jabar Setelah Penghapusan Baris Tidak Relevan (27 baris tersisa).

#### **2.4.3 Pipeline jabar: Normalisasi Nama Wilayah untuk Penggabungan GADM**

File GeoJSON GADM menggunakan format *NAME_2* tanpa spasi untuk wilayah bertipe Kota. Untuk menyelaraskan dengan data BPS, seluruh entri *NAME_2* dengan *TYPE_2 = Kota* dimodifikasi dengan menambahkan spasi setelah prefiks "Kota" secara *in-place* sebelum penggabungan. Satu pengecualian ditangani melalui peta manual: *Bandung Barat* dalam BPS berpadanan dengan *BandungBarat* dalam GADM.

![][image6]

**Gambar 2.4.3** Perbandingan Nilai *NAME_2* Sebelum dan Sesudah Normalisasi pada GeoJSON GADM.

#### **2.4.4 Pipeline jabar: Konversi Tipe Data**

Kolom nilai numerik (*poverty_rate*, *unemployment_rate*, *poverty_level*) dikonversi dari tipe *object* ke *float* menggunakan parameter `errors='coerce'` sehingga nilai non-numerik yang tersisa otomatis menjadi *NaN* dan dapat diidentifikasi.

![][image7]

**Gambar 2.4.4** Tipe Data Dataset jabar Setelah Konversi Numerik.

### **2.5 *Data Transformation for Analysis*** {#2.5-data-transformation}

#### **2.5.1 Pipeline ppo: Penggabungan Lima Tahun ke Format Wide**

Setelah setiap file tahunan diproses secara independen (filter, seleksi semester), kelima *dataframe* digabungkan secara berurutan menggunakan kolom *Provinsi* sebagai *key* melalui operasi *outer merge*. Hasil akhir adalah tabel dengan enam baris (satu per provinsi Pulau Jawa) dan tujuh kolom, yaitu *Provinsi* dan satu kolom per tahun (2021-2025). Format *wide* ini langsung dapat digunakan untuk pembuatan grafik garis dengan setiap kolom tahun sebagai sumbu-x.

![][image8]

**Gambar 2.5.1** Hasil Penggabungan Lima Tahun ke Format *Wide* (`ppo_jawa_2021-2025.csv`).

#### **2.5.2 Pipeline jabar: Penggabungan Tiga Indikator**

Tiga file BPS kabupaten/kota digabungkan menjadi satu tabel menggunakan kolom *region* sebagai *key* melalui operasi *inner join*. Hasil penggabungan menghasilkan 27 baris kabupaten/kota dengan empat kolom (*region*, *poverty_rate*, *unemployment_rate*, dan *poverty_level*).

![][image9]

**Gambar 2.5.2** Dataset jabar Hasil Penggabungan Tiga Indikator (27 baris, 4 kolom).

#### **2.5.3 Pipeline jabar: Penambahan Kolom Turunan**

Kolom *type* ditambahkan untuk membedakan Kota dan Kabupaten berdasarkan prefiks "Kota " pada nama wilayah. Kolom *gadm_name* ditambahkan sebagai nama wilayah yang disesuaikan dengan format GADM untuk digunakan sebagai *key* penggabungan dengan GeoJSON. Kolom *ratio* dihitung sebagai *poverty_rate* dibagi *unemployment_rate*, yang mengekspresikan seberapa besar angka kemiskinan relatif terhadap tingkat pengangguran di setiap wilayah.

![][image10]

**Gambar 2.5.3** Pratinjau Kolom Turunan *type*, *gadm_name*, dan *ratio* pada Dataset jabar.

#### **2.5.4 Penentuan Wilayah Anomali**

Berdasarkan kolom *ratio*, enam wilayah dengan pola paling ekstrem dipilih sebagai subyek analisis mendalam. Tiga wilayah dengan rasio tertinggi (*ANOMALI_HIGH*) merepresentasikan kondisi kemiskinan tinggi meskipun pengangguran sangat rendah, sedangkan tiga wilayah dengan rasio terendah (*ANOMALI_LOW*) merepresentasikan kondisi sebaliknya. Majalengka dikecualikan dari *ANOMALI_HIGH* karena garis kemiskinannya berada di atas median provinsi, sehingga tidak konsisten dengan narasi yang dibangun. Wilayah anomali yang terpilih adalah sebagai berikut.

**Tabel 2.5.1** Enam Wilayah Anomali Terpilih

| Wilayah | TPT (%) | Kemiskinan (%) | GK (Rp/kap/bln) | Rasio | Kelompok |
| :---- | ----: | ----: | ----: | ----: | :---- |
| Pangandaran | 1,91 | 8,03 | 486.285 | 4,20 | Tinggi |
| Tasikmalaya | 3,69 | 10,15 | 413.178 | 2,75 | Tinggi |
| Ciamis | 4,08 | 7,19 | 483.644 | 1,76 | Tinggi |
| Kota Depok | 6,52 | 2,31 | 884.633 | 0,35 | Rendah |
| Kota Cimahi | 8,75 | 4,20 | 642.016 | 0,48 | Rendah |
| Bekasi | 8,78 | 4,36 | 698.154 | 0,50 | Rendah |

#### **2.5.5 Penghitungan Peringkat**

Kolom peringkat dihitung dari urutan setiap wilayah di antara 27 kabupaten/kota Jawa Barat menggunakan `DataFrame.rank(method='min')`. Kolom *tpt_rank* menyatakan peringkat TPT (1 = TPT terendah) dan kolom *gk_rank* menyatakan peringkat garis kemiskinan (1 = garis kemiskinan terendah), keduanya dalam skala bilangan bulat 1-27.

![][image11]

**Gambar 2.5.5** Peringkat TPT dan Garis Kemiskinan untuk Enam Wilayah Anomali.

### **2.6 *Data Consolidation*** {#2.6-data-consolidation}

Seluruh hasil pembersihan dan transformasi disimpan dalam dua file bersih di direktori `data/clean/` melalui proses yang sepenuhnya terotomasi dalam *notebook*. Kedua pipeline berjalan pada bagian Persiapan Data sebelum visualisasi dijalankan, sehingga tidak diperlukan file bersih yang disiapkan secara manual di luar *notebook*. File *ppo_jawa_2021-2025.csv* dihasilkan dari penggabungan lima file tahunan mentah, sedangkan *jabar_2025_combined.csv* dihasilkan dari penggabungan tiga file indikator mentah Jawa Barat.

**Tabel 2.6.1** Dataset Final

| File | Baris | Kolom Kunci | Keterangan |
| :---- | :---- | :---- | :---- |
| *jabar_2025_combined.csv* | 27 | region, poverty_rate, unemployment_rate, poverty_level | Kabupaten/kota Jawa Barat 2025 |
| *ppo_jawa_2021-2025.csv* | 6 | Provinsi, 2021-2025 | Tren provinsi Pulau Jawa |

![][image12]

**Gambar 2.6.1** Konfirmasi Kedua File Bersih di Direktori `data/clean/`.

---

## **Langkah 3: Formulasi Pertanyaan dan Fokus Editorial** {#langkah-3}

---

### **3.1 *Analytical Question*** {#3.1-analytical-question}

Mengapa korelasi antara tingkat pengangguran terbuka dan angka kemiskinan di kabupaten/kota Jawa Barat bersifat negatif dan lemah? Wilayah mana yang membentuk anomali paling ekstrem, dan apakah perbedaan garis kemiskinan antar daerah menjadi faktor yang menjelaskan anomali tersebut?

### **3.2 *Editorial Focus*** {#3.2-editorial-focus}

Di sejumlah kabupaten pertanian Jawa Barat, hampir semua orang bekerja, namun tetap miskin. Upah sektor pertanian berada di bawah garis kemiskinan daerah itu sendiri. Kondisi ini tidak tertangkap apabila hanya membaca angka pengangguran sebagai proksi kesejahteraan.

Pesan ini dibangun dari data BPS yang tersedia secara publik, dan tidak memerlukan asumsi di luar yang dapat diverifikasi langsung dari angka yang ada.

### **3.3 *Reasoning*** {#3.3-reasoning}

Pendekatan yang digunakan adalah ***inductive reasoning***, yakni observasi terhadap enam wilayah anomali spesifik membentuk dasar untuk menarik kesimpulan yang lebih luas tentang karakteristik struktural kemiskinan di kawasan pertanian Jawa Barat. Pola yang ditemukan pada kelompok kecil wilayah ini, yaitu bahwa garis kemiskinan rendah di kawasan pertanian mengindikasikan upah yang bahkan lebih rendah dari standar subsisten yang rendah sekalipun, digunakan untuk mendukung argumen tentang kualitas upah sebagai determinan kemiskinan.

### **3.4 *Narrative*** {#3.4-narrative}

Jenis cerita data yang dibangun adalah narasi ***anomaly-driven*** yang bersifat *author-driven*. Mengacu pada Segel dan Heer (2010), posisi ini berada di ujung *author-driven* dari spektrum narasi, di mana alur membawa audiens dari konteks yang familiar menuju temuan yang mengejutkan, kemudian menuju penjelasan mekanistik.

Urutan narasinya adalah sebagai berikut. Pertama, audiens melihat Jawa Barat dalam konteks Pulau Jawa secara keseluruhan sehingga tidak ada kekhawatiran tentang kondisi provinsi secara umum. Kedua, sebaran spasial memperlihatkan bahwa disparitas internal provinsi jauh lebih besar dari angka agregat. Ketiga, korelasi negatif antara pengangguran dan kemiskinan memunculkan pertanyaan yang belum terjawab. Keempat, analisis garis kemiskinan memberikan jawaban parsial: di kawasan pertanian murah, upah bahkan lebih rendah dari standar subsisten yang rendah.

### **3.5 *Genre*** {#3.5-genre}

Visualisasi ini termasuk dalam kategori ***explanatory visualization***. Pembuat memiliki satu argumen spesifik yang ingin disampaikan dan seluruh elemen visual dirancang untuk mendukung penyampaian argumen tersebut secara berurutan. Audiens tidak diharapkan menemukan *insight*-nya sendiri, melainkan diantar untuk memahami dan memverifikasi argumen yang sudah dibangun.

Dalam kerangka Segel dan Heer (2010), format fisik yang digunakan adalah *partitioned poster* dengan elemen *magazine-style*, yaitu empat panel yang masing-masing mandiri, namun bersama-sama membentuk satu narasi kohesif.

### **3.6 *Narrative Tactics*** {#3.6-narrative-tactics}

#### **3.6.1 Urutan Informasi**

Narasi mengikuti struktur *linear* dari makro ke mikro. Grafik 1 menetapkan konteks provinsi di Pulau Jawa. Grafik 2 memperlihatkan disparitas internal Jawa Barat secara spasial. Grafik 3 memunculkan anomali melalui korelasi yang berlawanan dengan intuisi umum. Grafik 4 menguji satu hipotesis penjelasan dan menyimpulkan kondisi struktural yang menjadi akar masalah.

#### **3.6.2 Fokus Perhatian**

Warna merah (#E63946) digunakan secara konsisten untuk Jawa Barat pada Grafik 1 dan untuk kelompok anomali dengan kemiskinan tinggi pada Grafik 4. Warna hijau (#2A9D8F) digunakan untuk kelompok anomali dengan kemiskinan rendah pada Grafik 4. Pada Grafik 1, lima provinsi konteks ditampilkan dalam abu-abu (#888888) agar Jawa Barat menonjol tanpa gangguan warna kompetitif. Pada Grafik 3, kelompok Kabupaten menggunakan merah kategori (#C0392B) dan Kota menggunakan biru gelap (#1A6B8A) sebagai warna kategori yang berbeda dari merah-hijau Grafik 4 sehingga tidak menimbulkan kebingungan semantik. Label nama wilayah hanya ditampilkan untuk enam wilayah anomali sehingga perhatian pembaca terpusat pada kasus-kasus yang membentuk argumen.

#### **3.6.3 *Highlight Insight* Utama**

*Insight* yang diharapkan tersampaikan adalah bahwa di kelompok anomali tinggi (Pangandaran, Tasikmalaya, Ciamis), garis kemiskinan berada di kisaran bawah hingga menengah, namun kemiskinan tetap tinggi. Ini berarti bukan biaya hidup yang menyebabkan anomali, melainkan upah pertanian yang tidak mencukupi bahkan untuk memenuhi standar subsisten yang relatif rendah. Di kelompok anomali rendah (Kota Depok, Kota Cimahi, Bekasi), garis kemiskinan sangat tinggi, namun kemiskinan sangat rendah, mengonfirmasi bahwa pendapatan formal di kawasan urban melampaui standar biaya hidup yang mahal sekalipun.

---

## **Langkah 4: Konsep Desain** {#langkah-4}

---

### **4.1 *Data Representation*** {#4.1-data-representation}

#### **4.1.1 Pemilihan Metode dan Jenis Grafik**

Setiap grafik dipilih berdasarkan tujuan komunikasi primernya sesuai taksonomi Kirk (2012) Bab 5, dengan mempertimbangkan sifat data, jumlah variabel, dan tingkat akurasi yang dibutuhkan audiens.

**Tabel 4.1.1** Justifikasi Pemilihan Jenis Grafik

| Grafik | Metode (Kirk 2012) | Jenis Grafik | Variabel | Justifikasi |
| :---- | :---- | :---- | :---- | :---- |
| G1: Tren Pulau Jawa | *Showing changes over time* | *Line chart* | 1 temporal, 6 seri provinsi | Perubahan temporal paling akurat dikodekan melalui posisi pada sumbu vertikal bersama. Enam seri dapat dibedakan dengan warna tanpa mengorbankan keterbacaan. |
| G2: Peta Jawa Barat | *Mapping geo-spatial data* | Koropleth | 1 kuantitatif-rasio, 27 wilayah | Distribusi spasial memerlukan substrat geografis. Warna sekuensial (*Reds*) mengkodekan satu variabel kuantitatif sesuai hierarki akurasi MacKinlay. |
| G3: Korelasi | *Plotting connections and relationships* | *Scatter plot* | 2 kuantitatif, 1 kategorikal (warna) | Dua variabel kuantitatif dipetakan pada dua sumbu posisi, variabel yang paling akurat menurut hierarki MacKinlay. Garis regresi per kelompok memperlihatkan arah korelasi. |
| G4: Anomali | *Comparing categorical values* | *Slopegraph* | 1 kategorikal, 2 kuantitatif (peringkat) | Dua metrik per wilayah pada sumbu vertikal bersama memungkinkan perbandingan langsung. Kirk (2012) secara eksplisit mendefinisikan *slopegraph* sebagai pilihan tepat untuk menampilkan perbandingan dua metrik per kategori. Kemiringan garis langsung memperlihatkan arah dan besar perbedaan. |

Grafik dengan dua sumbu-y (*dual y-axis*) tidak digunakan karena tidak termuat dalam taksonomi Kirk dan menurunkan akurasi komparasi yang seharusnya disediakan oleh posisi sebagai variabel visual primer.

#### **4.1.2 Tingkat Kedetailan**

**Tabel 4.1.2** Tingkat Kedetailan per Grafik

| Grafik | Cakupan | Label |
| :---- | :---- | :---- |
| G1 - Tren Pulau Jawa | 6 provinsi, 5 tahun (2021-2025) | Nama provinsi langsung di ujung setiap garis |
| G2 - Peta Jawa Barat | 27 kabupaten/kota | Nomor urut kemiskinan di sentroid setiap poligon; legenda kartu berisi peringkat, nama, dan nilai untuk seluruh 27 wilayah |
| G3 - Korelasi | 27 kabupaten/kota | Nama hanya untuk 6 wilayah anomali |
| G4 - Anomali | 6 wilayah anomali | Nama wilayah di sisi kiri *slopegraph*; legenda dua warna; garis median sebagai referensi |

#### **4.1.3 *Design Metaphor***

Tidak ada *design metaphor* ikonik yang digunakan. Warna merah (#E63946) bertindak sebagai penanda semantik yang konsisten: pada Grafik 1 merah menyoroti Jawa Barat sebagai fokus, dan pada Grafik 4 merah menandai anomali kemiskinan tinggi. Hijau-teal (#2A9D8F) pada Grafik 4 menandai anomali kemiskinan rendah sebagai pasangan kontrastif. Konsistensi dua warna ini pada Grafik 1 dan 4 menggantikan kebutuhan legenda berulang pada panel tersebut.

### **4.2 *Data Presentation*** {#4.2-data-presentation}

#### **4.2.1 Palet Warna**

Pemilihan warna mengikuti dua prinsip, yaitu keterbacaan untuk audiens umum dan konsistensi semantik lintas grafik.

**Tabel 4.2.1** Palet Warna dan Fungsinya

| Warna | Kode Hex | Fungsi |
| :---- | :---- | :---- |
| Merah | #E63946 | Jawa Barat (G1), anomali kemiskinan tinggi (G4) |
| Hijau-teal | #2A9D8F | Anomali kemiskinan rendah (G4) |
| Biru gelap | #1A6B8A | Kelompok Kota (G3) |
| Merah kategori | #C0392B | Kelompok Kabupaten (G3) |
| Abu-abu | #888888 | Lima provinsi konteks Pulau Jawa (G1) |
| Merah sekuensial | *Reds* (ColorBrewer) | Intensitas kemiskinan pada koropleth (G2) |

Warna merah dan hijau-teal dipilih sebagai aksen utama karena memiliki kontras luminansi yang cukup untuk pengguna dengan *deuteranomaly* (defisiensi penglihatan hijau-merah paling umum) apabila dilengkapi dengan perbedaan bentuk dan posisi.

#### **4.2.2 *Explanatory Annotation***

Setiap grafik dilengkapi dengan anotasi yang membantu interpretasi tanpa mengulang isi yang sudah jelas dari visual itu sendiri.

**Tabel 4.2.2** Anotasi per Grafik

| Grafik | Anotasi |
| :---- | :---- |
| G1 - Tren Pulau Jawa | Nama provinsi langsung di ujung kanan setiap garis sehingga tidak diperlukan legenda terpisah. |
| G2 - Peta Jawa Barat | Nama wilayah beserta nilai persentase kemiskinan di sentroid setiap poligon untuk wilayah yang memiliki data. |
| G3 - Korelasi | Nilai korelasi Pearson (r = -0,37) di sudut kanan atas. Nama enam wilayah anomali diberi label langsung pada titik yang bersangkutan. |
| G4 - Anomali | Nama wilayah di sisi kiri *slopegraph*. Legenda dua warna di bawah grafik: teal untuk "Pengangguran Tinggi, Kemiskinan Rendah" dan merah untuk "Pengangguran Rendah, Kemiskinan Tinggi". Garis median sebagai referensi horizontal. |

Blok **Wawasan** (*insight*) dalam format *blockquote* ditempatkan di bawah setiap grafik sebagai anotasi naratif yang merangkum temuan utama dalam bahasa yang dapat dipahami audiens non-teknis.

#### **4.2.3 *Layout***

Visualisasi disajikan dalam format *notebook* Jupyter yang bersifat linear top-down, sesuai urutan narasi yang telah ditetapkan. Setiap panel grafik berdiri sendiri dengan judul, sumbu berlabel, dan blok wawasan, sehingga dapat dipahami secara independen sekalipun tanpa membaca panel sebelumnya. Untuk format poster, tiga panel pertama (G1, G2, G3+G4) disusun secara vertikal. Grafik 3 dan Grafik 4 digabungkan dalam satu baris berdampingan di bawah satu *section header* bersama, diikuti blok *insight* penuh yang merangkum temuan kedua grafik secara terintegrasi. *Footer* memuat sumber data dan nama anggota kelompok.

---

## **Langkah 5: Konstruksi dan Evaluasi** {#langkah-5}

---

### **5.1 *Tools* yang Digunakan** {#5.1-tools}

**Tabel 5.1.1** *Tools* dan Fungsinya

| *Tool* | Versi | Fungsi |
| :---- | :---- | :---- |
| Python | 3.13 | Bahasa pemrograman utama untuk seluruh *pipeline* |
| pandas | - | Pembacaan, pembersihan, transformasi, dan penggabungan data |
| geopandas | - | Pembacaan GeoJSON GADM dan *rendering* koropleth |
| matplotlib | - | Konstruksi seluruh grafik (G1-G4) |
| scipy.stats | - | Perhitungan korelasi Pearson dan regresi linier per kelompok |
| Jupyter Notebook | - | Dokumentasi *pipeline* sekaligus medium presentasi hasil |

Seluruh *pipeline* dari pembacaan data mentah hingga menghasilkan grafik final disimpan dalam satu *notebook* tunggal (`src/main.ipynb`) yang dibangun dari skrip generator (`src/build_main.py`) untuk memastikan reproducibility.

### **5.2 Evaluasi Visualisasi** {#5.2-evaluasi}

Evaluasi dilakukan berdasarkan kerangka "Things to do Before Launching" dari materi perkuliahan.

#### **a. Data & Statistical Accuracy**

Nilai korelasi Pearson (r = -0,37) dihitung menggunakan `scipy.stats.pearsonr` dari seluruh 27 wilayah. Garis regresi pada Grafik 3 dihitung secara terpisah untuk kelompok Kota dan Kabupaten menggunakan `scipy.stats.linregress`. Peringkat pada Grafik 4 dihitung menggunakan `DataFrame.rank(method='min')` dari pandas, yang menghasilkan bilangan bulat 1-27 secara langsung. Tidak ada data *outlier* yang dibuang karena keenam wilayah anomali merupakan observasi valid yang justru menjadi subjek analisis.

#### **b. Visual Inference**

Sumbu-y pada Grafik 1 dan 3 tidak dipotong dari nilai bukan nol untuk mencegah distorsi persepsi besar perubahan. Grafik 4 menggunakan skala peringkat 1-27 yang seragam pada sumbu-y sehingga kemiringan garis dapat dibandingkan secara langsung antar wilayah. Koropleth pada Grafik 2 menggunakan skala warna sekuensial yang tidak membalik arah persepsi (lebih merah = lebih tinggi = lebih perlu diperhatikan).

#### **c. Formatting Accuracy**

Ukuran *font* konsisten di seluruh grafik (judul 13-14pt, label sumbu 11pt, anotasi 8-9pt). Warna merah #E63946 digunakan secara konsisten sebagai aksen utama di seluruh grafik. *Spines* dihilangkan pada semua grafik untuk mengurangi *chartjunk*. Gridlines menggunakan gaya *dotted* (`:`) dengan transparansi 20-30%.

#### **d. Annotation Accuracy**

Judul setiap grafik mencantumkan nama wilayah, metrik, dan tahun secara eksplisit. Label sumbu dilengkapi satuan (% untuk persentase, Rp untuk garis kemiskinan apabila relevan). Blok wawasan ditulis dalam bahasa Indonesia yang dapat dipahami audiens umum.

### **5.3 *Feedback* Pengguna** {#5.3-feedback}

*[Placeholder - feedback dari minimal 5 responden akan diisikan setelah pengujian]*

Pertanyaan yang diajukan kepada responden:
1. Apakah visualisasi secara keseluruhan mudah dipahami tanpa penjelasan verbal tambahan?
2. Setelah melihat keempat grafik, apa pesan utama yang Anda tangkap?
3. Apakah ada grafik yang menimbulkan kebingungan atau memerlukan penjelasan lebih lanjut?
4. Apakah grafik keempat (*slopegraph* peringkat) mudah dibaca tanpa panduan?
5. Apakah ada informasi penting yang menurut Anda seharusnya ditampilkan tetapi tidak ada?

**Tabel 5.3.1** Ringkasan Feedback *(placeholder)*

| Responden | Grafik Paling Jelas | Grafik Paling Membingungkan | Pesan Utama yang Ditangkap | Saran |
| :----: | :---- | :---- | :---- | :---- |
| R1 | *[diisi]* | *[diisi]* | *[diisi]* | *[diisi]* |
| R2 | *[diisi]* | *[diisi]* | *[diisi]* | *[diisi]* |
| R3 | *[diisi]* | *[diisi]* | *[diisi]* | *[diisi]* |
| R4 | *[diisi]* | *[diisi]* | *[diisi]* | *[diisi]* |
| R5 | *[diisi]* | *[diisi]* | *[diisi]* | *[diisi]* |

### **5.4 Refleksi** {#5.4-refleksi}

*[Placeholder - akan diisikan setelah feedback terkumpul]*

**Apakah tujuan tercapai?**
*[diisi setelah feedback]*

**Apakah *insight* tersampaikan?**
*[diisi setelah feedback]*

**Apa kekurangan visualisasi?**

Berdasarkan evaluasi internal, beberapa kekurangan yang telah diidentifikasi adalah sebagai berikut. Pertama, *slopegraph* (Grafik 4) memerlukan tingkat literasi visualisasi yang lebih tinggi dibandingkan grafik batang. Audiens yang belum familiar dengan format ini mungkin memerlukan kalimat pengantar yang lebih eksplisit. Kedua, peta koropleth (Grafik 2) tidak menampilkan Pangandaran karena keterbatasan cakupan GADM 4.1. Ketiga, analisis saat ini terbatas pada satu titik waktu (2025) dan tidak dapat menelusuri apakah kondisi anomali ini bersifat persisten atau berubah sepanjang waktu.

---

## Daftar Pustaka {#daftar-pustaka}

---

1. Kirk, A. (2012). *Data Visualization: A Successful Design Process*. Packt Publishing.

2. Segel, E., & Heer, J. (2010). Narrative visualization: Telling stories with data. *IEEE Transactions on Visualization and Computer Graphics*, *16*(6), 1139-1148. https://doi.org/10.1109/TVCG.2010.179

3. Badan Pusat Statistik Jawa Barat. (2025). *Persentase Penduduk Miskin Menurut Kabupaten/Kota di Jawa Barat*. BPS Jawa Barat. https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html

4. Badan Pusat Statistik Jawa Barat. (2025). *Tingkat Pengangguran Terbuka Menurut Kabupaten/Kota di Jawa Barat*. BPS Jawa Barat. https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html

5. Badan Pusat Statistik. (2025). *Garis Kemiskinan (Rupiah/Kapita/Bulan) Menurut Provinsi dan Daerah*. BPS RI. https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html

6. Badan Pusat Statistik. (2021-2025). *Persentase Penduduk Miskin (P0) Menurut Provinsi dan Daerah*. BPS RI. https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html

7. GADM. (2023). *GADM data for Indonesia, Level 2 (Version 4.1)*. https://gadm.org

---

## Lampiran {#lampiran}

---

1. Pranala Data Sebelum Pemrosesan:

   - Persentase Penduduk Miskin Kabupaten/Kota Jawa Barat: https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html
   - TPT Kabupaten/Kota Jawa Barat: https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html
   - Garis Kemiskinan Menurut Provinsi dan Daerah: https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html
   - Persentase Penduduk Miskin Menurut Provinsi (tren 2021-2025): https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html

2. Pranala Data Sesudah Pemrosesan: *[diisi]*

3. Pranala Poster: *[diisi]*

4. *Notebook* Pemrosesan dan Visualisasi: *[diisi]*

---

## Pembagian Tugas {#pembagian-tugas}

---

| NIM | Nama Anggota | Tanggung Jawab | Deskripsi Tugas |
| :---: | :---: | :---: | :---: |
| **13523004** | **Razi Rachman Widyadhana** | **Langkah 2 & 5** | Pengolahan data, *pipeline* notebook (`build_main.py`), konstruksi grafik, dan evaluasi teknis. |
| **13523006** | **William Andrian Dharma T** | **Langkah 1** | Merumuskan *Purpose and Parameters* yang mencakup Topik, *Purpose*, *Users*, dan *Tone*. |
| **13523086** | **Bob Kunanda** | **Langkah 2** | Melakukan *Data Cleaning*, *Transformation*, dan *Consolidation* termasuk normalisasi GADM. |
| **13523103** | **Steven Owen Liauw** | **Langkah 3** | Menyusun *Analytical Question*, *Editorial Focus*, *Reasoning*, dan *Narrative*. |
| **13523109** | **Haegen Quinston** | **Langkah 4 & Finalisasi** | Merancang *Data Representation*, *Data Presentation*, *layout* poster, dan menyusun Daftar Pustaka. |
