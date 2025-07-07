from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CertRequest(BaseModel):
    name: str
    level: str
    email: str

@router.post("/issue")
def issue_certificate(data: CertRequest):
    cert_hash = f"blockchain-hash-{data.email[:3]}-{data.level}"
    return {
        "message": "Certificate issued successfully.",
        "cert_hash": cert_hash
    }
