from pdf2image import convert_from_path
import os

poppler_path = r"A:\Code\pdf_app\poppler-24.02.0\Library\bin"
pdf_folder = r"A:\Lifeskill\Sertifikat PDF"
image_folder = r"A:\Lifeskill\Sertifikat JPG"

if not os.path.exists(image_folder):
   os.makedirs(image_folder)
   
for pdf_file in os.listdir(pdf_folder):
   if pdf_file.endswith(".pdf"):
      pdf_path = os.path.join(pdf_folder, pdf_file)
      try:
         pages = convert_from_path(pdf_path=pdf_path, dpi=400, poppler_path=poppler_path)
         pdf_image_folder = os.path.join(image_folder, os.path.splitext(pdf_file)[0])
         if not os.path.exists(pdf_image_folder):
            os.makedirs(pdf_image_folder)
         
         for idx, page in enumerate(pages, start=1):
            img_name = f"{os.path.splitext(pdf_file)[0]}_[{idx}].jpg"
            page.save(os.path.join(pdf_image_folder, img_name), "JPEG")
         print(f"Konversi {pdf_file} berhasil")
      except Exception as e:
         print(f"Terjadi kesalahan saat mengonversi {pdf_file}: {e}")
