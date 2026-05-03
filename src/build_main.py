import json
import sys
from pathlib import Path
from uuid import uuid4

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = Path(__file__).parent / "main.ipynb"
HR  = "---"

def md(source: str) -> dict:
    return {"cell_type": "markdown", "id": uuid4().hex[:8], "metadata": {}, "source": source}

def code(source: str) -> dict:
    return {
        "cell_type": "code", "execution_count": None, "id": uuid4().hex[:8],
        "metadata": {}, "outputs": [], "source": source,
    }

def section(title: str, anchor: str) -> dict:
    return md(f"{HR}\n\n# {title} <a name=\"{anchor}\"></a>\n\n{HR}")

cells = []

# ---------------------------------------------------------------------------
# Banner
# ---------------------------------------------------------------------------
cells.append(md(
    f"{HR}\n\n"
    "# SundaLife\n\n"
    "*Visualisasi Data Kemiskinan Jawa Barat 2021-2025*"
))

cells.append(md(
    f"{HR}\n\n"
    "## Kelompok 01 - IF4061 Visualisasi Data\n\n"
    "- 13523004 - Razi Rachman Widyadhana\n"
    "- 13523006 - William Andrian Dharma T\n"
    "- 13523086 - Bob Kunanda\n"
    "- 13523103 - Steven Owen Liauw\n"
    "- 13523109 - Haegen Quinston"
))

cells.append(md(
    f"{HR}\n\n"
    "## Daftar Isi\n\n"
    "1. [**Pendahuluan**](#1)\n"
    "2. [**Inisialisasi**](#2)\n"
    "3. [**Persiapan Data**](#3)\n"
    "4. [**Transformasi Data**](#4)\n"
    "5. [**Grafik 1: Tren Kemiskinan Pulau Jawa 2021-2025**](#5)\n"
    "6. [**Grafik 2: Peta Sebaran Kemiskinan Jawa Barat**](#6)\n"
    "7. [**Grafik 3: Korelasi Kemiskinan dan Pengangguran**](#7)\n"
    "8. [**Grafik 4: Kota-Kota Anomali**](#8)\n"
))

# ---------------------------------------------------------------------------
# Section 1: Pendahuluan
# ---------------------------------------------------------------------------
cells.append(section("Pendahuluan", "1"))
cells.append(md(
    "Jawa Barat merupakan provinsi dengan jumlah penduduk terbesar di Indonesia, "
    "namun menyimpan disparitas kemiskinan yang signifikan antarwilayah. "
    "Pola kemiskinan di tingkat kabupaten/kota memperlihatkan dinamika yang berbeda "
    "dari gambaran agregat provinsi, dan perlu ditelusuri secara lebih rinci.\n\n"
    "Analisis ini menelusuri empat pertanyaan: bagaimana posisi Jawa Barat dibandingkan "
    "provinsi lain di Pulau Jawa selama 2021-2025, di mana kemiskinan paling terkonsentrasi "
    "di tingkat kabupaten/kota, seberapa kuat hubungan antara kemiskinan dan pengangguran, "
    "serta wilayah mana yang memperlihatkan pola berbeda dari mayoritas."
))

# ---------------------------------------------------------------------------
# Section 2: Inisialisasi
# ---------------------------------------------------------------------------
cells.append(section("Inisialisasi", "2"))
cells.append(md(
    "`geopandas` digunakan untuk membaca batas wilayah dari file GeoJSON GADM 4.1 "
    "dan memplot peta koropleth. Seluruh impor diletakkan dalam satu sel."
))
cells.append(code("# %pip install geopandas --quiet"))
cells.append(code(
    "import os\n"
    "import numpy as np\n"
    "import pandas as pd\n"
    "import geopandas as gpd\n"
    "import matplotlib.pyplot as plt\n"
    "import matplotlib.ticker as ticker\n"
    "from scipy import stats\n\n"
    "%matplotlib inline\n\n"
    "DATA_DIR   = '../data/'\n"
    "RAW_DIR    = DATA_DIR + 'raw/'\n"
    "CLEAN_DIR  = DATA_DIR + 'clean/'\n"
    "OUTPUT_DIR = '../docs/output/'\n"
    "os.makedirs(OUTPUT_DIR, exist_ok=True)\n\n"
    "plt.rcParams.update({\n"
    "    'font.family': 'sans-serif',\n"
    "    'font.sans-serif': ['Arial', 'DejaVu Sans'],\n"
    "    'figure.facecolor': 'none',\n"
    "    'axes.facecolor':   'none',\n"
    "})"
))

