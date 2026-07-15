import os
from pdf2image import convert_from_path

def pdf_to_png(pdf_path, output_folder):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    print(f"Processing: {pdf_path}...")
    
    # Convert PDF pages to a list of PIL (Pillow) Image objects
    # dpi=300 ensures sharp text clarity for AI vision or reading
    # If on Windows, pass your poppler path: poppler_path=r"C:\poppler\bin"
    pages = convert_from_path(pdf_path, dpi=300)
    
    # Loop through all pages and save them as PNGs
    for i, page in enumerate(pages):
        image_name = f"page_{i + 1}.png"
        image_path = os.path.join(output_folder, image_name)
        
        # Save as lossless PNG
        page.save(image_path, "PNG")
        print(f"Saved: {image_path}")

# --- Execute Script ---
pdf_file = r"C:\Users\02017067\Documents\pdfToImage\floorplan2.pdf"      # Path to your PDF
target_dir = "extracted_images"    # Where to store the PNGs

pdf_to_png(pdf_file, target_dir)