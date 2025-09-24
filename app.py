
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Tugas 1 - Tabel", page_icon="📊", layout="wide")
st.title("📊 Tugas 1 — Keamanan Data")

LOGO_PATH = Path(__file__).parent / "assets" / "uajy_logo.png"
col_logo, col_title = st.columns([1, 5], vertical_alignment="center")
with col_logo:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), caption=None, use_column_width=True)
    else:
        st.markdown(
            """
            <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;border:1px dashed #ccc;padding:8px;border-radius:8px;">
                <span style="font-size:13px;">Hehe -_-</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col_title:
    st.markdown(
        """
        <div style="padding-left:8px;">
            <h2 style="margin-bottom:0;">Universitas Atma Jaya Yogyakarta</h2>
            <div style="opacity:0.75; margin-top:2px;">Informatika / Keamanan Data — Tugas 1</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.divider()

lab1_rows = [
    [1, "Daftar nama karyawan dan gaji", "Confidential", "Data pribadi karyawan termasuk data sensitif; hanya terbatas HR & manajemen."],
    [2, "Press release produk baru", "Public", "Informasi memang ditujukan untuk publik."],
    [3, "Database pelanggan", "Restricted", "Berisi data pribadi (PII) yang dilindungi UU Perlindungan Data Pribadi, akses sangat terbatas."],
    [4, "Source code aplikasi", "Restricted", "Aset intelektual bernilai tinggi, risiko besar jika bocor."],
    [5, "Laporan keuangan triwulan", "Confidential", "Belum dipublikasikan, bisa mempengaruhi investor & regulasi jika bocor."],
    [6, "Manual user software", "Public", "Ditujukan untuk pengguna akhir, boleh diakses publik."],
    [7, "Rencana strategis ekspansi", "Restricted", "Dokumen rahasia strategis perusahaan."],
    [8, "Data transaksi kartu kredit", "Restricted", "Data finansial sensitif, harus dilindungi dengan ketat (PCI DSS)."],
    [9, "Foto company gathering", "Internal", "Ditujukan untuk konsumsi karyawan dan membangun budaya perusahaan. Tidak untuk publikasi umum tanpa izin dari individu di dalam foto."],
    [10, "Email internal budgeting", "Confidential", "Mengandung informasi keuangan internal yang tidak boleh tersebar luas."],
    [11, "Formula algoritma ML", "Restricted", "Aset R&D bernilai tinggi, rahasia kompetitif."],
    [12, "Data biometrik akses", "Restricted", "Data pribadi sangat sensitif, risiko tinggi jika bocor."],
    [13, "Website company profile", "Public", "Memang ditujukan untuk promosi ke publik."],
    [14, "Kontak supplier", "Confidential", "Dokumen bisnis yang mengandung informasi negosiasi & harga"],
    [15, "Data lokasi real-time", "Restricted", "Data sensitif pelanggan dan operasional, bisa disalahgunakan."],
]
lab1_df = pd.DataFrame(lab1_rows, columns=["No", "Jenis Data", "Level Klasifikasi", "Alasan/Justifikasi"])

lab2_rows = [
    ["Data gaji Karyawan", "RW", "R", "N", "Admin (HR/Finance) memiliki akses penuh untuk mengelola gaji. Staff diberikan akses baca (Read-only), kemungkinan untuk transparansi atau bagi manajer untuk melihat gaji timnya tanpa bisa mengubahnya."],
    ["Database pelanggan", "RW", "RW", "R", "Admin memiliki akses penuh. Staff (misal: Customer Service) perlu membaca dan mengubah data untuk melayani pelanggan. Intern diberi akses baca (Read-only) untuk pembelajaran, tanpa bisa mengubah data penting."],
    ["Source Code Aplikasi", "RW", "R", "N", "Admin/Lead Developer memiliki akses penuh. Staff developer diberi akses baca (Read-only) untuk mempelajari kode atau troubleshooting di luar modul intinya. Intern tidak diberi akses untuk melindungi kekayaan intelektual."],
    ["Data Kartu Kredit", "RW", "R", "N", "Akses ini sangat berisiko. Staff (misal: tim anti-penipuan) mungkin memerlukan akses baca (Read-only) untuk verifikasi. Admin memiliki akses tulis (Read-Write) untuk mengelola data pembayaran dalam kasus sengketa atau refund."],
    ["Manual User Software", "RW", "RW", "R", "Akses tulis (Read-Write) diberikan kepada Staff untuk memungkinkan mereka ikut serta memperbarui dokumentasi produk secara kolaboratif. Intern memiliki akses baca (Read-only) untuk mempelajari produk."],
    ["Rencana Strategis", "RW", "RW", "R", "Perusahaan menerapkan transparansi tinggi; Staff dilibatkan dalam memberi masukan dan mengedit rencana. Intern diberi akses baca (Read-only) sebagai bagian dari proses pembelajaran untuk memahami visi perusahaan."],
]
lab2_df = pd.DataFrame(lab2_rows, columns=["Jenis Data", "Admin", "Staff", "Intern", "Justifikasi"])

lab4_rows = [
    ["E-commerce", "Camera", "Yes, to scan the product barcode/QR code, or upload proof/review photos.", "Low", "Low", "Allow"],
    ["E-commerce", "Location", "Yes, for shipping cost estimates, searching for the nearest store, and delivery.", "Low", "Low", "Allow"],
    ["E-commerce", "Contacts", "No, not needed just for purchasing item.", "Low", "Low", "Allow"],
    ["Banking", "SMS", "Yes, to read the OTP (One-Time Password) code automatically", "Low", "Medium", "Allow"],
    ["Banking", "Microphone", "No. Core banking functions do not require a microphone.", "Medium", "High", "Deny"],
    ["Social Media", "Contacts", "Yes, to connect to friends", "Low", "Medium", "Allow"],
]
lab4_df = pd.DataFrame(lab4_rows, columns=["App", "Permission", "Necessary?", "Risk Level", "Alternative", "Action"])

lab1_html = """
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>No</th><th>Jenis Data</th><th>Level Klasifikasi</th><th>Alasan/Justifikasi</th>
    </tr>
  </thead>
  <tbody>
    {}
  </tbody>
</table>
""".format("\n".join([
    f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3].replace("&","&amp;")}</td></tr>'
    for r in lab1_rows
]))