# ---------------------------------------------------------------------------
# Section 3: Persiapan Data
# ---------------------------------------------------------------------------
cells.append(section("Persiapan Data", "3"))
cells.append(md(
    "Tahap ini membaca data mentah dari BPS dan menghasilkan dua file bersih di `data/clean/`. "
    "Seluruh logika pembersihan disertakan agar pipeline dapat direproduksi "
    "tanpa bergantung pada file bersih yang sudah tersimpan sebelumnya."
))

cells.append(md(
    "## Tren Kemiskinan Pulau Jawa\n\n"
    "Setiap file tahunan BPS menggunakan format yang seragam: empat baris header, "
    "diikuti kolom nama provinsi, Semester 1, dan Semester 2. Nilai Semester 2 dipakai "
    "sebagai acuan utama, dengan *fallback* ke Semester 1 apabila tidak tersedia."
))
cells.append(code(
    "YEARS = [2021, 2022, 2023, 2024, 2025]\n"
    "JAWA  = [\n"
    "    'JAWA BARAT', 'JAWA TENGAH', 'JAWA TIMUR',\n"
    "    'DKI JAKARTA', 'BANTEN', 'DI YOGYAKARTA',\n"
    "]\n\n"
    "processed = []\n"
    "for year in YEARS:\n"
    "    df = pd.read_csv(RAW_DIR + f'ppo_indonesia_{year}.csv', skiprows=4)\n"
    "    df = df.iloc[:, [0, 1, 2]]\n"
    "    df.columns = ['Provinsi', 'S1', 'S2']\n"
    "    df['Provinsi'] = df['Provinsi'].str.strip()\n"
    "    df = df[df['Provinsi'].isin(JAWA)].copy()\n"
    "    df['S1'] = pd.to_numeric(df['S1'], errors='coerce')\n"
    "    df['S2'] = pd.to_numeric(df['S2'], errors='coerce')\n"
    "    df[str(year)] = df['S2'].fillna(df['S1'])\n"
    "    processed.append(df[['Provinsi', str(year)]])\n\n"
    "ppo_jawa = processed[0]\n"
    "for df in processed[1:]:\n"
    "    ppo_jawa = ppo_jawa.merge(df, on='Provinsi', how='outer')\n\n"
    "ppo_jawa.to_csv(CLEAN_DIR + 'ppo_jawa_2021-2025.csv', index=False, encoding='utf-8')\n"
    "print(ppo_jawa.to_string(index=False))"
))

cells.append(md(
    "## Data Kabupaten/Kota Jawa Barat\n\n"
    "Tiga file BPS untuk 2025 digabungkan menjadi satu tabel berisi persentase penduduk miskin, "
    "tingkat pengangguran terbuka, dan garis kemiskinan per kabupaten/kota. "
    "Baris agregat provinsi dibuang karena analisis berfokus pada level wilayah individual."
))
cells.append(code(
    "def clean_bps(path, col):\n"
    "    df = pd.read_csv(path, header=None).iloc[:, :2]\n"
    "    df.columns = ['region', col]\n"
    "    df['region'] = df['region'].astype(str).str.strip()\n"
    "    df[col] = pd.to_numeric(df[col], errors='coerce')\n"
    "    df = df.dropna(subset=['region', col])\n"
    "    return df[~df['region'].str.contains('Provinsi', na=False)]\n\n"
    "jabar_raw = (\n"
    "    clean_bps(\n"
    "        RAW_DIR + 'Persentase_Penduduk_Miskin_Menurut_Kabupaten_Kota_di_Jawa_Barat_2025.csv',\n"
    "        'poverty_rate',\n"
    "    )\n"
    "    .merge(clean_bps(\n"
    "        RAW_DIR + 'Tingkat_Pengangguran_Terbuka_Menurut_Kabupaten_Kota_2025.csv',\n"
    "        'unemployment_rate',\n"
    "    ), on='region')\n"
    "    .merge(clean_bps(\n"
    "        RAW_DIR + 'Garis_Kemiskinan_Menurut_Kabupaten_Kota_2025.csv',\n"
    "        'poverty_level',\n"
    "    ), on='region')\n"
    ")\n\n"
    "jabar_raw.to_csv(CLEAN_DIR + 'jabar_2025_combined.csv', index=False, encoding='utf-8')\n"
    "print(jabar_raw.to_string(index=False))"
))

