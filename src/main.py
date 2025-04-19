from openai import OpenAI
import gradio as gr
import json


txt_openAI = gr.Textbox(label="Digite a sua chave de API da OpenAI", type="password", placeholder="sk-...")
client = OpenAI(api_key=txt_openAI)

taxa = {
    "EUR": 0.93,
    "USD": 1,
    "BRL": 5
}

def converter_moeda(quantidade, origem, destino):
    print("A função foi chamada")
    origem = origem.upper()
    destino = destino.upper()

    if origem not in taxa :
        return {"error": "Moeda não suportada: {origem}"}
    if destino not in taxa :
        return {"error": "Moeda não suportada {destino}"}

    quantidade_dolar = quantidade / taxa[origem]
    quantidade_convertida = quantidade_dolar * taxa[destino]

    return {
        "quantidade": quantidade,
        "origem": origem,
        "destino": destino,
        "quantidade_convertida": round(quantidade_convertida, 2),
    }

tools_moeda = [
    {
       "type": "function",     
       "name": "converter_moeda",
        "description": "Converte uma quantia de uma moeda para outra. Aceita as moedas: EUR, USD, BRL.",
        "parameters": {
            "type": "object",
            "properties": {
                "quantidade": {
                    "type": "number",
                    "description": "A quantia a ser convertida.",
                },
                "origem": {
                    "type": "string",
                    "description": "A moeda de origem.",
                },
                "destino": {
                    "type": "string",
                    "description": "A moeda de destino.",
                },
            },
            "required": ["quantidade", "origem", "destino"],
            "additionalProperties": False
    },
    "strict": True,
    }
]

def response_fn(message, history, txt_openAI):
    openai_history = []

    openai_history.append({"role": "user", "content": message})

    response = client.responses.create(
        model= "o4-mini",
        instructions="Responda como um pirata",
        input=openai_history,
        tools=tools_moeda
    )

    # verifica se o modelo quer fazer uma chamada de função
    if response.output and isinstance(response.output, list) and response.output[1].type == "function_call":

        tool_reasoning = response.output[0]
        tool_call = response.output[1]
        args = json.loads(tool_call.arguments)
        resultado_conversao = converter_moeda(**args)

        openai_history.append(tool_reasoning)
        openai_history.append(tool_call)
        openai_history.append({
            "type": "function_call_output",
            "call_id": tool_call.call_id,
            "output": json.dumps(resultado_conversao),
        })

        response = client.responses.create(
                model= "o4-mini",
                instructions="Responda como um pirata",
                input=openai_history,
                tools=tools_moeda
        )

    return response.output_text
    

gr.ChatInterface(response_fn, type="messages", additional_inputs=[txt_openAI]).launch()

