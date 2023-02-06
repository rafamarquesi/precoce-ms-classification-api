from flask import request, jsonify

from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import OneOf, Range

from model_support import app
from model_support.functions import get_model_response

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


class PredictInputSchema(Schema):

    estabelecimento_municipio = fields.Str(
        required=True,
        error_messages={'required': 'estabelecimento_municipio é obrigatório'},
        attribute='EstabelecimentoMunicipio'
    )
    tipificacao = fields.Str(
        required=True,
        error_messages={'required': 'tipificacao é obrigatório'},
        attribute='Tipificacao'
    )
    maturidade = fields.Str(
        required=True,
        error_messages={'required': 'maturidade é obrigatória'},
        validate=OneOf(
            ['d', '2', '4', '6', '8'],
            labels=['Dente de leite', 'Dois dentes',
                    'Quatro dentes', 'Seis dentes', 'Oito dentes'],
            error='Maturidade deve ser um dos seguintes valores: {choices}\nSignificados: {labels}'
        ),
        attribute='Maturidade'
    )
    acabamento = fields.Str(
        required=True,
        error_messages={'required': 'acabamento é obrigatório'},
        attribute='Acabamento'
    )
    peso = fields.Float(
        required=True,
        error_messages={'required': 'peso é obrigatório'},
        validate=Range(
            min=123, max=516.400024, min_inclusive=True, max_inclusive=True, error='Peso deve estar entre 123 e 516.400024'
        ),
        attribute='Peso'
    )
    questionario_classificacao_estabel = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_classificacao_estabel é obrigatório'},
        attribute='QuestionarioClassificacaoEstabel'
    )
    ferti_irrigacao = fields.Integer(
        required=True,
        error_messages={
            'required': 'ferti_irrigacao é obrigatório'},
        attribute='FERTIIRRIGACAO'
    )
    ilp = fields.Integer(
        required=True,
        error_messages={
            'required': 'ilp é obrigatório'},
        attribute='ILP'
    )
    ifp = fields.Integer(
        required=True,
        error_messages={
            'required': 'ifp é obrigatório'},
        attribute='IFP'
    )
    ilpf = fields.Integer(
        required=True,
        error_messages={
            'required': 'ilpf é obrigatório'},
        attribute='ILPF'
    )
    concen_volum = fields.Integer(
        required=True,
        error_messages={
            'required': 'concen_volum é obrigatório'},
        attribute='CONCEN_VOLUM'
    )
    creep_feeding = fields.Integer(
        required=True,
        error_messages={
            'required': 'creep_feeding é obrigatório'},
        attribute='CREEPFEEDING'
    )
    forn_estrat_silagem = fields.Integer(
        required=True,
        error_messages={
            'required': 'forn_estrat_silagem é obrigatório'},
        attribute='FORN_ESTRAT_SILAGEM'
    )
    proteico = fields.Integer(
        required=True,
        error_messages={
            'required': 'proteico é obrigatório'},
        attribute='PROTEICO'
    )
    proteico_energetico = fields.Integer(
        required=True,
        error_messages={
            'required': 'proteico_energetico é obrigatório'},
        attribute='PROTEICO_ENERGETICO'
    )
    racao_bal_cons_inferior = fields.Integer(
        required=True,
        error_messages={
            'required': 'racao_bal_cons_inferior é obrigatório'},
        attribute='RACAO_BAL_CONS_INFERIOR'
    )
    sal_mineral = fields.Integer(
        required=True,
        error_messages={
            'required': 'sal_mineral é obrigatório'},
        attribute='SAL_MINERAL'
    )
    salmineral_ureia = fields.Integer(
        required=True,
        error_messages={
            'required': 'salmineral_ureia é obrigatório'},
        attribute='SALMINERAL_UREIA'
    )
    racaoo_bal_consumo_ig = fields.Integer(
        required=True,
        error_messages={
            'required': 'racaoo_bal_consumo_ig é obrigatório'},
        attribute='RACAOO_BAL_CONSUMO_IG'
    )
    grao_inteiro = fields.Integer(
        required=True,
        error_messages={
            'required': 'grao_inteiro é obrigatório'},
        attribute='GRAO_INTEIRO'
    )
    alto_concentr_volum = fields.Integer(
        required=True,
        error_messages={
            'required': 'alto_concentr_volum é obrigatório'},
        attribute='ALTO_CONCENTR_VOLUM'
    )
    alto_concentrado = fields.Integer(
        required=True,
        error_messages={
            'required': 'alto_concentrado é obrigatório'},
        attribute='ALTO_CONCENTRADO'
    )
    questionario_possui_outros_incentiv = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_possui_outros_incentiv é obrigatório'},
        attribute='QuestionarioPossuiOutrosIncentiv'
    )
    questionario_fabrica_racao = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_fabrica_racao é obrigatório'},
        attribute='QuestionarioFabricaRacao'
    )
    regua_de_manejo = fields.Integer(
        required=True,
        error_messages={
            'required': 'regua_de_manejo é obrigatório'},
        attribute='regua de manejo'
    )
    identificacao_individual = fields.Integer(
        required=True,
        error_messages={
            'required': 'identificacao_individual é obrigatório'},
        attribute='identificacao individual'
    )
    rastreamento_sisbov = fields.Integer(
        required=True,
        error_messages={
            'required': 'rastreamento_sisbov é obrigatório'},
        attribute='rastreamento SISBOV'
    )
    bpa = fields.Integer(
        required=True,
        error_messages={
            'required': 'bpa é obrigatório'},
        attribute='BPA'
    )
    participa_de_aliancas_mercadolog = fields.Integer(
        required=True,
        error_messages={
            'required': 'participa_de_aliancas_mercadolog é obrigatório'},
        attribute='participa de aliancas mercadolog'
    )
    questionario_pratica_recuperacao_pa = fields.Integer(
        required=True,
        error_messages={
            'required': 'questionario_pratica_recuperacao_pa é obrigatória'},
        attribute='QuestionarioPraticaRecuperacaoPa'
    )
    confinamento = fields.Integer(
        required=True,
        error_messages={
            'required': 'confinamento é obrigatório'},
        attribute='Confinamento'
    )
    suplementacao_a_campo = fields.Integer(
        required=True,
        error_messages={
            'required': 'suplementacao_a_campo é obrigatório'},
        attribute='Suplementacao_a_campo'
    )
    semi_confinamento = fields.Integer(
        required=True,
        error_messages={
            'required': 'semi_confinamento é obrigatório'},
        attribute='SemiConfinamento'
    )
    med7d_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med7d_form_itu_inst é obrigatório'},
        attribute='med7d_formITUinst'
    )
    med7d_prer_soja = fields.Float(
        required=True,
        error_messages={'required': 'med7d_prer_soja é obrigatória'},
        attribute='med7d_preR_soja'
    )
    med7d_prer_milho = fields.Float(
        required=True,
        error_messages={'required': 'med7d_prer_milho é obrigatório'},
        attribute='med7d_preR_milho'
    )
    med7d_prer_boi = fields.Float(
        required=True,
        error_messages={'required': 'med7d_prer_boi é obrigatório'},
        attribute='med7d_preR_boi'
    )
    med1m_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med1m_form_itu_inst é obrigatório'},
        attribute='med1m_formITUinst'
    )
    med1m_prer_soja = fields.Float(
        required=True,
        error_messages={'required': 'med1m_prer_soja é obrigatória'},
        attribute='med1m_preR_soja'
    )
    med1m_prer_milho = fields.Float(
        required=True,
        error_messages={'required': 'med1m_prer_milho é obrigatório'},
        attribute='med1m_preR_milho'
    )
    med1m_prer_boi = fields.Float(
        required=True,
        error_messages={'required': 'med1m_prer_boi é obrigatório'},
        attribute='med1m_preR_boi'
    )
    med3m_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med3m_form_itu_inst é obrigatório'},
        attribute='med3m_formITUinst'
    )
    med3m_prer_soja = fields.Float(
        required=True,
        error_messages={'required': 'med3m_prer_soja é obrigatória'},
        attribute='med3m_preR_soja'
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
    med6m_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med6m_form_itu_inst é obrigatório'},
        attribute='med6m_formITUinst'
    )
    med6m_prer_soja = fields.Float(
        required=True,
        error_messages={'required': 'med6m_prer_soja é obrigatória'},
        attribute='med6m_preR_soja'
    )
    med6m_prer_milho = fields.Float(
        required=True,
        error_messages={'required': 'med6m_prer_milho é obrigatório'},
        attribute='med6m_preR_milho'
    )
    med6m_prer_boi = fields.Float(
        required=True,
        error_messages={'required': 'med6m_prer_boi é obrigatório'},
        attribute='med6m_preR_boi'
    )
    med12m_form_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'med12m_form_itu_inst é obrigatório'},
        attribute='med12m_formITUinst'
    )
    med12m_prer_soja = fields.Float(
        required=True,
        error_messages={'required': 'med12m_prer_soja é obrigatória'},
        attribute='med12m_preR_soja'
    )
    med12m_prer_milho = fields.Float(
        required=True,
        error_messages={'required': 'med12m_prer_milho é obrigatório'},
        attribute='med12m_preR_milho'
    )
    med12m_prer_boi = fields.Float(
        required=True,
        error_messages={'required': 'med12m_prer_boi é obrigatório'},
        attribute='med12m_preR_boi'
    )
    cnt7d_cl_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'cnt7d_cl_itu_inst é obrigatório'},
        attribute='cnt7d_CL_ITUinst'
    )
    cnt1m_cl_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'cnt1m_cl_itu_inst é obrigatório'},
        attribute='cnt1m_CL_ITUinst'
    )
    cnt3m_cl_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'cnt3m_cl_itu_inst é obrigatório'},
        attribute='cnt3m_CL_ITUinst'
    )
    cnt6m_cl_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'cnt6m_cl_itu_inst é obrigatório'},
        attribute='cnt6m_CL_ITUinst'
    )
    cnt12m_cl_itu_inst = fields.Float(
        required=True,
        error_messages={'required': 'cnt12m_cl_itu_inst é obrigatório'},
        attribute='cnt12m_CL_ITUinst'
    )
    ano = fields.Integer(
        required=False,
        load_default=2020,
        # error_messages={'required': 'ano é obrigatório'},
        attribute='ANO'
    )


predict_input_schema = PredictInputSchema()

model_name = 'Precoce MS'
version = 'v1.0.0'

@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}

    result['name'] = model_name
    result['version'] = version

    return result

@app.route('/health', methods=['GET'])
def health():
    """Return service health"""
    return 'ok'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        inputs = predict_input_schema.load(request.get_json())
    except ValidationError as err:
        return err.messages, 400
    
    try:
        response = get_model_response(predict_input_schema=inputs)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return jsonify(response)