# ---------------------------------------------------------------------------
# Section 4: Transformasi Data
# ---------------------------------------------------------------------------
cells.append(section("Transformasi Data", "4"))
cells.append(md(
    "Nama wilayah dinormalisasi dengan menghapus spasi agar sesuai dengan format `NAME_2` "
    "pada GeoJSON GADM. Kolom `type` ditambahkan untuk membedakan Kota dan Kabupaten. "
    "Tiga wilayah memerlukan pemetaan manual karena GADM tidak menyertakan prefiks *Kota* "
    "pada namanya: Cimahi, Depok, dan Banjar."
))
cells.append(code(
    "ppo_jawa = pd.read_csv(CLEAN_DIR + 'ppo_jawa_2021-2025.csv')\n"
    "jabar    = pd.read_csv(CLEAN_DIR + 'jabar_2025_combined.csv')\n\n"
    "jabar = jabar.dropna(subset=['region'])\n"
    "jabar['type'] = np.where(\n"
    "    jabar['region'].str.startswith('Kota ', na=False), 'Kota', 'Kabupaten'\n"
    ")\n\n"
    "GADM_FIX = {'Bandung Barat': 'BandungBarat'}\n"
    "jabar['gadm_name'] = jabar['region'].map(GADM_FIX).fillna(jabar['region'])\n\n"
    "jabar['ratio'] = jabar['poverty_rate'] / jabar['unemployment_rate']\n"
    "ANOMALI_HIGH = (\n"
    "    jabar.nlargest(4, 'ratio')\n"
    "    .query(\"region != 'Majalengka'\")\n"
    "    ['region'].head(3).tolist()\n"
    ")\n"
    "ANOMALI_LOW  = jabar.nsmallest(3, 'ratio')['region'].tolist()\n"
    "ANOMALI_ALL  = ANOMALI_HIGH + ANOMALI_LOW\n\n"
    "print('Rasio tinggi:', ANOMALI_HIGH)\n"
    "print('Rasio rendah:', ANOMALI_LOW)\n"
    "print(jabar[['region', 'type', 'gadm_name', 'poverty_rate',\n"
    "             'unemployment_rate', 'poverty_level', 'ratio']].to_string(index=False))"
))

