from fastapi.responses import Response
import os
import zipfile
import io

def jsonDefault(object):
    return object.__dict__

def zipfiles(files):
    zip_filename = "response.zip"

    s = io.BytesIO()

    with zipfile.ZipFile(s, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.writestr(f[0], f[1])

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = Response(s.getvalue(), media_type="application/x-zip-compressed", headers={
        'Content-Disposition': f'attachment;filename={zip_filename}'
    })

    return resp