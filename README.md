# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal luas karena telah menghasilkan lulusan-lulusan berkualitas. Meskipun memiliki reputasi yang baik, institusi ini menghadapi tantangan serius terkait tingginya angka siswa yang tidak menyelesaikan studi atau dropout. Fenomena ini tidak hanya berdampak pada citra institusi, tetapi juga menghambat upaya dalam mencetak generasi terdidik secara optimal.

Sebagai respons terhadap permasalahan tersebut, diperlukan upaya preventif untuk mendeteksi siswa yang berpotensi mengalami dropout sedini mungkin. Dengan bantuan analisis data, potensi ini dapat diprediksi sehingga pihak institusi dapat memberikan intervensi atau bimbingan yang tepat kepada siswa yang membutuhkan.

### Permasalahan Bisnis
Masalah penting yang ingin diatasi dalam proyek ini meliputi:
1. Jaya Jaya Institut menghadapi masalah serius terkait tingginya jumlah siswa yang tidak menyelesaikan pendidikannya. Hal ini berdampak pada reputasi institusi dan efektivitas proses pembelajaran.
2. Saat ini belum tersedia sistem yang mampu mengidentifikasi siswa yang berpotensi dropout sejak dini, sehingga institusi kesulitan memberikan intervensi yang tepat waktu.
3. Pihak institusi belum memiliki dashboard yang dapat menampilkan performa siswa secara menyeluruh, sehingga pengambilan keputusan berbasis data menjadi kurang efektif.

### Cakupan Proyek
Untuk membantu Jaya Jaya Institut dalam mengatasi masalah tersebut, proyek ini akan mencakup:

1. **Data Understanding dan Preprocessing**
Melakukan eksplorasi dan pemahaman terhadap dataset yang telah disediakan dan membersihkan data dari duplikasi, nilai kosong, dan transformasi data agar lebih mudah divisualisasikan.

2. **Analisis Faktor-Faktor Status Siswa**
Mengidentifikasi variabel-variabel yang berkorelasi dengan variabel Status menggunakan korelasi matriks untuk melihat pengaruh variabel lain terhadap Status siswa.

3. **Pembuatan Business Dashboard**
Mendesain dan membangun dashboard yang menampilkan insight penting terkait attrition, seperti total attrition rate, distribusi attrition, indikator karyawan berisiko tinggi untuk keluar. Dashboard dibuat dengan tools Looker Studio.

4. **Pembuatan Solusi Machine Learning**
Membuat solusi machine learning yang dapat membantu Jaya Jaya Institut agar dapat memprediksi status para siswanya dengan mudah dan cepat menggunakan model yang sudah dilatih.

5. **Rekomendasi Strategis**
Memberikan rekomendasi berbasis data untuk strategi menangani tingginya jumlah siswa yang dropout di Jaya Jaya Institut.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment untuk membuka file notebook:
1. Buka terminal atau PowerShell.
2. Buat sebuah folder baru bernama proyek_dashboard_student_performance dengan menjalankan perintah berikut.
    ```
    mkdir proyek_dashboard_student_performance
    ```
3. Pindah ke folder terbaru tersebut menggunakan perintah berikut.
    ```
    cd proyek_dashboard_student_performance
    ```
4. Buat sebuah virtual environment dengan menjalankan perintah berikut.
    ```
    pipenv install
    ```
5. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    pipenv shell
    ```
6. Instal semua library yang dibutuhkan dari requirements.txt menggunakan perintah berikut.
    ```
    pip install -r requirements.txt
    ```
7. Jika belum terinstall jupyter notebook maka install terlebih dahulu menggunakan perintah berikut.
    ```
    pip install jupyter
    ```
8. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```

## Business Dashboard
Dashboard ini dirancang untuk memberikan gambaran menyeluruh mengenai data peforma siswa untuk mengidentifikasi faktor-faktor apa saja yang menyebabkan tingginya dropout pada siswa. Dashboard ini mencakup data keseluruhan siswa baik jumlah siswa, performa siswa, dan juga status siswa saat ini.

Berikut link dashboard untuk melihat lebih detail : https://lookerstudio.google.com/reporting/27baa726-65ca-4ccc-824b-57ce49eab18f