# ---------------------------------------------------------------------------
# Section 5: Grafik 1 - Line chart
# ---------------------------------------------------------------------------
cells.append(section("Grafik 1: Tren Kemiskinan Pulau Jawa 2021-2025", "5"))
cells.append(md(
    "Grafik garis ini memperlihatkan perkembangan persentase penduduk miskin di enam provinsi "
    "Pulau Jawa dari 2021 hingga 2025. Jawa Barat disorot dengan warna merah dan ketebalan "
    "garis yang lebih besar, sedangkan provinsi lain ditampilkan dalam abu-abu sebagai konteks."
))
cells.append(code(
    "df_plot = ppo_jawa.set_index('Provinsi').T\n"
    "df_plot.index = df_plot.index.astype(int)\n\n"
    "PROV_STYLE = {\n"
    "    'JAWA BARAT'    : ('Jawa Barat',    '#E63946', 2.8, 7, 5),\n"
    "    'DI YOGYAKARTA' : ('DI Yogyakarta', '#888888', 1.4, 4, 2),\n"
    "    'JAWA TENGAH'   : ('Jawa Tengah',   '#888888', 1.4, 4, 2),\n"
    "    'JAWA TIMUR'    : ('Jawa Timur',    '#888888', 1.4, 4, 2),\n"
    "    'BANTEN'        : ('Banten',        '#888888', 1.4, 4, 2),\n"
    "    'DKI JAKARTA'   : ('DKI Jakarta',   '#888888', 1.4, 4, 2),\n"
    "}\n\n"
    "fig, ax = plt.subplots(figsize=(11, 4.5))\n\n"
    "for prov, (label, color, lw, ms, zo) in PROV_STYLE.items():\n"
    "    is_jabar = prov == 'JAWA BARAT'\n"
    "    ax.plot(df_plot.index, df_plot[prov],\n"
    "            color=color, linewidth=lw, marker='o',\n"
    "            markersize=ms, zorder=zo)\n"
    "    ax.text(\n"
    "        df_plot.index[-1] + 0.08, df_plot[prov].iloc[-1],\n"
    "        label, color=color, fontsize=9, va='center',\n"
    "        fontweight='bold' if is_jabar else 'normal',\n"
    "    )\n\n"
    "for ref_y in [4.0, 11.0]:\n"
    "    ax.axhline(ref_y, color='#CCCCCC', linewidth=0.8, linestyle=':', zorder=0)\n"
    "    ax.text(df_plot.index[0] - 0.12, ref_y,\n"
    "            f'{ref_y:.1f}%', fontsize=13, color='#999999', va='center', ha='right')\n\n"
    "for year in df_plot.index:\n"
    "    ax.axvline(year, color='#DDDDDD', linewidth=0.8, linestyle=':', zorder=0)\n\n"
    "ax.set_xlim(df_plot.index[0] - 0.1, df_plot.index[-1] + 0.75)\n"
    "ax.set_ylim(2.8, 11.8)\n"
    "ax.set_xticks(df_plot.index)\n"
    "ax.set_xticklabels([str(y) for y in df_plot.index], fontsize=13, color='#555555')\n"
    "ax.tick_params(axis='x', length=0)\n"
    "ax.tick_params(axis='y', left=False, labelleft=False)\n"
    "ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)\n"
    "plt.tight_layout()\n"
    "plt.savefig(OUTPUT_DIR + 'g1_tren.png', dpi=150, bbox_inches='tight', facecolor='none')\n"
    "plt.show()"
))
cells.append(md(
    "#### Wawasan\n\n"
    "> Secara keseluruhan, seluruh provinsi di Pulau Jawa mencatat penurunan angka kemiskinan "
    "dari 2021 ke 2025, meskipun beberapa provinsi mengalami fluktuasi di tengah periode. "
    "Jawa Tengah dan Jawa Timur bahkan mencatat sedikit kenaikan di tahun 2025, "
    "mengindikasikan bahwa pemulihan pasca 2021 tidak bersifat linier. "
    "Jawa Barat berada di posisi menengah dengan kisaran 6,65-7,52%, "
    "di bawah DI Yogyakarta dan Jawa Tengah yang konsisten di atas 8%, "
    "tetapi lebih tinggi dibandingkan DKI Jakarta dan Banten."
))

