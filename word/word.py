from docx import Document

async def generate_doc(new_speciality, new_napr, new_level):
    
    document = Document("demo.docx")
    
    def replace_text(doc, old_text, new_text):
        for paragraph in doc.paragraphs:
            if old_text in paragraph.text:
                for run in paragraph.runs:
                    run.text = run.text.replace(old_text, new_text)
                    
    old_speciality = "speciality"
    old_napr = "napr"
    old_level = "level"
    
    replace_text(doc=document, old_text=old_speciality, new_text=new_speciality)
    replace_text(doc=document, old_text=old_napr, new_text=new_napr)
    replace_text(doc=document, old_text=old_level, new_text=new_level)
    
    document.save('finish.docx')
    