lab2_html = """
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Jenis Data</th><th>Admin</th><th>Staff</th><th>Intern</th><th>Justifikasi</th>
    </tr>
  </thead>
  <tbody>
    {}
  </tbody>
</table>
""".format("\n".join([
    f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4].replace("&","&amp;")}</td></tr>'
    for r in lab2_rows
]))

lab4_html = """
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>App</th><th>Permission</th><th>Necessary?</th><th>Risk Level</th><th>Alternative</th><th>Action</th>
    </tr>
  </thead>
  <tbody>
    {}
  </tbody>
</table>
""".format("\n".join([
    f'<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td>{r[5]}</td></tr>'
    for r in lab4_rows
]))

tabs = st.tabs(["Lab 1 — Inventarisasi & Klasifikasi", "Lab 2 — Kebijakan Akses", "Lab 4 — Mobile App Permissions"])

def section(df, html, csv_name):
    view_html = st.toggle("Tampilkan sebagai HTML murni (tanpa style)?", value=False, key=csv_name+"_toggle")
    if view_html:
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(f"⬇️ Download CSV ({csv_name}.csv)", data=csv, file_name=f"{csv_name}.csv", mime="text/csv")

with tabs[0]:
    st.subheader("Lab 1 — Inventarisasi & Klasifikasi Data Dasar")
    section(lab1_df, lab1_html, "lab1")

with tabs[1]:
    st.subheader("Lab 2 — Simulasi Kebijakan Akses")
    section(lab2_df, lab2_html, "lab2")

with tabs[2]:
    st.subheader("Lab 4 — Mobile App Permission Audit")
    section(lab4_df, lab4_html, "lab4")