# ---------------------------------------------------------------------------
# Section 6: Grafik 2 - Choropleth
# ---------------------------------------------------------------------------
cells.append(section("Grafik 2: Peta Sebaran Kemiskinan Jawa Barat 2025", "6"))
cells.append(md(
    "Peta koropleth ini menampilkan tingkat kemiskinan di setiap kabupaten/kota Jawa Barat "
    "pada 2025. Batas wilayah menggunakan data GADM 4.1 yang dibaca dengan `geopandas`. "
    "Wilayah tanpa padanan data (Pangandaran tidak tercakup dalam GADM 4.1 dan Waduk Cirata "
    "merupakan badan air) ditampilkan dalam abu-abu."
))
cells.append(code(
    "from matplotlib.colors import LinearSegmentedColormap\n\n"
    "gdf = gpd.read_file(CLEAN_DIR + 'gadm41_IDN_2.json')\n"
    "gdf_jabar = gdf[gdf['NAME_1'] == 'JawaBarat'].copy()\n\n"
    "gdf_jabar = gdf_jabar.merge(\n"
    "    jabar[['gadm_name', 'region', 'type', 'poverty_rate']],\n"
    "    left_on='NAME_2', right_on='gadm_name',\n"
    "    how='left',\n"
    ")\n\n"
    "ranked = (\n"
    "    jabar[['gadm_name', 'region', 'poverty_rate']]\n"
    "    .sort_values('poverty_rate', ascending=False)\n"
    "    .reset_index(drop=True)\n"
    ")\n"
    "ranked['num'] = ranked.index + 1\n"
    "gdf_jabar = gdf_jabar.merge(ranked[['gadm_name', 'num']], on='gadm_name', how='left')\n\n"
    "reds_light = LinearSegmentedColormap.from_list(\n"
    "    'Reds_light', plt.cm.Reds(np.linspace(0.05, 0.78, 256))\n"
    ")\n\n"
    "fig, ax_map = plt.subplots(figsize=(18, 8))\n"
    "fig.subplots_adjust(left=0.16, right=0.92, top=0.96, bottom=0.04)\n\n"
    "gdf_jabar.plot(\n"
    "    column='poverty_rate',\n"
    "    cmap=reds_light,\n"
    "    linewidth=0.6,\n"
    "    edgecolor='white',\n"
    "    legend=True,\n"
    "    legend_kwds={'label': 'Kemiskinan (%)', 'orientation': 'vertical', 'shrink': 0.6},\n"
    "    missing_kwds={'color': '#DDDDDD', 'label': 'Tidak ada data'},\n"
    "    ax=ax_map,\n"
    ")\n\n"
    "pos = {}\n"
    "for _, row in gdf_jabar.iterrows():\n"
    "    if pd.notna(row.get('num')):\n"
    "        c = row.geometry.centroid\n"
    "        pos[int(row['num'])] = (c.x, c.y, row.geometry.area)\n\n"
    "NUDGE = {\n"
    "    19: ( 0.025, -0.02),\n"
    "    21: ( 0.15,   0.01),\n"
    "    12: ( 0.1,   -0.1 ),\n"
    "}\n\n"
    "for num, (x, y, _) in pos.items():\n"
    "    dx, dy = NUDGE.get(num, (0, 0))\n"
    "    ax_map.annotate(\n"
    "        str(num), xy=(x + dx, y + dy),\n"
    "        ha='center', va='center',\n"
    "        fontsize=9, fontweight='bold', color='#111111',\n"
    "    )\n\n"
    "ax_map.axis('off')\n\n"
    "lines = [\n"
    "    f\"{int(r['num']):2d}  {r['region']:<18} {r['poverty_rate']:.2f}%\"\n"
    "    for _, r in ranked.iterrows()\n"
    "]\n"
    "fig.text(0.03, 0.82, '\\n'.join(lines),\n"
    "         fontsize=11, fontfamily='monospace', color='#222222',\n"
    "         va='top', linespacing=1.5,\n"
    "         bbox=dict(boxstyle='round,pad=0.6', facecolor='white',\n"
    "                   edgecolor='#CCCCCC', alpha=0.92))\n\n"
    "plt.savefig(OUTPUT_DIR + 'g2_peta.png', dpi=150, bbox_inches='tight', pad_inches=0.2, facecolor='none')\n"
    "plt.show()"
))
cells.append(md(
    "#### Wawasan\n\n"
    "> Kemiskinan di Jawa Barat terkonsentrasi di bagian selatan dan timur. "
    "Kabupaten Indramayu, Kuningan, Majalengka, dan Tasikmalaya memperlihatkan angka "
    "kemiskinan tertinggi yang melampaui 10%. Sebaliknya, kota-kota di koridor utara "
    "seperti Kota Depok, Kota Bekasi, dan Kota Bandung mencatat tingkat kemiskinan "
    "terendah di bawah 5%, mencerminkan konsentrasi aktivitas ekonomi formal di kawasan tersebut."
))

