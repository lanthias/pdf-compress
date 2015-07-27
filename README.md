# Pdf-compress Service

Given the URL of a PDF, I will compress it and send it back to you. I do this by using ghostscript as follows:

`gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=out.pdf in.pdf`

## Usage
* Look at the API (defined in `api.idl`) to see what functions are available, friend.
