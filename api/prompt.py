from flask import Flask, request
import vertexai
from vertexai.language_models import TextGenerationModel


app = Flask(__name__)

@app.route("/genai",methods=["POST"])
def hello_world():

    vertexai.init(project='on-prem-project-337210', location='us-central1')
    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 1000,  # Token limit determines the maximum amount of text output.
        "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    request_data = request.get_json()
    prompt_new = request_data['prompt']

    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
            prompt_new,
        **parameters,
    )
    print(f"Response from Model: {response.text}")

    return response.text