# ---------------------------------------------------------------------------
# Section 7: Grafik 3 - Scatter
# ---------------------------------------------------------------------------
cells.append(section("Grafik 3: Korelasi Kemiskinan dan Pengangguran 2025", "7"))
cells.append(md(
    "Grafik pencar ini menguji hubungan antara persentase penduduk miskin dan tingkat "
    "pengangguran terbuka (TPT) di 27 kabupaten/kota Jawa Barat pada 2025. "
    "Kota dan Kabupaten dibedakan dengan warna berbeda, dan garis regresi linier "
    "ditampilkan untuk masing-masing kelompok."
))
cells.append(code(
    "COLOR_MAP = {'Kota': '#1A6B8A', 'Kabupaten': '#C0392B'}\n\n"
    "fig, ax = plt.subplots(figsize=(7, 4.5))\n\n"
    "for t, grp in jabar.groupby('type'):\n"
    "    ax.scatter(\n"
    "        grp['unemployment_rate'], grp['poverty_rate'],\n"
    "        color=COLOR_MAP[t], s=65, alpha=0.85,\n"
    "        edgecolors='white', linewidths=0.5,\n"
    "        label=t, zorder=3,\n"
    "    )\n"
    "    slope, intercept, *_ = stats.linregress(\n"
    "        grp['unemployment_rate'], grp['poverty_rate']\n"
    "    )\n"
    "    xl = np.linspace(jabar['unemployment_rate'].min(),\n"
    "                     jabar['unemployment_rate'].max(), 100)\n"
    "    ax.plot(xl, slope * xl + intercept,\n"
    "            color=COLOR_MAP[t], linewidth=1.8, alpha=0.65)\n\n"
    "LABEL_OFFSET = {\n"
    "    'Bekasi':     (6, 6),\n"
    "    'Kota Cimahi': (6, -10),\n"
    "}\n"
    "for _, row in jabar[jabar['region'].isin(ANOMALI_ALL)].iterrows():\n"
    "    dx, dy = LABEL_OFFSET.get(row['region'], (6, 3))\n"
    "    ax.annotate(\n"
    "        row['region'],\n"
    "        xy=(row['unemployment_rate'], row['poverty_rate']),\n"
    "        xytext=(dx, dy), textcoords='offset points',\n"
    "        fontsize=8, color='#333333',\n"
    "    )\n\n"
    "r, _ = stats.pearsonr(jabar['unemployment_rate'], jabar['poverty_rate'])\n"
    "ax.text(0.97, 0.96, f'r = {r:.2f}', transform=ax.transAxes,\n"
    "        fontsize=10, va='top', ha='right', color='#555555')\n\n"
    "ax.legend(title='Tipe Wilayah', frameon=True, fontsize=10,\n"
    "          loc='lower left', borderaxespad=0.5)\n"
    "ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f%%'))\n"
    "ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f%%'))\n"
    "ax.tick_params(axis='x', labelsize=8, colors='#777777')\n"
    "ax.tick_params(axis='y', labelsize=8, colors='#777777')\n"
    "ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)\n"
    "ax.grid(linestyle=':', alpha=0.3, color='#DDDDDD')\n"
    "plt.tight_layout()\n"
    "plt.savefig(OUTPUT_DIR + 'g3_scatter.png', dpi=150, bbox_inches='tight', facecolor='none')\n"
    "plt.show()"
))
cells.append(md(
    "#### Wawasan\n\n"
    "> Korelasi antara kemiskinan dan pengangguran di Jawa Barat lemah dan negatif "
    "(r = -0.37), menunjukkan bahwa tingginya pengangguran tidak selalu sejalan dengan "
    "tingginya kemiskinan. Kabupaten Pangandaran, Tasikmalaya, dan Ciamis memiliki "
    "tingkat pengangguran yang sangat rendah tetapi angka kemiskinan tinggi di Jawa Barat, "
    "mengindikasikan bahwa pekerjaan yang tersedia di kawasan tersebut belum mampu "
    "mengangkat daya beli masyarakat."
))

