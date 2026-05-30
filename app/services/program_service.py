from app.schemas.program_schema import ProgramaRequest, ProgramaResponse
from app.services.donation_service import donation_forms

programas_db = {}
contador = 1

def create_programa(data: ProgramaRequest) -> ProgramaResponse:
    global contador
    programa = ProgramaResponse(
        id=contador,
        **data.model_dump()
    )
    programas_db[contador] = programa
    contador += 1
    return programa

def list_programas(apenas_ativos: bool = True):
    programas = list(programas_db.values())
    if apenas_ativos:
        programas = [p for p in programas if p.ativo]
    return programas

def get_programa_by_id(programa_id: int):
    return programas_db.get(programa_id)

def deactivate_programa(programa_id: int) -> bool:
    if programa_id not in programas_db:
        return False
    programa = programas_db[programa_id]
    programas_db[programa_id] = ProgramaResponse(
        **{**programa.model_dump(), "ativo": False}
    )
    return True

def get_programa_com_contagem():
    resultado = []
    
    for programa in programas_db.values():
        # Conta quantas doações referenciam esse programa
        total_solicitacoes = sum(
            1 for doacao in donation_forms
            if doacao.get("programa_id") == programa.id
        )
        
        resultado.append({
            "id": programa.id,
            "nome_programa": programa.nome_programa,
            "objetivo": programa.objetivo,
            "ativo": programa.ativo,
            "total_solicitacoes": total_solicitacoes
        })
    
    return resultado