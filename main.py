import requests, urllib.parse, json, csv

provinsi = 'SUMATERA BARAT'
prov = urllib.parse.quote_plus(provinsi)

bps_total = "https://gis.dukcapil.kemendagri.go.id/arcgis/rest/services/Data_Baru_26092017/MapServer/3/query?f=json&returnIdsOnly=true&returnCountOnly=true&where=(UPPER(giskemendagri.gisadmin.Desa_Tabel_26092017_2.nama_prop_)%20=%20'" + prov + "')&returnGeometry=false&spatialRel=esriSpatialRelIntersects"
total = requests.get(bps_total)
y = json.loads(total.text)

bps_list = "https://gis.dukcapil.kemendagri.go.id/arcgis/rest/services/Data_Baru_26092017/MapServer/3/query?f=json&where=(UPPER(giskemendagri.gisadmin.Desa_Tabel_26092017_2.nama_prop_)%20=%20'" + prov + "')&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=giskemendagri.gisadmin.Desa_Spasial_22092017.objectid%20ASC&resultOffset=0&resultRecordCount=" + str(y['count'])
data_list = requests.get(bps_list)

a = data_list.text.replace("giskemendagri.gisadmin.Desa_Spasial_22092017.", "").replace("giskemendagri.gisadmin.Desa_Tabel_26092017_2.", "")
x = json.loads(a)
data = x['features']

with open("Output__" + provinsi + ".csv", "w", newline='', encoding='utf-8') as outfile:
    f = csv.writer(outfile)
    f.writerow(["kode_desa", "provinsi", "kabupaten", "kecamatan", "kelurahan", "jumlah_penduduk", "jumlah_kk", "luas_wilayah", "kepadatan_penduduk", "perpindahan_penduduk", "jumlah_meninggal", "perubahan_data", "wajib_ktp", "islam", "kristen", "katholik", "hindu", "budha", "konghucu", "kepercayaan", "pria", "wanita", "belum_kawin", "kawin", "cerai_hidup", "cerai_mati", "usia_0_4_th", "usia_5_9_th", "usia_10_14_th", "usia_15_19_th", "usia_20_24_th", "usia_25_29_th", "usia_30_34_th", "usia_35_39_th", "usia_40_44_th", "usia_45_49_th", "usia_50_54_th", "usia_55_59_th", "usia_60_64_th", "usia_65_69_th", "usia_70_74_th", "usia_75_th", "lahir_th_2016", "lahir_kur_th_2016", "lahir_th_2017", "lahir_kur_th_2017", "lahir_th_2018", "lahir_kur_th_2018", "pertumbuhan_penduduk_th_2016", "pertumbuhan_penduduk_th_2017", "pertumbuhan_penduduk_th_2018", "sekolah_3_4_th", "sekolah_5_th", "sekolah_6_11_th", "sekolah_12_14_th", "sekolah_15_17_th", "sekolah_18_22_th", "tdk_blm_sekolah", "belum_tamat_sd", "tamat_sd", "sltp", "slta", "d1_d2", "d3", "d4_s1", "s2", "s3", "gol_a", "gol_b", "gol_ab", "gol_o", "gol_a_plus", "gol_a_neg", "gol_b_plus", "gol_b_neg", "gol_ab_plus", "gol_ab_neg", "gol_o_plus", "gol_o_neg", "gol_tdk_diketahui", "blm_tdk_bekerja", "aparatur_pejabat_negara", "tenaga_pengajar", "wiraswasta", "pertanian_peternakan", "nelayan", "agama_kepercayaan", "pelajar_mahasiswa", "tenaga_kesehatan", "pensiunan", "lainnya", "sumber_data", "jml_rek_wktp"])
    for i in range(0, len(data)):
        per_line = data[i]['attributes']
        f.writerow([per_line['kode_desa_'],per_line['nama_prop_'],per_line['nama_kab_s'],per_line['nama_kec_s'],per_line['nama_kel_s'],per_line['jumlah_pen'],per_line['jumlah_kk'],per_line['luas_wilay'],per_line['kepadatan_'],per_line['perpindaha'],per_line['jumlah_men'],per_line['perubahan_'],per_line['wajib_ktp'],per_line['islam'],per_line['kristen'],per_line['katholik'],per_line['hindu'],per_line['budha'],per_line['konghucu'],per_line['kepercayaa'],per_line['pria'],per_line['wanita'],per_line['belum_kawi'],per_line['kawin'],per_line['cerai_hidu'],per_line['cerai_mati'],per_line['u0'],per_line['u5'],per_line['u10'],per_line['u15'],per_line['u20'],per_line['u25'],per_line['u30'],per_line['u35'],per_line['u40'],per_line['u45'],per_line['u50'],per_line['u55'],per_line['u60'],per_line['u65'],per_line['u70'],per_line['u75'],per_line['lahir_thn1'],per_line['lahir_seb'],per_line['lahir_thn2'],per_line['lahir_seb2'],per_line['lahir_thn3'],per_line['lahir_seb3'],per_line['pertumbuha'],per_line['pertumbuh2'],per_line['pertumbuh3'],per_line['pendidikan'],per_line['pendidika2'],per_line['pendidika3'],per_line['pendidika4'],per_line['pendidika5'],per_line['pendidika6'],per_line['tidak_belu'],per_line['belum_tama'],per_line['tamat_sd'],per_line['sltp'],per_line['slta'],per_line['diploma_i_'],per_line['diploma_ii'],per_line['diploma_iv'],per_line['strata_ii'],per_line['strata_iii'],per_line['a'],per_line['b'],per_line['ab'],per_line['o'],per_line['a_'],per_line['a_2'],per_line['b_'],per_line['b_2'],per_line['ab_'],per_line['ab_2'],per_line['o_'],per_line['o_2'],per_line['tidak_di_k'],per_line['belum_tida'],per_line['aparatur_p'],per_line['tenaga_pen'],per_line['wiraswasta'],per_line['pertanian_'],per_line['nelayan'],per_line['agama_dan_'],per_line['pelajar_ma'],per_line['tenaga_kes'],per_line['pensiunan'],per_line['lainnya'],per_line['generated_'],per_line['jml_rek_wktp']])
    outfile.close()  