# ---------------------------------------------------------------------------
# Section 8: Grafik 4 - Dual bar
# ---------------------------------------------------------------------------
cells.append(section("Grafik 4: Kota-Kota Anomali Jawa Barat 2025", "8"))
cells.append(md(
    "Untuk menguji apakah garis kemiskinan menjelaskan anomali, setiap wilayah anomali "
    "dipetakan ke dua persentil secara bersamaan: persentil TPT dan persentil garis kemiskinan "
    "relatif terhadap 27 wilayah Jawa Barat. Apabila garis kemiskinan memang menjadi "
    "penyebab anomali, wilayah dengan TPT rendah seharusnya memiliki garis kemiskinan "
    "yang tinggi pula, dan sebaliknya. Kemiringan garis setiap wilayah langsung "
    "memperlihatkan apakah hipotesis itu terkonfirmasi atau tidak."
))
cells.append(code(
    "jabar['tpt_rank'] = jabar['unemployment_rate'].rank(method='min').astype(int)\n"
    "jabar['gk_rank']  = jabar['poverty_level'].rank(method='min').astype(int)\n\n"
    "anomali = jabar[jabar['region'].isin(ANOMALI_ALL)].copy()\n\n"
    "C_HIGH = '#E63946'\n"
    "C_LOW  = '#2A9D8F'\n"
    "STYLES = ['-', '--', ':']\n\n"
    "fig, ax = plt.subplots(figsize=(8, 4.8))\n\n"
    "for grp, color in [(ANOMALI_HIGH, C_HIGH), (ANOMALI_LOW, C_LOW)]:\n"
    "    subset = anomali[anomali['region'].isin(grp)].sort_values('tpt_rank')\n"
    "    for i, (_, row) in enumerate(subset.iterrows()):\n"
    "        tpt, gk = row['tpt_rank'], row['gk_rank']\n"
    "        ax.plot([0, 1], [tpt, gk], color=color, lw=2.2,\n"
    "                ls=STYLES[i], alpha=0.88)\n"
    "        ax.scatter([0, 1], [tpt, gk], color=color, s=60, zorder=5)\n"
    "        ax.text(-0.04, tpt, f\"{row['region']}  #{int(tpt)}\",\n"
    "                ha='right', va='center', fontsize=8, color=color)\n"
    "        ax.text(1.04, gk, f\"#{int(gk)}\",\n"
    "                ha='left', va='center', fontsize=8, color=color)\n\n"
    "ax.axhline(14, color='#AAAAAA', lw=0.9, ls='--')\n"
    "ax.text(0.5, 14.5, 'median (#14)', ha='center', va='bottom',\n"
    "        fontsize=7, color='#AAAAAA')\n\n"
    "from matplotlib.lines import Line2D\n"
    "legend_el = [\n"
    "    Line2D([0],[0], color=C_LOW,  lw=2,\n"
    "           label='Rasio rendah: kemiskinan rendah, TPT tinggi'),\n"
    "    Line2D([0],[0], color=C_HIGH, lw=2,\n"
    "           label='Rasio tinggi: kemiskinan tinggi, TPT rendah'),\n"
    "]\n"
    "ax.legend(handles=legend_el, loc='lower center',\n"
    "          bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=11, frameon=True)\n\n"
    "ax.set_xticks([])\n"
    "ax.set_xlim(-0.18, 1.08)\n"
    "ax.set_ylim(0, 30)\n"
    "for ref_y in [1, 27]:\n"
    "    ax.axhline(ref_y, color='#CCCCCC', linewidth=0.8, linestyle=':', zorder=0)\n"
    "for x_val in [0, 1]:\n"
    "    ax.axvline(x_val, color='#DDDDDD', linewidth=0.8, linestyle=':', zorder=0)\n"
    "ax.tick_params(axis='y', left=False, labelleft=False)\n"
    "ax.set_yticks([])\n"
    "ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)\n"
    "ax.grid(axis='y', linestyle=':', alpha=0.2, color='#DDDDDD')\n"
    "plt.tight_layout()\n"
    "plt.savefig(OUTPUT_DIR + 'g4_slopegraph.png', dpi=150, bbox_inches='tight', facecolor='none')\n"
    "plt.show()"
))
cells.append(md(
    "#### Wawasan\n\n"
    "> Tiga wilayah rasio tinggi (merah) memiliki TPT di persentil terbawah "
    "tetapi garis kemiskinan yang hanya berada di kisaran menengah ke bawah. "
    "Garis mereka condong ke atas atau relatif datar, artinya garis kemiskinan "
    "tidak tinggi sehingga hipotesis biaya hidup tidak terkonfirmasi. "
    "Kemiskinan tinggi di sini bukan karena standar subsisten yang mahal, "
    "melainkan karena upah sektor pertanian memang rendah secara absolut.\n\n"
    "> Tiga wilayah rasio rendah (hijau) memiliki garis kemiskinan di persentil "
    "tertinggi, jauh di atas persentil TPT mereka. Garis mereka menanjak tajam "
    "ke kanan, mengonfirmasi bahwa tingginya standar biaya hidup memang "
    "berkorelasi dengan rendahnya kemiskinan meski penganggurannya tinggi."
))

# ---------------------------------------------------------------------------
# Notebook writer
# ---------------------------------------------------------------------------
nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.13.0"},
    },
    "cells": cells,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
print(f"Wrote {len(cells)} cells -> {OUT}")
