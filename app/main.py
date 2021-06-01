from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from pyshex import ShExEvaluator

app = FastAPI(
    title='ShEx Validation API',
    description='Microservice for ShEx validation.',
    version="0.1.0",
)

class Validator(BaseModel):
    shex: str = Query(..., title='ShEx Schema')
    rdf: str = Query(..., title='RDF (RDF XML)')
    start: str = Query(..., title='Starting Shape')
    focus: str = Query(..., title='Focus URI')

class Response(BaseModel):
    success: bool = True
    error: Optional[str] = None

@app.post('/validate', response_model=Response)
def validation(validator: Validator):
    shex = validator.shex.encode('latin-1', 'backslashreplace').decode('unicode-escape')

    try:
        pyshex_validator = ShExEvaluator(schema=shex, start=validator.start)
    except Exception:
        raise HTTPException(status_code=400, detail='Unable to parse ShEx or start shape.')

    try:
        result = pyshex_validator.evaluate(validator.rdf, focus=validator.focus, rdf_format='xml')
    except Exception:
        raise HTTPException(status_code=400, detail='Unable to parse or validate RDF.')

    if result[0].result:
        return Response()
    return Response(success=False, error=result[0].reason)
