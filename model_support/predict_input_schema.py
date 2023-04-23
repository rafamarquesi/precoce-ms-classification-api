from marshmallow import Schema, fields
from marshmallow.validate import OneOf


class PredictInputSchema(Schema):

    tipificacao = fields.Str(
        required=True,
        error_messages={'required': 'tipificacao é obrigatório'},
        validate=OneOf(
            ['Macho Inteiro', 'Fêmea', 'Macho Castrado'],
            error='tipificacao deve ser um dos seguintes valores: {choices}'
        ),
        attribute='Tipificacao'
    )
    qtd_animais_lote = fields.Integer(
        required=True,
        error_messages={
            'required': 'qtd_animais_lote é obrigatório'},
        attribute='QTD_ANIMAIS_LOTE'
    )
    peso_medio_lote = fields.Float(
        required=True,
        error_messages={'required': 'peso_medio_lote é obrigatório'},
        attribute='PESO_MEDIO_LOTE'
    )
    questionario_classificacao_estabel = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_classificacao_estabel é obrigatório'},
        validate=OneOf(
            [0, 21, 26, 30],
            labels=['sem classificação', 'simples',
                    'intermediário', 'avançado'],
            error='questionario_classificacao_estabel deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='QuestionarioClassificacaoEstabel'
    )
    ilp = fields.Integer(
        required=True,
        error_messages={
            'required': 'ilp é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='ilp deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='ILP'
    )
    ifp = fields.Integer(
        required=True,
        error_messages={
            'required': 'ifp é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='ifp deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='IFP'
    )
    ilpf = fields.Integer(
        required=True,
        error_messages={
            'required': 'ilpf é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='ilpf deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='ILPF'
    )
    questionario_possui_outros_incentiv = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_possui_outros_incentiv é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='questionario_possui_outros_incentiv deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='QuestionarioPossuiOutrosIncentiv'
    )
    questionario_fabrica_racao = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_fabrica_racao é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='questionario_fabrica_racao deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='QuestionarioFabricaRacao'
    )
    regua_de_manejo = fields.Integer(
        required=True,
        error_messages={
            'required': 'regua_de_manejo é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='regua_de_manejo deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='regua de manejo'
    )
    identificacao_individual = fields.Integer(
        required=True,
        error_messages={
            'required': 'identificacao_individual é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='identificacao_individual deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='identificacao individual'
    )
    rastreamento_sisbov = fields.Integer(
        required=True,
        error_messages={
            'required': 'rastreamento_sisbov é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='rastreamento_sisbov deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='rastreamento SISBOV'
    )
    participa_de_aliancas_mercadolog = fields.Integer(
        required=True,
        error_messages={
            'required': 'participa_de_aliancas_mercadolog é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='participa_de_aliancas_mercadolog deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='participa de aliancas mercadolog'
    )
    questionario_pratica_recuperacao_pa = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_pratica_recuperacao_pa é obrigatória'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='questionario_pratica_recuperacao_pa deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='QuestionarioPraticaRecuperacaoPa'
    )
    confinamento = fields.Integer(
        required=True,
        error_messages={
            'required': 'confinamento é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='confinamento deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='Confinamento'
    )
    suplementacao_a_campo = fields.Integer(
        required=True,
        error_messages={
            'required': 'suplementacao_a_campo é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='suplementacao_a_campo deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='Suplementacao_a_campo'
    )
    semi_confinamento = fields.Integer(
        required=True,
        error_messages={
            'required': 'semi_confinamento é obrigatório'},
        validate=OneOf(
            [0, 1],
            labels=['não', 'sim'],
            error='semi_confinamento deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='SemiConfinamento'
    )
    tot3m_chuva = fields.Float(
        required=True,
        error_messages={'required': 'tot3m_chuva é obrigatório'},
        attribute='tot3m_Chuva'
    )
    med3m_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med3m_form_itu_inst é obrigatório'},
        attribute='med3m_formITUinst'
    )
    med3m_ndvi = fields.Float(
        required=True,
        error_messages={'required': 'med3m_ndvi é obrigatório'},
        attribute='med3m_NDVI'
    )
    med3m_prer_milho = fields.Float(
        required=True,
        error_messages={'required': 'med3m_prer_milho é obrigatório'},
        attribute='med3m_preR_milho'
    )
    med3m_prer_boi = fields.Float(
        required=True,
        error_messages={'required': 'med3m_prer_boi é obrigatório'},
        attribute='med3m_preR_boi'
    )

# class PredictInput():

#     def __init__(
#         self, estabelecimento_municipio: str, tipificacao: str, maturidade: str, acabamento: str, peso: float,
#         questionario_classificacao_estabel: int, ferti_irrigacao: int, ilp: int, ifp: int, ilpf: int, concen_volum: int,
#         creep_feeding: int, forn_estrat_silagem: int, proteico: int, proteico_energetico: int, racao_bal_cons_inferior: int,
#         sal_mineral: int, salmineral_ureia: int, racaoo_bal_consumo_ig: int, grao_inteiro: int, alto_concentr_volum: int,
#         alto_concentrado: int, questionario_possui_outros_incentiv: int, questionario_fabrica_racao: int, regua_de_manejo: int,
#         identificacao_individual: int, rastreamento_sisbov: int, bpa: int, participa_de_aliancas_mercadolog: int,
#         questionario_pratica_recuperacao_pa: int, confinamento: int, suplementacao_a_campo: int, semi_confinamento: int,
#         med7d_form_itu_inst: float, med7d_prer_soja: float, med7d_prer_milho: float, med7d_prer_boi: float,
#         med1m_form_itu_inst: float, med1m_prer_soja: float, med1m_prer_milho: float, med1m_prer_boi: float,
#         med3m_form_itu_inst: float, med3m_prer_soja: float, med3m_prer_milho: float, med3m_prer_boi: float,
#         med6m_form_itu_inst: float, med6m_prer_soja: float, med6m_prer_milho: float, med6m_prer_boi: float,
#         med12m_form_itu_inst: float, med12m_prer_soja: float, med12m_prer_milho: float, med12m_prer_boi: float,
#         cnt7d_cl_itu_inst: float, cnt1m_cl_itu_inst: float, cnt3m_cl_itu_inst: float, cnt6m_cl_itu_inst: float,
#         cnt12m_cl_itu_inst: float, ano: int
#     ):
#         self.estabelecimento_municipio = estabelecimento_municipio
#         self.tipificacao = tipificacao
#         self.maturidade = maturidade
#         self.acabamento = acabamento
#         self.peso = peso
#         self.questionario_classificacao_estabel = questionario_classificacao_estabel
#         self.ferti_irrigacao = ferti_irrigacao
#         self.ilp = ilp
#         self.ifp = ifp
#         self.ilpf = ilpf
#         self.concen_volum = concen_volum
#         self.creep_feeding = creep_feeding
#         self.forn_estrat_silagem = forn_estrat_silagem
#         self.proteico = proteico
#         self.proteico_energetico = proteico_energetico
#         self.racao_bal_cons_inferior = racao_bal_cons_inferior
#         self.sal_mineral = sal_mineral
#         self.salmineral_ureia = salmineral_ureia
#         self.racaoo_bal_consumo_ig = racaoo_bal_consumo_ig
#         self.grao_inteiro = grao_inteiro
#         self.alto_concentr_volum = alto_concentr_volum
#         self.alto_concentrado = alto_concentrado
#         self.questionario_possui_outros_incentiv = questionario_possui_outros_incentiv
#         self.questionario_fabrica_racao = questionario_fabrica_racao
#         self.regua_de_manejo = regua_de_manejo
#         self.identificacao_individual = identificacao_individual
#         self.rastreamento_sisbov = rastreamento_sisbov
#         self.bpa = bpa
#         self.participa_de_aliancas_mercadolog = participa_de_aliancas_mercadolog
#         self.questionario_pratica_recuperacao_pa = questionario_pratica_recuperacao_pa
#         self.confinamento = confinamento
#         self.suplementacao_a_campo = suplementacao_a_campo
#         self.semi_confinamento = semi_confinamento
#         self.med7d_form_itu_inst = med7d_form_itu_inst
#         self.med7d_prer_soja = med7d_prer_soja
#         self.med7d_prer_milho = med7d_prer_milho
#         self.med7d_prer_boi = med7d_prer_boi
#         self.med1m_form_itu_inst = med1m_form_itu_inst
#         self.med1m_prer_soja = med1m_prer_soja
#         self.med1m_prer_milho = med1m_prer_milho
#         self.med1m_prer_boi = med1m_prer_boi
#         self.med3m_form_itu_inst = med3m_form_itu_inst
#         self.med3m_prer_soja = med3m_prer_soja
#         self.med3m_prer_milho = med3m_prer_milho
#         self.med3m_prer_boi = med3m_prer_boi
#         self.med6m_form_itu_inst = med6m_form_itu_inst
#         self.med6m_prer_soja = med6m_prer_soja
#         self.med6m_prer_milho = med6m_prer_milho
#         self.med6m_prer_boi = med6m_prer_boi
#         self.med12m_form_itu_inst = med12m_form_itu_inst
#         self.med12m_prer_soja = med12m_prer_soja
#         self.med12m_prer_milho = med12m_prer_milho
#         self.med12m_prer_boi = med12m_prer_boi
#         self.cnt7d_cl_itu_inst = cnt7d_cl_itu_inst
#         self.cnt1m_cl_itu_inst = cnt1m_cl_itu_inst
#         self.cnt3m_cl_itu_inst = cnt3m_cl_itu_inst
#         self.cnt6m_cl_itu_inst = cnt6m_cl_itu_inst
#         self.cnt12m_cl_itu_inst = cnt12m_cl_itu_inst
#         self.ano = ano