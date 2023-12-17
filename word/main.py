from fastapi import FastAPI
from fastapi.responses import FileResponse
from word import generate_doc
app = FastAPI()


    
@app.post("/download-doc")
async def doc_to_download(new_speciality, new_napr, new_level):
    await generate_doc(new_speciality=new_speciality, new_napr=new_napr, new_level=new_level)
    return FileResponse('finish.docx', headers={"Content-Disposition": f"attachment; filename=finish.docx"})