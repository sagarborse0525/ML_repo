import fitz  # PyMuPDF library
import os
 
def extract_columns(pdf_path, column_1_area, column_2_area):
    document = fitz.open(pdf_path)
    all_text = []
 
    for page_num in range(len(document)):
        page = document.load_page(page_num)
 
        # Extract text from the specified areas for each column
        text_column_1 = page.get_text("text", clip=column_1_area)
        text_column_2 = page.get_text("text", clip=column_2_area)
 
        all_text.append((text_column_1, text_column_2))
 
    return all_text
 
# Define the areas for each column (coordinates: x0, y0, x1, y1)
column_1_area = fitz.Rect(0, 0, 300, 842)  # Adjust the coordinates based on your PDF
column_2_area = fitz.Rect(300, 0, 600, 842)  # Adjust the coordinates based on your PDF
 
# Extract text from all pages

for file in os.listdir('2021-2024_Approved_Bills_Senate'):
    input_pdf_file = file
    print(input_pdf_file)
    all_text = extract_columns("2021-2024_Approved_Bills_Senate/"+input_pdf_file, column_1_area, column_2_area)
    
    # Print the extracted text for each page
    extract_file = input_pdf_file.split(".")
    with open("extracted_pdf_files/"+extract_file[0]+".txt", "w",encoding="utf-8") as output_file:

        for page_num, (text_column_1, text_column_2) in enumerate(all_text):
            output_file.write(f"Page {page_num + 1} \n")
            output_file.write(text_column_1 + "\n")
        
print("PDF file extracted completed and saved to extractected_file .txt")