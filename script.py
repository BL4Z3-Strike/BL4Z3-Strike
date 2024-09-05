from PyPDF2 import PdfWriter

def create_malicious_pdf(output_path):
    pdf_writer = PdfWriter()

    pdf_writer.add_blank_page(width=72, height=72)

    # This JavaScript code will show an alert box when the PDF is opened.
    # You can modify the payload for shell access or other purposes.
    js_code = """
    app.alert({
        cMsg: "This is a malicious JavaScript example for educational purposes.",
        cTitle: "Malicious PDF Alert"
    });
    """
    pdf_writer.add_js(js_code)

    with open(output_path, 'wb') as f:
        pdf_writer.write(f)
create_malicious_pdf('malicious_example.pdf')
