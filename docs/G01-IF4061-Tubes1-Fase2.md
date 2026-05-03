  
**IF4061 \- Visualisasi Data**  
**Dosen Pengampu:** Dessi Puji Lestari, S.T, M.Eng., Ph.D.

***Tugas Besar 1 \- Fase 2***  
**Visualisasi Data Statik:**	

*Penentuan Tujuan, Persiapan Data, Penentuan Fokus Editorial*

Disusun oleh \- Kelompok 01:

**13523004**	   Razi Rachman Widyadhana  
**13523006**	   William Andrian Dharma T  
**13523086**	   Bob Kunanda  
**13523103**	   Steven Owen Liauw  
**13523109**	   Haegen Quinston

Prodi Teknik Informatika  
Sekolah Teknik Elektro dan Informatika  
Institut Teknologi Bandung  
Semester Genap Tahun Akademik  2025/2026

# **Daftar Isi** {#daftar-isi}

---

[**Daftar Isi	1**](#daftar-isi)

[**Daftar Gambar	3**](#daftar-gambar)

[**Daftar Tabel	4**](#daftar-tabel)

[**Langkah 1: Define Purpose and Parameters	5**](#langkah-1:-define-purpose-and-parameters)

[1.1 Topic	5](#1.1-topic)

[1.2 Purpose	5](#1.2-purpose)

[1.3 Users	6](#1.3-users)

[1.4 Tone	6](#1.4-tone)

[**Langkah 2: Eksplorasi dan Persiapan Data	7**](#langkah-2:-eksplorasi-dan-persiapan-data)

[2.1 Data Acquisition	7](#2.1-data-acquisition)

[2.1.1 Sumber Dataset	7](#2.1.1-sumber-dataset)

[2.1.2 Cara Memperoleh	7](#2.1.2-cara-memperoleh)

[2.1.3 Lisensi dan Etika Penggunaan Data	7](#2.1.3-lisensi-dan-etika-penggunaan-data)

[2.2 Data Examination	8](#2.2-data-examination)

[2.3 Data Type Identification	9](#2.3-data-type-identification)

[2.4 Data Cleaning & Quality Improvement	11](#2.4-data-cleaning-&-quality-improvement)

[2.4.1 Konversi Tipe	11](#2.4.1-konversi-tipe)

[2.4.2 Penghapusan Kolom Redundan	11](#2.4.2-penghapusan-kolom-redundan)

[2.4.3 Penandaan Entitas Agregat Regional	11](#2.4.3-penandaan-entitas-agregat-regional)

[2.4.4 Penanganan Nilai Kosong	12](#2.4.4-penanganan-nilai-kosong)

[2.5 Data Transformation for Analysis	12](#2.5-data-transformation-for-analysis)

[2.5.1 Filter Indeks Relevan	12](#2.5.1-filter-indeks-relevan)

[2.5.2 Reshape ke Format Wide	12](#2.5.2-reshape-ke-format-wide)

[2.5.3 Penambahan Variabel Turunan	13](#2.5.3-penambahan-variabel-turunan)

[2.5.4 Normalisasi Komponen HDI	13](#2.5.4-normalisasi-komponen-hdi)

[2.5.5 Penghitungan Peringkat	14](#2.5.5-penghitungan-peringkat)

[2.6 Data Consolidation	14](#2.6-data-consolidation)

[**Langkah 3: Formulasi Pertanyaan dan Fokus Editorial	15**](#langkah-3:-formulasi-pertanyaan-dan-fokus-editorial)

[3.1 Analytical Question	15](#3.1-analytical-question)

[3.2. Editorial Focus	15](#3.2.-editorial-focus)

[3.3 Reasoning	15](#3.3-reasoning)

[3.4 Narrative	15](#3.4-narrative)

[3.5 Genre	16](#3.5-genre)

[3.6 Narrative Tactics	16](#3.6-narrative-tactics)

[3.6.1 Urutan Informasi	16](#3.6.1-urutan-informasi)

[3.6.2 Fokus Perhatian	16](#3.6.2-fokus-perhatian)

[3.6.3 Highlight Insight Utama	17](#3.6.3-highlight-insight-utama)

[**Langkah 4: Konsep Desain	18**](#langkah-4:-konsep-desain)

[4.1 Data Representation	18](#4.1-data-representation)

[4.1.1 Pemilihan Metode dan Jenis Grafik	18](#4.1.1-pemilihan-metode-dan-jenis-grafik)

[4.1.2 Tingkat Kedetailan	19](#4.1.2-tingkat-kedetailan)

[4.1.3 Design Metaphor	19](#4.1.3-design-metaphor)

[4.2. Data Presentation	20](#4.2.-data-presentation)

[4.2.1 Palet Warna	20](#4.2.1-palet-warna)

[4.2.2 Explanatory Annotation	20](#4.2.2-explanatory-annotation)

[4.2.3 Layout	21](#4.2.3-layout)

[**Langkah 5: Konstruksi dan Evaluasi	22**](#langkah-5:-konstruksi-dan-evaluasi)

[5.1 Tools yang Digunakan	22](#5.1-tools-yang-digunakan)

[5.2 Evaluasi Visualisasi	22](#5.2-evaluasi-visualisasi)

[5.2.1 Functional Accuracy	22](#5.2.1-functional-accuracy)

[5.2.2 Data & Statistical Accuracy	22](#5.2.2-data-&-statistical-accuracy)

[5.2.3 Visual Inference	23](#5.2.3-visual-inference)

[5.2.4 Formatting Accuracy	23](#5.2.4-formatting-accuracy)

[5.2.5 Annotation Accuracy	23](#5.2.5-annotation-accuracy)

[5.3 Feedback Pengguna	23](#5.3-feedback-pengguna)

[5.4 Refleksi	24](#5.4-refleksi)

[**Daftar Pustaka	25**](#daftar-pustaka)

[**Lampiran	26**](#lampiran)

[**Pembagian Tugas	27**](#pembagian-tugas)

## 

# **Daftar Gambar** {#daftar-gambar}

---

[Gambar 2.2.1 Pratinjau Baris Pertama File ppo\_indonesia\_{tahun}.csv Mentah.	8](#gambar-2.2.1-pratinjau-baris-pertama-file-ppo_indonesia_{tahun}.csv-mentah.)

[Gambar 2.2.2 Pratinjau File Indikator BPS Kabupaten/Kota Jawa Barat	8](#gambar-2.2.2-pratinjau-file-indikator-bps-kabupaten/kota-jawa-barat)

[Gambar 2.2.3 Pemeriksaan Nilai Unik Atribut Nama Wilayah pada GeoJSON Jawa Barat	9](#gambar-2.2.3-pemeriksaan-nilai-unik-atribut-name_1-dan-name_2-pada-geojson-gadm)

[Gambar 2.4.2 Dataset jabar Setelah Penghapusan Baris Tidak Relevan (27 baris tersisa).	11](#gambar-2.4.2-dataset-jabar-setelah-penghapusan-baris-tidak-relevan-\(27-baris-tersisa\).)

[Gambar 2.4.3 Perbandingan Nilai NAME\_2 Sebelum dan Sesudah Normalisasi	12](#gambar-2.4.3-perbandingan-nilai-name_2-sebelum-dan-sesudah-normalisasi)

[Gambar 2.4.4 Tipe Data Dataset jabar Setelah Konversi Numerik.	12](#gambar-2.4.4-tipe-data-dataset-jabar-setelah-konversi-numerik.)

[Gambar 2.5.1 Hasil Penggabungan Lima Tahun ke Format Wide (ppo\_jawa\_2021-2025.csv).	12](#gambar-2.5.1-hasil-penggabungan-lima-tahun-ke-format-wide-\(ppo_jawa_2021-2025.csv\).)

[Gambar 2.5.2 Dataset jabar Hasil Penggabungan Tiga Indikator (27 baris, 4 kolom).	13](#gambar-2.5.2-dataset-jabar-hasil-penggabungan-tiga-indikator-\(27-baris,-4-kolom\).)

[Gambar 2.5.3 Pratinjau Kolom Turunan type, gadm\_name, dan ratio pada Dataset jabar.	13](#gambar-2.5.3-pratinjau-kolom-turunan-type,-gadm_name,-dan-ratio-pada-dataset-jabar.)

## 

# **Daftar Tabel** {#daftar-tabel}

---

[Tabel 2.3.1 Identifikasi Tipe Data \- Dataset ppo Tahunan (per file, 10 kolom)	9](#tabel-2.3.1-identifikasi-tipe-data---dataset-ppo-tahunan-\(per-file,-10-kolom\))

[Tabel 2.3.2 Tipe Data Persentase Penduduk Miskin Menurut Kabupaten\_Kota di Jawa Barat, 2025.csv	10](#tabel-2.3.2-tipe-data-persentase_penduduk_miskin_menurut_kabupaten_kota_di_jawa_barat_2025.csv)

[Tabel 2.3.3 Tipe Data Tingkat Pengangguran Terbuka Kabupaten\_Kota, 2025.csv	10](#tabel-2.3.3-tipe-data-tingkat_pengangguran_terbuka_menurut_kabupaten_kota_2025.csv)

[Tabel 2.3.4 Tipe Data Garis Kemiskinan (Rupiah\_Kapita\_Bulan) Menurut Provinsi dan Daerah , 2025.csv	10](#tabel-2.3.4-tipe-data-garis_kemiskinan_menurut_kabupaten_kota_2025.csv)

[Gambar 2.4.1 Dataset ppo Setelah Filter Enam Provinsi Pulau Jawa.	11](#gambar-2.4.1-dataset-ppo-setelah-filter-enam-provinsi-pulau-jawa.)

[Tabel 2.5.1 Normalisasi Kompo	13](#tabel-2.5.1-normalisasi-kompo)

[Tabel 4.1.1 Justifikasi Pemilihan Jenis Grafik	18](#tabel-4.1.1-justifikasi-pemilihan-jenis-grafik)

[Tabel 4.1.2 Tingkat Kedetailan per Grafik	19](#tabel-4.1.2-tingkat-kedetailan-per-grafik)

[Tabel 4.2.1 Palet Warna dan Fungsinya	20](#tabel-4.2.1-palet-warna-dan-fungsinya)

[Tabel 4.2.2 Anotasi per Grafik	21](#tabel-4.2.2-anotasi-per-grafik)

[Tabel 5.1.1 Tools dan Fungsinya	22](#tabel-5.1.1-tools-dan-fungsinya)

[Tabel 5.3.1 Ringkasan Feedback	24](#tabel-5.3.1-ringkasan-feedback)

## 

# **Langkah 1: *Define Purpose and Parameters*** {#langkah-1:-define-purpose-and-parameters}

---

## **1.1 *Topic*** {#1.1-topic}

Topik yang dianalisis adalah pola kemiskinan di Jawa Barat pada 2025, dengan fokus khusus pada hubungan antara tingkat pengangguran terbuka (TPT) dan angka kemiskinan di level kabupaten/kota. Jawa Barat merupakan provinsi berpenduduk terbesar di Indonesia dengan lebih dari 48 juta jiwa.

![][image_jabar]

**Gambar 1.1.1** Peta Provinsi Jawa Barat beserta 27 Kabupaten/Kota.

Angka kemiskinan agregat yang sering dikutip dalam laporan nasional tidak mengungkap dinamika di dalam provinsi itu sendiri. Disparitas antarwilayah dan pola yang tidak sepenuhnya linear antara pengangguran dan kemiskinan mengindikasikan adanya faktor struktural yang perlu ditelusuri lebih dalam melalui data tingkat kabupaten/kota.

Analisis ini menggunakan data BPS untuk tahun 2025 pada level kabupaten/kota serta data tren kemiskinan lima tahun (2021-2025) di enam provinsi Pulau Jawa sebagai konteks komparatif.

## **1.2 *Purpose*** {#1.2-purpose}

Visualisasi ini dibuat untuk mengungkap bahwa status "bekerja" tidak selalu berarti terbebas dari kemiskinan. Di sejumlah kabupaten Jawa Barat yang diindikasikan didominasi sektor pertanian, tingkat pengangguran sangat rendah, namun angka kemiskinan justru termasuk tertinggi se-provinsi. Kondisi ini mengindikasikan bahwa upah yang diperoleh belum mencukupi untuk melampaui garis kemiskinan setempat, dan tidak akan tertangkap apabila hanya membaca angka pengangguran sebagai proksi tunggal kesejahteraan.

Tujuan yang lebih dalam adalah mendorong pembaca untuk mempertanyakan asumsi bahwa pengangguran merupakan satu-satunya penyebab kemiskinan. Kualitas pekerjaan, bukan hanya ketersediaannya, menjadi faktor penentu yang sering luput dari diskusi kebijakan tingkat daerah. Visualisasi ini hadir sebagai argumen berbasis data yang menjembatani gap antara statistik agregat dan realitas struktural di lapangan.

## **1.3 *Users*** {#1.3-users}

Target pengguna adalah **pembaca terdidik** yang mengikuti isu pembangunan dan kesejahteraan daerah. Profil ini mencakup mahasiswa ilmu sosial dan kebijakan publik, jurnalis data, serta pembuat kebijakan di tingkat provinsi maupun kabupaten yang terbiasa membaca laporan BPS dan media seperti Katadata, Tirto, atau *Our World in Data*.

Dari sisi karakteristik kognitif, pengguna diasumsikan memiliki literasi statistik dasar untuk membaca persentase dan tren, tetapi tidak harus memiliki latar belakang analisis data kuantitatif formal. Literasi visual diasumsikan cukup untuk membaca grafik garis, peta koropleth, dan *scatter plot*, tetapi belum tentu familiar dengan *slopegraph* sehingga grafik keempat memerlukan pengantar eksplisit. Pengguna juga diasumsikan membaca dalam konteks satu sesi tunggal (*one-to-one* atau audiens digital global), bukan presentasi tatap muka, sehingga setiap panel harus mandiri tanpa penjelasan verbal tambahan.

Dalam konteks tugas ini, audiens utama adalah sesama mahasiswa dan dosen pengampu yang akan mengevaluasi ketepatan pemilihan visualisasi dan kejelasan narasi.

## **1.4 *Tone*** {#1.4-tone}

Visualisasi ini berada pada kutub **pragmatic** dalam kerangka Kirk (2012), di mana kepentingan utama adalah kejelasan pesan dan efektivitas komunikasi informasi. Dalam ranah *pragmatic* tersebut, gaya yang dipilih bersifat **analitis-persuasif** dengan sudut pandang investigatif, yakni ada sesuatu yang tersembunyi di balik angka yang tampak wajar, dan posisi itu harus terasa melalui cara visual ini disusun.

Nada ini diwujudkan melalui judul yang tegas, anotasi yang bersifat editorial, serta urutan narasi yang membangun ketegangan dari gambaran umum menuju temuan yang mengejutkan. Visualisasi dirancang untuk memancing refleksi tanpa menghakimi wilayah atau kelompok masyarakat tertentu secara eksplisit.

## 

# **Langkah 2: Eksplorasi dan Persiapan Data** {#langkah-2:-eksplorasi-dan-persiapan-data}

---

## **2.1 *Data Acquisition*** {#2.1-data-acquisition}

### **2.1.1 Sumber *Dataset*** {#2.1.1-sumber-dataset}

Data statistik bersumber dari dua portal Badan Pusat Statistik (BPS), yaitu BPS Republik Indonesia di https://www.bps.go.id/ dan BPS Provinsi Jawa Barat di https://jabar.bps.go.id/. Dua kelompok data digunakan dengan cakupan yang berbeda.

Kelompok pertama adalah data tren kemiskinan tingkat provinsi, yaitu lima file tahunan berisi persentase penduduk miskin di seluruh provinsi Indonesia, masing-masing untuk tahun 2021 hingga 2025, dengan nama file `Persentase Penduduk Miskin (P0) Menurut Provinsi dan Daerah, {tahun}.csv`, yang bersumber dari BPS RI. Kelompok kedua adalah data kabupaten/kota Jawa Barat tahun 2025, yaitu tiga file indikator terpisah (persentase penduduk miskin, tingkat pengangguran terbuka/TPT, dan garis kemiskinan per kapita per bulan), yang bersumber dari BPS Jawa Barat.

Data batas wilayah (poligon kabupaten/kota) diperoleh dari repositori GeoJSON komunitas Jawa Barat yang tersedia di https://github.com/hitamcoklat/Jawa-Barat-Geo-JSON/blob/master/Jabar_By_Kab.geojson.

### **2.1.2 Cara Memperoleh** {#2.1.2-cara-memperoleh}

Seluruh file BPS diunduh dalam format CSV melalui mekanisme ekspor tabel pada portal BPS. File indikator jabar menggunakan format yang seragam, yaitu empat baris header non-data di bagian atas, diikuti baris data dengan dua kolom utama (nama wilayah dan nilai indikator).

File ppo tahunan menggunakan format yang lebih kompleks dengan sepuluh kolom, yaitu satu kolom nama provinsi dan sembilan kolom nilai yang terbagi dalam tiga kelompok (perkotaan, perdesaan, dan total/Jumlah), masing-masing berisi nilai Semester 1, Semester 2, dan rata-rata tahunan. File GeoJSON batas wilayah Jawa Barat diunduh langsung dari repositori GitHub dalam format `.geojson` melalui URL *raw* repositori tersebut.

### **2.1.3 Lisensi dan Etika Penggunaan Data** {#2.1.3-lisensi-dan-etika-penggunaan-data}

BPS mempublikasikan seluruh data statistik resmi sebagai data publik yang dapat digunakan untuk keperluan akademik, penelitian, dan non-komersial. Atribusi kepada BPS RI disertakan dalam setiap visualisasi. Data GeoJSON Jawa Barat tersedia sebagai repositori publik di GitHub dan dapat digunakan untuk keperluan akademik dengan atribusi kepada kontributor repositori. Tidak ada isu privasi individual karena seluruh data merupakan agregat tingkat kabupaten/kota atau provinsi.

## **2.2 *Data Examination*** {#2.2-data-examination}

Pemeriksaan dilakukan secara terpisah pada dua kelompok data.

**Dataset ppo tahunan (tren Pulau Jawa)**. Setiap file ppo\_indonesia\_{tahun}.csv berisi data seluruh provinsi Indonesia dengan lima baris header diikuti sepuluh kolom data. Kolom pertama (indeks 0\) berisi nama provinsi, kemudian diikuti tiga kelompok nilai (perkotaan, perdesaan, dan total/Jumlah) yang masing-masing memuat subkolom Semester 1, Semester 2, dan rata-rata tahunan.

*Pipeline* menggunakan kolom indeks 0, 1, dan 2, yaitu nama provinsi serta kemiskinan perkotaan Semester 1 dan Semester 2\. Pemeriksaan mengonfirmasi bahwa nilai Semester 2 perkotaan konsisten tersedia untuk enam provinsi Pulau Jawa di seluruh tahun, kecuali beberapa kasus di tahun tertentu yang hanya tersedia nilai Semester 1\. Nama provinsi menggunakan huruf kapital penuh (misalnya *JAWA BARAT, DKI JAKARTA*) dan memerlukan pencocokkan eksak saat filter.

##### **Gambar 2.2.1** Pratinjau Baris Pertama File ppo\_indonesia\_{tahun}.csv Mentah. {#gambar-2.2.1-pratinjau-baris-pertama-file-ppo_indonesia_{tahun}.csv-mentah.}

**Dataset kabupaten/kota Jawa Barat**. Setiap file indikator berisi satu kolom nama wilayah dan satu kolom nilai. Pemeriksaan mengidentifikasi adanya baris agregat provinsi yang disisipkan di antara baris kabupaten/kota, serta satu baris dengan nilai NaN pada kolom nama wilayah sebagai artefak dari format header BPS. Kedua kondisi ini harus ditangani sebelum penggabungan.

##### **Gambar 2.2.2** Pratinjau File Indikator BPS Kabupaten/Kota Jawa Barat {#gambar-2.2.2-pratinjau-file-indikator-bps-kabupaten/kota-jawa-barat}

**Dataset GeoJSON Jawa Barat.** Pemeriksaan pada properti GeoJSON menemukan bahwa setiap fitur merepresentasikan satu kabupaten atau kota di Jawa Barat dengan atribut nama wilayah yang perlu diselaraskan dengan format nama pada data BPS sebelum penggabungan.

##### **Gambar 2.2.3** Pemeriksaan Nilai Unik Atribut Nama Wilayah pada GeoJSON Jawa Barat {#gambar-2.2.3-pemeriksaan-nilai-unik-atribut-name_1-dan-name_2-pada-geojson-gadm}

## **2.3 *Data Type Identification*** {#2.3-data-type-identification}

Berdasarkan hasil pemeriksaan sebelumnya, berikut identifikasi tipe data untuk setiap kolom beserta tipe yang seharusnya digunakan dalam analisis.

#### **Tabel 2.3.1** Identifikasi Tipe Data \- Dataset ppo Tahunan (per file, 10 kolom) {#tabel-2.3.1-identifikasi-tipe-data---dataset-ppo-tahunan-(per-file,-10-kolom)}

| Indeks | Nama Kolom | Tipe Asli | Digunakan | Keterangan |
| ----- | ----- | ----- | ----- | ----- |
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

####  **Tabel 2.3.2** Tipe Data `Persentase Penduduk Miskin Menurut Kabupaten_Kota di Jawa Barat, 2025.csv` {#tabel-2.3.2-tipe-data-persentase_penduduk_miskin_menurut_kabupaten_kota_di_jawa_barat_2025.csv}

| Indeks | Nama Kolom | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----- | ----- | ----- | ----- | ----- |
| 0 | region | *object* | *Categorical* | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | poverty\_rate | *object* | Float64 | Persentase penduduk miskin, dikonversi ke numerik |

#### **Tabel 2.3.3** Tipe Data `Tingkat Pengangguran Terbuka Kabupaten_Kota, 2025.csv` {#tabel-2.3.3-tipe-data-tingkat_pengangguran_terbuka_menurut_kabupaten_kota_2025.csv}

| Indeks | Nama Kolom | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----- | ----- | ----- | ----- | ----- |
| 0 | region | *object* | *Categorical* | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | unemployment\_rate | *object* | Float64 | TPT dalam persen, dikonversi ke numerik |

#### **Tabel 2.3.4** Tipe Data `Garis Kemiskinan (Rupiah_Kapita_Bulan) Menurut Provinsi dan Daerah , 2025.csv` {#tabel-2.3.4-tipe-data-garis_kemiskinan_menurut_kabupaten_kota_2025.csv}

| Indeks | Nama dalam Pipeline | Tipe Asli | Tipe untuk Analisis | Keterangan |
| ----- | ----- | ----- | ----- | ----- |
| 0 | region | object | Categorical | Nama kabupaten/kota, menjadi *key* penggabungan |
| 1 | poverty\_level | object | Float64 | Garis kemiskinan dalam Rp/kapita/bulan, dikonversi ke numerik |

Ketiga file dibaca dengan header=None karena tidak memiliki baris header standar. Kolom kedua (indeks 1\) diberi nama berbeda sesuai indikatornya dalam *pipeline*, kemudian digabungkan menjadi satu tabel (lihat Bagian 2.5.2).

## **2.4 *Data Cleaning & Quality Improvement*** {#2.4-data-cleaning-&-quality-improvement}

### **2.4.1 Konversi Tipe** {#2.4.1-konversi-tipe}

Dari setiap file tahunan, hanya enam baris yang merepresentasikan provinsi Pulau Jawa yang dipertahankan melalui filter nama eksak (*JAWA BARAT, JAWA TENGAH, JAWA TIMUR, DKI JAKARTA, BANTEN, DI YOGYAKARTA*). Nilai Semester 2 digunakan sebagai acuan utama karena mencerminkan kondisi akhir tahun. Apabila nilai Semester 2 tidak tersedia (*NaN*), nilai Semester 1 digunakan sebagai *fallback*. Perlakuan ini memastikan tidak ada titik data yang hilang pada rentang 2021-2025.

#### **Gambar 2.4.1** Dataset ppo Setelah Filter Enam Provinsi Pulau Jawa. {#gambar-2.4.1-dataset-ppo-setelah-filter-enam-provinsi-pulau-jawa.}

### **2.4.2 Penghapusan Kolom Redundan** {#2.4.2-penghapusan-kolom-redundan}

Baris dengan nilai *NaN* pada kolom *region* dibuang karena merupakan artefak dari format header BPS. Baris yang mengandung kata "Provinsi" pada kolom *region* dibuang karena merepresentasikan agregat provinsi yang tidak relevan untuk analisis level kabupaten/kota.

##### **Gambar 2.4.2** Dataset jabar Setelah Penghapusan Baris Tidak Relevan (27 baris tersisa). {#gambar-2.4.2-dataset-jabar-setelah-penghapusan-baris-tidak-relevan-(27-baris-tersisa).}

### **2.4.3 Penandaan Entitas Agregat Regional** {#2.4.3-penandaan-entitas-agregat-regional}

GeoJSON Jawa Barat menggunakan format nama wilayah yang perlu diselaraskan dengan format nama pada data BPS. Penyesuaian dilakukan melalui peta manual untuk entri yang tidak cocok secara langsung, yaitu *Bandung Barat* dalam BPS berpadanan dengan nama berbeda dalam GeoJSON.

##### **Gambar 2.4.3** Perbandingan Nilai NAME\_2 Sebelum dan Sesudah Normalisasi {#gambar-2.4.3-perbandingan-nilai-name_2-sebelum-dan-sesudah-normalisasi}

### **2.4.4 Penanganan Nilai Kosong** {#2.4.4-penanganan-nilai-kosong}

Kolom nilai numerik (*poverty\_rate, unemployment\_rate, poverty\_level*) dikonversi dari tipe *object* ke *float* menggunakan parameter errors='coerce' sehingga nilai non-numerik yang tersisa otomatis menjadi *NaN* dan dapat diidentifikasi.

##### **Gambar 2.4.4** Tipe Data Dataset jabar Setelah Konversi Numerik. {#gambar-2.4.4-tipe-data-dataset-jabar-setelah-konversi-numerik.}

### **2.5 *Data Transformation for Analysis*** {#2.5-data-transformation-for-analysis}

### **2.5.1 Filter Indeks Relevan** {#2.5.1-filter-indeks-relevan}

Setelah setiap file tahunan diproses secara independen (filter, seleksi semester), kelima dataframe digabungkan secara berurutan menggunakan kolom *Provinsi* sebagai *key* melalui operasi *outer merge.* Hasil akhir adalah tabel dengan enam baris (satu per provinsi Pulau Jawa) dan tujuh kolom, yaitu *Provinsi* dan satu kolom per tahun (2021-2025). Format *wide* ini langsung dapat digunakan untuk pembuatan grafik garis dengan setiap kolom tahun sebagai sumbu-x.

##### **Gambar 2.5.1** Hasil Penggabungan Lima Tahun ke Format Wide (*ppo\_jawa\_2021-2025.csv*). {#gambar-2.5.1-hasil-penggabungan-lima-tahun-ke-format-wide-(ppo_jawa_2021-2025.csv).}

### **2.5.2 Reshape ke Format Wide** {#2.5.2-reshape-ke-format-wide}

Tiga file BPS kabupaten/kota digabungkan menjadi satu tabel menggunakan kolom region sebagai *key* melalui operasi *inner join*. Hasil penggabungan menghasilkan 27 baris kabupaten/kota dengan empat kolom (*region, poverty\_rate, unemployment\_rate, dan poverty\_level*).

##### **Gambar 2.5.2** Dataset jabar Hasil Penggabungan Tiga Indikator (27 baris, 4 kolom). {#gambar-2.5.2-dataset-jabar-hasil-penggabungan-tiga-indikator-(27-baris,-4-kolom).}

### **2.5.3 Penambahan Variabel Turunan** {#2.5.3-penambahan-variabel-turunan}

Kolom type ditambahkan untuk membedakan Kota dan Kabupaten berdasarkan prefiks "Kota " pada nama wilayah. Kolom *gadm\_name* ditambahkan sebagai nama wilayah yang disesuaikan dengan format GADM untuk digunakan sebagai *key* penggabungan dengan GeoJSON. Kolom *ratio* dihitung sebagai *poverty\_rate* dibagi *unemployment\_rate*, yang mengekspresikan seberapa besar angka kemiskinan relatif terhadap tingkat pengangguran di setiap wilayah.

##### **Gambar 2.5.3** Pratinjau Kolom Turunan type, gadm\_name, dan ratio pada Dataset jabar. {#gambar-2.5.3-pratinjau-kolom-turunan-type,-gadm_name,-dan-ratio-pada-dataset-jabar.}

### **2.5.4 Normalisasi Komponen HDI** {#2.5.4-normalisasi-komponen-hdi}

Berdasarkan kolom *ratio*, enam wilayah dengan pola paling ekstrem dipilih sebagai subyek analisis mendalam. Tiga wilayah dengan rasio tertinggi (*ANOMALI\_HIGH*) merepresentasikan kondisi kemiskinan tinggi meskipun pengangguran sangat rendah, sedangkan tiga wilayah dengan rasio terendah (*ANOMALI\_LOW*) merepresentasikan kondisi sebaliknya. Majalengka dikecualikan dari *ANOMALI\_HIGH* karena garis kemiskinannya berada di atas median provinsi, sehingga tidak konsisten dengan narasi yang dibangun. Wilayah anomali yang terpilih adalah sebagai berikut.

#### **Tabel 2.5.1** Normalisasi Kompo {#tabel-2.5.1-normalisasi-kompo}

| Wilayah | Tingkat Pengangguran Terbuka (%) | Tingkat Kemiskinan (%) | GK (Rp/kap/bln) | Rasio | Kelompok |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Pangandaran | 1,91 | 8,03 | 486.285 | 4,20 | Tinggi |
| Tasikmalaya | 3,69 | 10,15 | 413.178 | 2,75 | Tinggi |
| Ciamis | 4,08 | 7,19 | 483.644 | 1,76 | Tinggi |
| Kota Depok | 6,52 | 2,31 | 884.633 | 0,35 | Rendah |
| Kota Cimahi | 8,75 | 4,20 | 642.016 | 0,48 | Rendah |
| Bekasi | 8,78 | 4,36 | 698.154 | 0,50 | Rendah |

#### 

### **2.5.5 Penghitungan Peringkat** {#2.5.5-penghitungan-peringkat}

Kolom peringkat dihitung dari urutan setiap wilayah di antara 27 kabupaten/kota Jawa Barat menggunakan DataFrame.rank(method='min'). Kolom *tpt\_rank* menyatakan peringkat TPT (1 \= TPT terendah) dan kolom *gk\_rank* menyatakan peringkat garis kemiskinan (1 \= garis kemiskinan terendah), keduanya dalam skala bilangan bulat 1-27.

**Gambar 2.5.5** Peringkat TPT dan Garis Kemiskinan untuk Enam Wilayah Anomali.

### **2.6 *Data Consolidation*** {#2.6-data-consolidation}

Seluruh hasil pembersihan dan transformasi disimpan dalam dua file bersih di direktori data/clean/ melalui proses yang sepenuhnya terotomasi dalam *notebook*. Kedua pipeline berjalan pada bagian Persiapan Data sebelum visualisasi dijalankan, sehingga tidak diperlukan file bersih yang disiapkan secara manual di luar *notebook*. File *ppo\_jawa\_2021-2025.csv* dihasilkan dari penggabungan lima file tahunan mentah, sedangkan *jabar\_2025.csv* dihasilkan dari penggabungan tiga file indikator mentah Jawa Barat.

**Tabel 2.6.1** Dataset Final

| File | Baris | Kolom | Keterangan |
| ----- | ----- | ----- | ----- |
| *jabar\_2025.csv* | 27 | region, poverty\_rate, unemployment\_rate, poverty\_level | Kabupaten/kota Jawa Barat 2025 |
| *ppo\_jawa\_2021-2025.csv* | 6 | Provinsi, 2021-2025 | Tren provinsi Pulau Jawa |

## 

# **Langkah 3: Formulasi Pertanyaan dan Fokus Editorial** {#langkah-3:-formulasi-pertanyaan-dan-fokus-editorial}

---

## **3.1 *Analytical Question*** {#3.1-analytical-question}

Mengapa korelasi antara tingkat pengangguran terbuka dan angka kemiskinan di kabupaten/kota Jawa Barat bersifat negatif dan lemah? Wilayah mana yang membentuk anomali paling ekstrem, dan apakah perbedaan garis kemiskinan antar daerah menjadi faktor yang menjelaskan anomali tersebut?

## **3.2. *Editorial Focus*** {#3.2.-editorial-focus}

Di sejumlah kabupaten pertanian Jawa Barat, hampir semua orang bekerja, namun tetap miskin. Upah sektor pertanian berada di bawah garis kemiskinan daerah itu sendiri. Kondisi ini tidak tertangkap apabila hanya membaca angka pengangguran sebagai proksi kesejahteraan.

Pesan ini dibangun dari data BPS yang tersedia secara publik, dan tidak memerlukan asumsi di luar yang dapat diverifikasi langsung dari angka yang ada.

## **3.3 *Reasoning*** {#3.3-reasoning}

Pendekatan yang digunakan adalah ***inductive reasoning***, yakni observasi terhadap enam wilayah anomali spesifik membentuk dasar untuk menarik kesimpulan yang lebih luas tentang karakteristik struktural kemiskinan di kawasan pertanian Jawa Barat. Pola yang ditemukan pada kelompok kecil wilayah ini, yaitu bahwa garis kemiskinan rendah di kawasan pertanian mengindikasikan upah yang bahkan lebih rendah dari standar subsisten yang rendah sekalipun, digunakan untuk mendukung argumen tentang kualitas upah sebagai determinan kemiskinan.

## **3.4 *Narrative*** {#3.4-narrative}

Jenis cerita data yang dibangun adalah narasi ***anomaly-driven*** yang bersifat *author-driven*. Mengacu pada Segel dan Heer (2010), posisi ini berada di ujung author-driven dari spektrum narasi, di mana alur membawa audiens dari konteks yang familiar menuju temuan yang mengejutkan, kemudian menuju penjelasan mekanistik.

Urutan narasinya adalah sebagai berikut. Pertama, audiens melihat Jawa Barat dalam konteks Pulau Jawa secara keseluruhan sehingga tidak ada kekhawatiran tentang kondisi provinsi secara umum. Kedua, sebaran spasial memperlihatkan bahwa disparitas internal provinsi jauh lebih besar dari angka agregat. Ketiga, korelasi negatif antara pengangguran dan kemiskinan memunculkan pertanyaan yang belum terjawab. Keempat, analisis garis kemiskinan memberikan jawaban parsial, yaitu di kawasan pertanian murah, upah bahkan lebih rendah dari standar subsisten yang rendah.

## **3.5 *Genre*** {#3.5-genre}

Visualisasi ini termasuk dalam kategori ***explanatory visualization***. Pembuat memiliki satu argumen spesifik yang ingin disampaikan dan seluruh elemen visual dirancang untuk mendukung penyampaian argumen tersebut secara berurutan. Audiens tidak diharapkan menemukan *insight*\-nya sendiri, melainkan diantar untuk memahami dan memverifikasi argumen yang sudah dibangun.

Dalam kerangka Segel dan Heer (2010), format fisik yang digunakan adalah *partitioned poster* dengan elemen *magazine-style*, yaitu empat panel yang masing-masing mandiri, namun bersama-sama membentuk satu narasi kohesif.

## **3.6 *Narrative Tactics*** {#3.6-narrative-tactics}

### **3.6.1 Urutan Informasi** {#3.6.1-urutan-informasi}

Narasi mengikuti struktur *linear* dari makro ke mikro, dengan setiap grafik mengemban peran naratif yang berbeda.

| Grafik | Peran dalam Narasi |
| ----- | ----- |
| G1 - Tren Pulau Jawa | Menetapkan konteks provinsi di Pulau Jawa agar audiens memiliki gambaran umum sebelum masuk ke analisis spesifik Jawa Barat. |
| G2 - Peta Jawa Barat | Memperlihatkan disparitas internal Jawa Barat secara spasial sehingga audiens melihat bahwa angka agregat provinsi menyembunyikan ketimpangan antarwilayah. |
| G3 - Korelasi | Memunculkan anomali melalui korelasi pengangguran-kemiskinan yang berlawanan dengan intuisi umum, membuka pertanyaan yang belum terjawab. |
| G4 - Anomali | Menguji satu hipotesis penjelasan melalui perbandingan peringkat TPT dan garis kemiskinan, lalu menyimpulkan kondisi struktural yang menjadi akar masalah. |

### **3.6.2 Fokus Perhatian** {#3.6.2-fokus-perhatian}

| Grafik | Taktik Fokus Perhatian | Prinsip Desain |
| ----- | ----- | ----- |
| G1 - Tren Pulau Jawa | Jawa Barat diberi warna merah (\#E63946), sementara lima provinsi konteks ditampilkan abu-abu (\#888888). Label nama langsung di ujung setiap garis. | *Similarity* (Gestalt), yaitu elemen warna sama dipersepsikan sebagai kelompok sehingga pembaca langsung mengasosiasikan merah dengan fokus narasi tanpa membaca legenda terpisah. |
| G2 - Peta Jawa Barat | Warna sekuensial *Reds* mengkodekan intensitas kemiskinan, sedangkan nomor urut di sentroid setiap poligon menggantikan label teks. | *Figure-ground*, yaitu wilayah dengan kemiskinan tinggi (merah pekat) tampil sebagai figur di atas latar wilayah terang. |
| G3 - Korelasi | Kabupaten diberi merah kategori (\#C0392B), Kota diberi biru gelap (\#1A6B8A), berbeda dari merah-hijau Grafik 4. Label hanya untuk enam wilayah anomali. | *Figure-ground*, yaitu titik anomali berlabel tampil sebagai figur di atas latar titik-titik konteks yang tidak berlabel, sementara pemisahan warna dari G4 mencegah kebingungan semantik lintas panel. |
| G4 - *Slopegraph* | Kelompok kemiskinan tinggi diberi merah (\#E63946), kemiskinan rendah diberi hijau-teal (\#2A9D8F), konsisten dengan G1. | *Similarity*, yaitu warna sama lintas panel memperkuat asosiasi semantik tanpa memerlukan legenda berulang. |

### **3.6.3 Highlight Insight Utama** {#3.6.3-highlight-insight-utama}

*Insight* yang diharapkan tersampaikan adalah bahwa di kelompok anomali tinggi (Pangandaran, Tasikmalaya, Ciamis), garis kemiskinan berada di kisaran bawah hingga menengah, namun kemiskinan tetap tinggi. Ini berarti bukan biaya hidup yang menyebabkan anomali, melainkan upah pertanian yang tidak mencukupi bahkan untuk memenuhi standar subsisten yang relatif rendah. Di kelompok anomali rendah (Kota Depok, Kota Cimahi, Bekasi), garis kemiskinan sangat tinggi, namun kemiskinan sangat rendah, mengonfirmasi bahwa pendapatan formal di kawasan urban melampaui standar biaya hidup yang mahal sekalipun.

# 

# **Langkah 4: Konsep Desain** {#langkah-4:-konsep-desain}

---

## **4.1 *Data Representation*** {#4.1-data-representation}

### **4.1.1 Pemilihan Metode dan Jenis Grafik** {#4.1.1-pemilihan-metode-dan-jenis-grafik}

Setiap grafik dipilih berdasarkan tujuan komunikasi primernya sesuai taksonomi Kirk (2012) Bab 5, dengan mempertimbangkan sifat data, jumlah variabel, dan tingkat akurasi yang dibutuhkan audiens. 

#### **Tabel 4.1.1** Justifikasi Pemilihan Jenis Grafik {#tabel-4.1.1-justifikasi-pemilihan-jenis-grafik}

| Grafik | Metode (Kirk 2012\) | Jenis Grafik | Variabel Data | Variabel Visual | Justifikasi |
| ----- | ----- | ----- | ----- | ----- | ----- |
| G1: Tren Pulau Jawa | *Showing changes over time* | *Line chart* | 1 temporal (tahun 2021-2025), 1 kuantitatif-rasio (% kemiskinan), 6 kategorikal-nominal (provinsi) | Posisi-x (waktu), posisi-y (magnitudo), warna-hue (6 provinsi), kemiringan garis | Perubahan temporal paling akurat dikodekan melalui posisi pada sumbu vertikal bersama. Enam seri dapat dibedakan dengan warna tanpa mengorbankan keterbacaan. |
| G2: Peta Jawa Barat | *Mapping geo-spatial data* | Koropleth | 2 kuantitatif-interval (koordinat geografis), 1 kuantitatif-rasio (% kemiskinan), 1 kategorikal (27 wilayah) | Posisi (substrat geografis), warna-saturation/lightness (skala sekuensial *Reds*) | Distribusi spasial memerlukan substrat geografis. Warna sekuensial mengkodekan satu variabel kuantitatif sesuai hierarki akurasi MacKinlay. |
| G3: Korelasi | *Plotting connections and relationships* | *Scatter plot* | 2 kuantitatif-rasio (TPT × kemiskinan), 1 kategorikal-nominal (Kota/Kabupaten) | Posisi-x dan posisi-y (2D Cartesian), warna-hue (kategori biner), kemiringan garis regresi | Dua variabel kuantitatif dipetakan pada dua sumbu posisi, encoding paling akurat menurut hierarki MacKinlay. Garis regresi per kelompok memperlihatkan arah korelasi. |
| G4: Anomali | *Comparing categorical values* | *Slopegraph* | 1 kategorikal-nominal (6 wilayah anomali), 2 kuantitatif-ordinal (tpt\_rank 1-27, gk\_rank 1-27) | Posisi pada dua sumbu paralel, koneksi/kemiringan garis, warna-hue (kelompok biner) | Dua metrik per wilayah pada sumbu vertikal bersama memungkinkan perbandingan langsung. Kirk (2012) secara eksplisit mendefinisikan *slopegraph* sebagai pilihan tepat untuk menampilkan perbandingan dua metrik per kategori. Kemiringan garis langsung memperlihatkan arah dan besar perbedaan. |

Grafik dengan dua sumbu-y *(dual y-axis)* tidak digunakan karena tidak termuat dalam taksonomi Kirk dan menurunkan akurasi komparasi yang seharusnya disediakan oleh posisi sebagai variabel visual primer.

### **4.1.2 Tingkat Kedetailan** {#4.1.2-tingkat-kedetailan}

#### **Tabel 4.1.2** Tingkat Kedetailan per Grafik {#tabel-4.1.2-tingkat-kedetailan-per-grafik}

| Grafik | Cakupan | Label |
| ----- | ----- | ----- |
| G1 \- Tren Pulau Jawa | 6 provinsi, 5 tahun (2021-2025) | Nama provinsi langsung di ujung setiap garis |
| G2 \- Peta Jawa Barat | 27 kabupaten/kota | Nomor urut kemiskinan di sentroid setiap poligon, legenda kartu berisi peringkat, nama, dan nilai untuk seluruh 27 wilayah |
| G3 \- Korelasi | 27 kabupaten/kota | Nama hanya untuk 6 wilayah anomali |
| G4 \- Anomali | 6 wilayah anomali | Nama wilayah di sisi kiri *slopegraph*, legenda dua warna, dan garis median sebagai referensi |

### **4.1.3 Design Metaphor** {#4.1.3-design-metaphor}

Menurut Kirk (2012), *design metaphor* adalah integrasi kualitas visual yang membangun koneksi konseptual antara data, desain, dan topik, misalnya bentuk yang mencerminkan makna subjeknya secara analogis. Dalam visualisasi ini, keputusan pragmatis diambil untuk tidak menggunakan *metaphor* ikonik karena pendekatan tersebut berisiko mengalihkan perhatian dari data itu sendiri pada audiens yang berfokus pada kebijakan.

Sebagai gantinya, *design metaphor* yang digunakan bersifat struktural. Kemiringan garis pada *slopegraph* (Grafik 4) secara metaforis merepresentasikan "jarak" antara peringkat pengangguran dan peringkat garis kemiskinan setiap wilayah, yaitu semakin curam garis, semakin besar ketidaksesuaian antara dua dimensi tersebut. Selain itu, substrat geografis pada koropleth (Grafik 2) mengikat data kemiskinan pada tempat secara harfiah sehingga pola spasial terbaca sebagai realitas fisik, bukan sekadar abstraksi statistik.

Warna merah (\#E63946) dan hijau-teal (\#2A9D8F) berfungsi sebagai *encoding* semantik lintas panel, bukan sebagai *metaphor* ikonik. Konsistensi ini menggantikan kebutuhan legenda berulang dan menguatkan asosiasi merah-perhatian dan teal-kontras sepanjang narasi.

## **4.2. Data Presentation** {#4.2.-data-presentation}

### **4.2.1 Palet Warna** {#4.2.1-palet-warna}

Pemilihan warna mengikuti dua prinsip, yaitu keterbacaan untuk audiens umum dan konsistensi semantik lintas grafik.

#### **Tabel 4.2.1** Palet Warna dan Fungsinya {#tabel-4.2.1-palet-warna-dan-fungsinya}

| Warna | Kode Hex | Fungsi |
| ----- | ----- | ----- |
| Merah | \#E63946 | Jawa Barat (G1), anomali kemiskinan tinggi (G4) |
| Hijau-teal | \#2A9D8F | Anomali kemiskinan rendah (G4) |
| Biru gelap | \#1A6B8A | Kelompok Kota (G3) |
| Merah kategori | \#C0392B | Kelompok Kabupaten (G3) |
| Abu-abu | \#888888 | Lima provinsi konteks Pulau Jawa (G1) |
| Merah sekuensial | Reds (ColorBrewer) | Intensitas kemiskinan pada *choropleth* (G2) |

Warna merah dan hijau-teal dipilih sebagai aksen utama karena memiliki kontras luminansi yang cukup untuk pengguna dengan *deuteranomaly* (defisiensi penglihatan hijau-merah paling umum) apabila dilengkapi dengan perbedaan bentuk dan posisi.

### **4.2.2 Explanatory Annotation** {#4.2.2-explanatory-annotation}

Setiap grafik dilengkapi dengan anotasi yang membantu interpretasi tanpa mengulang isi yang sudah jelas dari visual itu sendiri.

#### **Tabel 4.2.2** Anotasi per Grafik {#tabel-4.2.2-anotasi-per-grafik}

| Grafik | Anotasi |
| ----- | ----- |
| G1 \- Tren Pulau Jawa | Nama provinsi langsung di ujung kanan setiap garis sehingga tidak diperlukan legenda terpisah. |
| G2 \- Peta Jawa Barat | Nama wilayah beserta nilai persentase kemiskinan di sentroid setiap poligon untuk wilayah yang memiliki data. |
| G3 \- Korelasi | Nilai korelasi Pearson (r \= \-0,37) di sudut kanan atas. Nama enam wilayah anomali diberi label langsung pada titik yang bersangkutan. |
| G4 \- Anomali | Nama wilayah di sisi kiri *slopegraph*. Legenda dua warna di bawah grafik, yaitu teal untuk "Pengangguran Tinggi, Kemiskinan Rendah" dan merah untuk "Pengangguran Rendah, Kemiskinan Tinggi". Garis median sebagai referensi horizontal. |

Blok Wawasan *(insight)* dalam format *blockquote* ditempatkan di bawah setiap grafik sebagai anotasi naratif yang merangkum temuan utama dalam bahasa yang dapat dipahami audiens non-teknis.

### **4.2.3 Layout** {#4.2.3-layout}

Visualisasi disajikan dalam format *notebook* Jupyter yang bersifat linear top-down, sesuai urutan narasi yang telah ditetapkan. Setiap panel grafik berdiri sendiri dengan judul, sumbu berlabel, dan blok wawasan sehingga dapat dipahami secara independen sekalipun tanpa membaca panel sebelumnya.

Untuk format poster, tiga panel pertama (G1, G2, G3+G4) disusun secara vertikal. Grafik 3 dan Grafik 4 digabungkan dalam satu baris berdampingan di bawah satu *section header* bersama, diikuti blok *insight* penuh yang merangkum temuan kedua grafik secara terintegrasi. *Footer* memuat sumber data dan nama anggota kelompok.

Tata letak ini menerapkan prinsip *proximity* (Gestalt), yaitu elemen-elemen yang berdekatan dipersepsikan sebagai satu unit sehingga grafik dan blok *insight* di bawahnya terbaca sebagai satu kesatuan argumentatif. Prinsip *continuity* mendukung pembacaan linear dari atas ke bawah mengikuti alur narasi makro ke mikro. Penempatan G3 dan G4 berdampingan memanfaatkan prinsip *similarity* sehingga audiens langsung memahami keduanya sebagai analisis komplementer dalam satu pertanyaan yang sama.

# **Langkah 5: Konstruksi dan Evaluasi** {#langkah-5:-konstruksi-dan-evaluasi}

### ---

## **5.1 *Tools yang Digunakan*** {#5.1-tools-yang-digunakan}

#### **Tabel 5.1.1** *Tools* dan Fungsinya {#tabel-5.1.1-tools-dan-fungsinya}

| *Tool* | Versi | Fungsi |
| ----- | ----- | ----- |
| Python | 3.13 | Bahasa pemrograman utama untuk seluruh *pipeline* |
| pandas | \- | Pembacaan, pembersihan, transformasi, dan penggabungan data |
| geopandas | \- | Pembacaan GeoJSON GADM dan *rendering* koropleth |
| matplotlib | \- | Konstruksi seluruh grafik (G1-G4) |
| scipy.stats | \- | Perhitungan korelasi Pearson dan regresi linier per kelompok |
| Jupyter Notebook | \- | Dokumentasi *pipeline* |
| Figma | \- |  |

### 

### **5.2 *Evaluasi Visualisasi*** {#5.2-evaluasi-visualisasi}

Evaluasi dilakukan berdasarkan kerangka "Things to do Before Launching" dari materi perkuliahan.

### **5.2.1 *Functional Accuracy*** {#5.2.1-functional-accuracy}

Visualisasi ini bersifat statis sehingga tidak terdapat komponen interaktif yang perlu diverifikasi. Seluruh output berupa gambar PNG yang dihasilkan dari *notebook* dan ditampilkan dalam poster HTML. Tidak ada fungsi yang perlu diuji karena tidak ada elemen yang merespons interaksi pengguna.

### **5.2.2 *Data & Statistical Accuracy*** {#5.2.2-data-&-statistical-accuracy}

Nilai korelasi Pearson (r \= \-0,37) dihitung menggunakan *scipy.stats.pearsonr* dari seluruh 27 wilayah. Garis regresi pada Grafik 3 dihitung secara terpisah untuk kelompok Kota dan Kabupaten menggunakan scipy.stats.linregress. Peringkat pada Grafik 4 dihitung menggunakan DataFrame.rank(method='min') dari pandas, yang menghasilkan bilangan bulat 1-27 secara langsung. Tidak ada data *outlier* yang dibuang karena keenam wilayah anomali merupakan observasi valid yang justru menjadi subjek analisis.

### **5.2.3 *Visual Inference*** {#5.2.3-visual-inference}

| Grafik | Aspek *Visual Inference* |
| ----- | ----- |
| G1, G3 | Sumbu-y tidak dipotong dari nilai bukan nol untuk mencegah distorsi persepsi besar perubahan relatif. |
| G2 | *Choropleth* menggunakan skala warna sekuensial yang tidak membalik arah persepsi sehingga lebih merah berarti lebih tinggi dan lebih perlu diperhatikan. |
| G4 | Skala peringkat 1-27 seragam pada sumbu-y sehingga kemiringan garis dapat dibandingkan secara langsung antar wilayah tanpa distorsi skala. |

### **5.2.4 *Formatting Accuracy*** {#5.2.4-formatting-accuracy}

Ukuran *font* konsisten di seluruh grafik (judul 13-14pt, label sumbu 11pt, anotasi 8-9pt). Warna merah \#E63946 digunakan secara konsisten sebagai aksen utama di seluruh grafik. *Spines* dihilangkan pada semua grafik untuk mengurangi *chartjunk*. Gridlines menggunakan gaya *dotted* (:) dengan transparansi 20-30%.

### **5.2.5 *Annotation Accuracy*** {#5.2.5-annotation-accuracy}

Judul setiap grafik mencantumkan nama wilayah, metrik, dan tahun secara eksplisit. Label sumbu dilengkapi satuan (% untuk persentase, Rp untuk garis kemiskinan apabila relevan). Blok wawasan ditulis dalam bahasa Indonesia yang dapat dipahami audiens umum.

## **5.3 *Feedback Pengguna*** {#5.3-feedback-pengguna}

Kuesioner terdiri dari tiga bagian penilaian keseluruhan poster dan empat bagian per grafik, masing-masing menggunakan skala 1-5.

**Penilaian Keseluruhan Poster**

1. Desain dan tata letak keseluruhan poster (1-5)
2. Keterbacaan teks dan judul (1-5)
3. Kesinambungan cerita atau narasi data (1-5)

**Penilaian Per Grafik (diulang untuk G1, G2, G3, dan G4)**

4. Kemudahan memahami informasi dari grafik (1-5)
5. Kesesuaian jenis grafik dengan data yang ditampilkan (1-5)
6. Alasan penilaian (teks bebas, termasuk pilihan kategori masalah)
7. Insight yang Anda dapatkan dari grafik, yaitu poin utama yang berhasil ditangkap (teks bebas)
8. Saran perbaikan spesifik untuk grafik tersebut (teks bebas)

#### **Tabel 5.3.1** Ringkasan Feedback {#tabel-5.3.1-ringkasan-feedback}

| Responden | Grafik Paling Jelas | Grafik Paling Membingungkan | Pesan Utama yang Ditangkap | Saran |
| ----- | ----- | ----- | ----- | ----- |
| R1 - Leon | G1, G2 | G3 (perlu beberapa saat untuk dimengerti) | Hubungan TPT dan kemiskinan di Jawa Barat | Kurangi elemen visual G1 agar garis tidak tumpang tindih. Pastikan warna G2 tidak menutupi teks angka pada peta. |
| R2 - Daniel Pedrosa Wu | G2 (peta langsung terbaca) | G4 (kurang memahami keseluruhan grafik) | Kemiskinan menurun secara umum. Selatan-timur Jawa Barat paling miskin. Korelasi TPT-kemiskinan bersifat terbalik. | Tujuan garis regresi pada G3 kurang eksplisit. G4 perlu pengantar konsep yang lebih jelas. |
| R3 - Reza Ahmad Syarif | G3 (insight korelasi terbalik tersampaikan dengan baik) | Tidak ada (semua grafik dinilai sangat jelas) | Lima tahun kemiskinan cenderung turun. Ada pemisahan wilayah ekonomi yang jelas. Semakin rendah pengangguran justru semakin tinggi kemiskinan. Daerah urban berada di peringkat atas garis kemiskinan. | Tidak ada saran perbaikan. |
| R4 - Krystle | G2 (distribusi kemiskinan antarwilayah terbaca) | G4 (grafik perlu beberapa saat untuk dipahami) | Kemiskinan di Pulau Jawa turun 2021-2025. Enam wilayah mengalami kesenjangan ekstrem antara TPT dan kemiskinan. | Tambahkan kalimat pengantar yang lebih eksplisit sebelum G4. |
| R5 - Richard | G2, G3 | G4 (rating terendah, definisi peringkat tidak intuitif pada versi lama) | Kemiskinan tidak merata antarwilayah. Makin tinggi pengangguran justru makin rendah kemiskinan. | Perbesar teks untuk keterbacaan di perangkat mobile. G4 versi peringkat lebih intuitif daripada versi persentil sebelumnya. |
| R6 - Justin | G3, G4 | G1, G3 | Kemiskinan Jawa Barat menurun. Terdapat korelasi kemiskinan dan pengangguran antarwilayah. | Perbesar angka nomor wilayah G2. Tambahkan keterangan tujuan garis regresi pada G3. |

### 

## **5.4 *Refleksi*** {#5.4-refleksi}

**Apakah tujuan tercapai?**

Secara umum, tujuan tercapai. Lima dari enam responden mampu menangkap pesan utama tentang paradoks kemiskinan-pengangguran di Jawa Barat tanpa penjelasan verbal tambahan. Grafik 1 dan Grafik 2 dinilai paling mudah dipahami oleh seluruh responden. Grafik 3 berhasil menyampaikan temuan korelasi negatif kepada mayoritas responden, termasuk beberapa yang mengungkapkan bahwa *insight*-nya terasa "menarik" dan "tidak terduga".

**Apakah *insight* tersampaikan?**

*Insight* utama berhasil tersampaikan kepada sebagian besar responden. Seluruh responden memahami bahwa kemiskinan menurun selama 2021-2025 dan bahwa kemiskinan di Jawa Barat terkonsentrasi di selatan-timur. Tiga responden secara eksplisit menangkap paradoks korelasi negatif TPT-kemiskinan. Grafik 4 masih menjadi hambatan bagi dua responden yang belum sepenuhnya memahami implikasi kemiringan garis.

**Apa kekurangan visualisasi?**

Berdasarkan evaluasi internal dan umpan balik responden, beberapa kekurangan yang teridentifikasi adalah sebagai berikut. Pertama, *slopegraph* (Grafik 4) memerlukan tingkat literasi visualisasi yang lebih tinggi dibandingkan grafik lain sehingga beberapa responden memerlukan waktu lebih lama untuk memahaminya meskipun konsep persentil sudah diganti dengan peringkat. Kedua, tujuan garis regresi pada Grafik 3 tidak selalu tersampaikan secara intuitif kepada responden yang belum familiar dengan visualisasi statistik. Ketiga, keterbacaan di perangkat *mobile* masih menjadi kendala terutama untuk teks berukuran kecil pada Grafik 2. Keempat, analisis saat ini terbatas pada satu titik waktu (2025) dan tidak dapat menelusuri apakah kondisi anomali ini bersifat persisten atau berubah sepanjang waktu.

# **Daftar Pustaka** {#daftar-pustaka}

---

1. Kirk, A. (2012). Data Visualization: A Successful Design Process. Packt Publishing.

2. Segel, E., & Heer, J. (2010). Narrative visualization: Telling stories with data. *IEEE Transactions on Visualization and Computer Graphics*, *16*(6), 1139–1148. [https://doi.org/10.1109/TVCG.2010.179](https://doi.org/10.1109/TVCG.2010.179)

3. Badan Pusat Statistik Jawa Barat. (2025). Persentase Penduduk Miskin Menurut Kabupaten/Kota di Jawa Barat. BPS Jawa Barat. [https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html](https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html)

4. Badan Pusat Statistik Jawa Barat. (2025). Tingkat Pengangguran Terbuka Menurut Kabupaten/Kota di Jawa Barat. BPS Jawa Barat. [https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html](https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html)

5. Badan Pusat Statistik. (2025). Garis Kemiskinan (Rupiah/Kapita/Bulan) Menurut Provinsi dan Daerah. BPS RI. [https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html](https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html)

6. Badan Pusat Statistik. (2021-2025). Persentase Penduduk Miskin (P0) Menurut Provinsi dan Daerah. BPS RI. [https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html](https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html)

7. hitamcoklat. (n.d.). *Jawa Barat GeoJSON - Jabar\_By\_Kab.geojson*. GitHub. https://github.com/hitamcoklat/Jawa-Barat-Geo-JSON/blob/master/Jabar\_By\_Kab.geojson

# **Lampiran** {#lampiran}

---

1. Pranala Data Sebelum Pemrosesan:

Persentase Penduduk Miskin Kabupaten/Kota Jawa Barat: [https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html](https://jabar.bps.go.id/id/statistics-table/2/OTE5IzI=/persentase-penduduk-miskin-menurut-kabupaten-kota-di-jawa-barat.html)

TPT Kabupaten/Kota Jawa Barat: [https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html](https://jabar.bps.go.id/id/statistics-table/2/Nzg4IzI=/tingkat-pengangguran-terbuka-menurut-kabupaten-kota.html)

Garis Kemiskinan Menurut Provinsi dan Daerah: [https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html](https://www.bps.go.id/id/statistics-table/2/MTk1IzI=/garis-kemiskinan-rupiah-kapita-bulan-menurut-provinsi-dan-daerah-.html)

Persentase Penduduk Miskin Menurut Provinsi (tren 2021-2025): [https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html](https://www.bps.go.id/id/statistics-table/2/MTkyIzI=/persentase-penduduk-miskin--p0--menurut-provinsi-dan-daerah.html)

2. Pranala Data Sesudah Pemrosesan:

[https://drive.google.com/file/d/1yXal5H3r2gRJq6a1Z0BgYu-CwpAEql69/view?usp=sharing](https://drive.google.com/file/d/1yXal5H3r2gRJq6a1Z0BgYu-CwpAEql69/view?usp=sharing) 

3. Pranala Poster: 

4. Notebook Pemrosesan dan Visualisasi:

## 

# **Pembagian Tugas** {#pembagian-tugas}

---

| NIM | Nama Anggota | Tanggung Jawab | Deskripsi Tugas |
| :---: | :---: | :---: | :---: |
| 13523004 | Razi Rachman Widyadhana | Langkah 2 & Langkah 4 | Pengolahan data, *pipeline* notebook, konstruksi grafik, dan *layout poster*. |
| 13523006 | William Andrian Dharma T | Langkah 1 | Melakukan Data Cleaning, Transformation, dan Consolidation termasuk normalisasi GADM. |
| 13523086 | Bob Kunanda | Langkah 2 & Langkah 5 | Merumuskan *Purpose and Parameters* dan Evaluasi. |
| 13523103 | Steven Owen Liauw | Langkah 3 | Menyusun *Analytical Question, Editorial Focus, Reasoning, dan Narrative.* |
| 13523109 | Haegen Quinston | Langkah 4 | Merancang *Data Representation, Data Presentation,* dan menyusun Daftar Pustaka. |