![alt text](https://github.com/alynra/student-performance/blob/main/alynna33-dashboard.png?raw=true)

Berdasarkan data pada dashboard performa siswa dengan status dropout di Jaya Jaya Institut, ditemukan beberapa pola signifikan yang dapat menjadi indikator utama penyebab tingginya tingkat dropout. Sebagian besar siswa dropout diketahui tidak menerima beasiswa, yang menunjukkan bahwa keterbatasan dukungan finansial dapat menjadi faktor krusial dalam keberlangsungan pendidikan mahasiswa. Selain itu, proporsi siswa dengan latar belakang sosial yang rentan, khususnya mereka yang berstatus displaced, juga cukup tinggi, mengindikasikan adanya kebutuhan untuk perhatian dan intervensi khusus bagi kelompok ini.

Dari sisi demografis, dropout paling banyak terjadi pada rentang usia 18 hingga 21 tahun, serta mayoritas berasal dari kelompok single, yang kemungkinan berkaitan dengan kesiapan mental dan emosional dalam menghadapi tekanan akademik. Secara akademis, nilai rata-rata saat masuk (admission grade) dan kualifikasi sebelumnya juga cenderung moderat, memperkuat dugaan bahwa kesiapan akademik yang rendah menjadi salah satu pemicu utama putus studi. Selain itu, jurusan tertentu seperti Manajemen baik kelas reguler maupun malam serta Keperawatan mencatat jumlah dropout tertinggi, yang menunjukkan perlunya evaluasi lebih lanjut terhadap proses pembelajaran, beban studi, atau metode pengajaran di program-program tersebut.

## Menjalankan Sistem Machine Learning
Terdapat prototype machine learning yang sudah dibuat yang dapat melakukan prediksi untuk status mahasiswa berdasarkan data mahasiswa yang diinput. Prototype dapat diakses dengan membuka link berikut.

https://student-performance-simple-predict.streamlit.app/

Penggunaan prototype sangat sederhana, anda hanya perlu memasukkan semua data siswa, setelah memastikan data yang dimasukkan benar, anda dapat klik button predict student status dan hasil predict akan langsung muncul.

## Conclusion

Hasil analisis terhadap data siswa dropout menunjukkan bahwa tingginya angka putus studi di Jaya Jaya Institut berkorelasi dengan beberapa faktor kritis, seperti tidak adanya bantuan beasiswa, latar belakang sosial yang rentan (displaced), kesiapan akademik yang rendah, serta dominasi siswa usia muda yang kemungkinan masih dalam fase penyesuaian terhadap beban studi perguruan tinggi. Ketidakterlibatan dalam program dukungan finansial dan dominasi status sosial tertentu semakin memperkuat perlunya perhatian terhadap aspek non-akademik dalam mencegah dropout. Temuan ini menegaskan bahwa masalah tingginya dropout tidak hanya berdampak pada reputasi institusi dan efektivitas pembelajaran, tetapi juga menunjukkan bahwa selama ini belum tersedia sistem yang secara proaktif mampu mengidentifikasi siswa berisiko sejak dini.

Untuk menjawab tantangan tersebut, Jaya Jaya Institut kini telah memiliki dashboard visual interaktif yang menyajikan data performa siswa secara menyeluruh dan komprehensif. Dashboard ini memungkinkan pihak manajemen untuk melihat distribusi siswa berdasarkan faktor-faktor risiko secara real time, sehingga pengambilan keputusan menjadi lebih tepat sasaran dan berbasis data.

Lebih lanjut, pengembangan model machine learning yang mampu memprediksi status siswa (dropout atau tidak) menjadi capaian strategis yang signifikan. Model ini berfungsi sebagai sistem peringatan dini yang dapat mengidentifikasi siswa dengan risiko tinggi untuk putus studi sejak dini. Dengan demikian, institusi dapat melakukan intervensi yang bersifat preventif dan personal, seperti pemberian konseling, bantuan finansial, atau program pembinaan akademik.

Secara keseluruhan, integrasi antara analisis data, visualisasi dashboard, dan pemodelan prediktif memberikan solusi yang holistik terhadap tiga permasalahan utama Jaya Jaya Institut: tingginya angka dropout, ketiadaan sistem identifikasi risiko secara dini, dan kurangnya pengambilan keputusan berbasis data. Implementasi sistem ini diharapkan dapat meningkatkan efektivitas proses pembelajaran, mempertahankan keberlangsungan studi mahasiswa, serta memperbaiki reputasi institusi secara berkelanjutan.


### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang dapat dilakukan institiut guna menyelesaikan permasalahan mereka.
-	Perluasan program beasiswa & subsidi sosial dengan prioritaskan beasiswa untuk siswa displaced dan buat skema bantuan belajar untuk kelompok berisiko tinggi  
-	Evaluasi kurikulum & beban studi program tertentu seperti melakukan audit akademik pada jurusan dengan tingkat dropout tinggi dan meninjau ulang struktur kuliah malam untuk mengurangi dropout  
-	Kelas khusus atau remedial untuk siswa dengan nilai masuk rendah  
-	Pemantauan berkala melalui dashboard interaktif sebagai bagian dari evaluasi rutin bulanan dan kolaborasikan dengan bagian akademik, keuangan, dan kemahasiswaan

