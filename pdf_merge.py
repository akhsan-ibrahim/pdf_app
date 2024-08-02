import os
import PyPDF2

def merge_pdfs_from_folder(input_folder, output_folder, output_pdf):
   merger = PyPDF2.PdfMerger()

   try:
      # Dapatkan semua file PDF di folder yang diberikan
      pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

      # Urutkan file PDF agar digabungkan dalam urutan yang diinginkan
      pdf_files.sort()

      for pdf in pdf_files:
         pdf_path = os.path.join(input_folder, pdf)
         merger.append(pdf_path)

      # Pastikan folder output ada
      if not os.path.exists(output_folder):
         os.makedirs(output_folder)

      # Path lengkap untuk file output
      output_pdf_path = os.path.join(output_folder, output_pdf)

      # Simpan file PDF yang sudah digabungkan
      with open(output_pdf_path, 'wb') as merged_pdf:
         merger.write(merged_pdf)

      print(f'Merged PDFs successfully. Output saved to: {output_pdf_path}')

   except Exception as e:
      print(f'Error merging PDFs: {e}')

# Contoh penggunaan
input_folder = 'A:\Kerja'
output_folder = 'A:\Kerja'
output_pdf = 'Berkas Lamaran.pdf'

merge_pdfs_from_folder(input_folder, output_folder, output_pdf)
