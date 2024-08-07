#Biblioteca necessarias
pip install jupyter notebook pandas numpy openai

#Configuración del entorno
# Importar bibliotecas necesarias
import openai  # o la API de lenguaje que prefieras usar
import pandas as pd
import numpy as np

#configuración de API
import openai
openai.api_key = 'tu_clave_api_aquí'

Implementación la función principal de generación de asesoría:
def generate_legal_advice(prompt, case_details):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # o el modelo que prefieras
        messages=[
            {"role": "system", "content": "Eres un asistente legal experto."},
            {"role": "user", "content": prompt.format(case_details=case_details)}
        ]
    )
    return response.choices[0].message['content']

#funciones de Fast Prompting
def generate_legal_advice(prompt, case_details):
    # Implementar la lógica de Fast Prompting aquí
    pass


#Implementación de técnicas de Fast Prompting
#a. Few-shot prompting   

def few_shot_legal_advice(case_details):
    prompt = """
    Caso 1: Disputa laboral
    Detalles: Empleado despedido sin causa justa
    Consejo: Presentar una demanda por despido injustificado

    Caso 2: Accidente de tráfico
    Detalles: Colisión en intersección, lesiones leves
    Consejo: Recopilar evidencias, contactar testigos, negociar con la aseguradora

    Nuevo caso:
    Detalles: {case_details}
    Consejo:
    """
    return generate_legal_advice(prompt, case_details)

#b. Chain-of-thought prompting

def cot_legal_advice(case_details):
    prompt = """
    Dado el siguiente caso legal:
    {case_details}

    Sigue estos pasos para proporcionar asesoría:
    1. Identifica el área del derecho involucrada
    2. Analiza los hechos clave del caso
    3. Considera las leyes y precedentes aplicables
    4. Evalúa las posibles acciones legales
    5. Proporciona una recomendación

    Asesoría detallada:
    """
    return generate_legal_advice(prompt, case_details)

#Ejemplos de uso
    caso_ejemplo = "Cliente acusado de robo en tienda, sin antecedentes penales"

print("Asesoría usando Few-shot Prompting:")
print(few_shot_legal_advice(caso_ejemplo))

print("\nAsesoría usando Chain-of-thought Prompting:")
print(cot_legal_advice(caso_ejemplo))

casos_ejemplo = [
    "Cliente acusado de robo en tienda, sin antecedentes penales",
    "Disputa por custodia de hijos en proceso de divorcio",
    "Empleado sufre accidente laboral, empresa niega responsabilidad"
]

#las pruebas y muestra los resultados:
for caso in casos_ejemplo:
    print(f"Caso: {caso}")
    print("\nAsesoría usando Few-shot Prompting:")
    print(few_shot_legal_advice(caso))
    print("\nAsesoría usando Chain-of-thought Prompting:")
    print(cot_legal_advice(caso))
    print("\n" + "="*50 + "\n")