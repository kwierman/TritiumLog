from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

Further resources¶

    PDFlib is another PDF-generation library that has Python bindings. To use it with Django, just use the same concepts explained in this article.
    Pisa XHTML2PDF is yet another PDF-generation library. Pisa ships with an example of how to integrate Pisa with Django.
    HTMLdoc is a command-line script that can convert HTML to PDF. It doesn’t have a Python interface, but you can escape out to the shell using system or popen and retrieve the output in Python.

Other formats¶

Notice that there isn’t a lot in these examples that’s PDF-specific – just the bits using reportlab. You can use a similar technique to generate any arbitrary format that you can find a Python library for. Also see Outputting CSV with Django for another example and some techniques you can use when generated text-based formats.
Outputting CSV with Django
Managing static files (CSS, images)
Additional Information
Search: Version:
