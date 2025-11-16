
# Average scores

> [!NOTE]
> The evaluation results for each test variant are displayed below, averaged over the 21 test cases.

| Evaluator | |
| :-------- | ---:|
| coherence | 3.9523809523809526 
| relevance | 4.666666666666667 
| intent_resolution | 4.809523809523809 


# Individual test scores



## Test 1

### Inputs

* **Query:** What is the importance of choosing the right provider in getting the most value out of your health insurance plan?
* **Ground truth:** Choosing an in-network provider helps you save money and ensures better, more personalized care. [Northwind_Health_Plus_Benefits_Details-3.pdf]

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Choosing the right provider is key to maximizing your health insurance benefits. In-network providers reduce costs, offer better coverage, and support continuity of care, leading to more effective and personalized treatment. [Northwind_Health_Plus_Benefits_Details.pdf][Northwind_Standard_Benefits_Details.pdf]

</details>





## Test 2

### Inputs

* **Query:** What should you do when choosing an in-network provider for your health care needs?
* **Ground truth:** Check with Northwind Health Plus to confirm the provider is in-network, as this helps reduce costs.
[Northwind_Health_Plus_Benefits_Details-3.pdf]

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 4.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

To choose an in-network provider, confirm they are part of your plan using the Northwind website or by calling their office. Also consider location, availability, and office hours. [Northwind_Standard_Benefits_Details.pdf]

</details>





## Test 3

### Inputs

* **Query:** What range of in-network providers does Northwind Health Plus offer?
* **Ground truth:** Northwind Health Plus offers a wide range of in-network providers, including doctors, specialists, hospitals, and pharmacies.
[Northwind_Health_Plus_Benefits_Details-3.pdf]

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 4.0 |
| intent_resolution | 4.0 |




### Raw Outputs

<details>

Northwind Health Plus offers a wide range of in-network providers, including primary care physicians, specialists, hospitals, and pharmacies [Northwind_Health_Plus_Benefits_Details.pdf]. The exact range of in-network providers may vary depending on the area, but the Northwind Health Plus website provides a searchable directory of all in-network providers in your area [Northwind_Health_Plus_Benefits_Details.pdf]. It is important to check with Northwind Health Plus to ensure that the provider you are considering is in-network [Northwind_Health_Plus_Benefits_Details.pdf].

</details>





## Test 4

### Inputs

* **Query:** What is the limitation of in-network providers?
* **Ground truth:** The limitation of in-network providers is that they may not always be available in every area.
[Northwind_Health_Plus_Benefits_Details-3.pdf]

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

The limitation of in-network providers is that they may not accept the amount of payment offered by Northwind Health, which means you may be responsible for a greater portion of the cost [Northwind_Standard_Benefits_Details.pdf]. Additionally, out-of-network providers may not offer additional services or discounts that are available to in-network providers [Northwind_Standard_Benefits_Details.pdf]. It is recommended to choose an in-network provider whenever possible to ensure the best value for your health care expenses [Northwind_Standard_Benefits_Details.pdf].

Sources:
- Northwind_Standard_Benefits_Details.pdf

</details>





## Test 5

### Inputs

* **Query:** What resource does Northwind Health Plus provide to find in-network providers in your area?
* **Ground truth:** The Northwind Health Plus website offers a searchable directory of all in-network providers in your area. This directory is regularly updated, so you can be sure that you are choosing from in-network providers that are available.
[Northwind_Health_Plus_Benefits_Details-3.pdf]

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 3.0 |
| relevance | 3.0 |
| intent_resolution | 2.0 |




### Raw Outputs

<details>

Northwind Health Plus provides a variety of in-network providers, including primary care physicians, specialists, hospitals, and pharmacies [Northwind_Health_Plus_Benefits_Details.pdf].

</details>





## Test 6

### Inputs

* **Query:** How do you create a run?
* **Ground truth:** To create a run in Azure ML, create an Experiment and call start_logging().

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

To create a run using the Azure Machine Learning API, you first need to create an Experiment. Once you have an experiment, you can create a Run object that is associated with that experiment. Here is some Python code that demonstrates this process:

from azureml.core import Experiment, Run
from azureml.core.workspace import Workspace

# Define workspace and experiment
ws = Workspace.from_config()
exp = Experiment(workspace=ws, name='my_experiment')

# Create a new run
run = exp.start_logging()

In this code, the `from_config()` method reads the configuration file that you created when you set up your Azure Machine Learning workspace. The `Experiment` constructor creates an Experiment object that is associated with your workspace, and the `start_logging()` method creates a new Run object that is associated with the Experiment. Now you can use the `run` object to log metrics, upload files, and track other information related to your machine learning experiment.

</details>





## Test 7

### Inputs

* **Query:** How do you log a model?
* **Ground truth:** Use Model.register() or Run.upload_file() to log models in Azure ML.

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

There are a few ways to log models in Azure Machine Learning. One way is to use the `register_model()` method of the `Run` object. The `register_model()` method logs a model file in the Azure Machine Learning service workspace and makes it available for deployment. Here's an example:
from azureml.core import Model
model_path = './outputs/my_model.pkl'
model = Model.register(workspace=ws, model_path=model_path, model_name='my_model')
Another way to log a model is to save it as an output of a `Run`. If your model generation code is part of a script or Jupyter notebook that runs as an Azure Machine Learning experiment, you can save the model file as an output of the `Run` object.
from sklearn.linear_model import LogisticRegression
from azureml.core.run import Run
run = Run.get_context()
X_train, y_train = ...
log_reg = LogisticRegression().fit(X_train, y_train)
model_path = 'outputs/model.pkl'
joblib.dump(value=log_reg, filename=model_path)
run.upload_file(name=model_path, path_or_stream=model_path)

</details>





## Test 8

### Inputs

* **Query:** What is the capital of France?
* **Ground truth:** Paris is the capital of France.

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Paris is the capital of France.

</details>





## Test 9

### Inputs

* **Query:** What is the largest planet in our solar system?
* **Ground truth:** Jupiter is the largest planet in our solar system.

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 4.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Jupiter is the largest planet in our solar system.

</details>





## Test 10

### Inputs

* **Query:** Who wrote 'Pride and Prejudice'?
* **Ground truth:** Jane Austen wrote 'Pride and Prejudice'.

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Jane Austen wrote 'Pride and Prejudice'.

</details>





## Test 11

### Inputs

* **Query:** What is the boiling point of water?
* **Ground truth:** 100°C at 1 atm.

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

The boiling point of water is 100°C at standard atmospheric pressure.

</details>





## Test 12

### Inputs

* **Query:** Translate 'hello' to Spanish.
* **Ground truth:** hola

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

'Hello' in Spanish is 'hola'.

</details>





## Test 13

### Inputs

* **Query:** What is 2 + 2?
* **Ground truth:** 4

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 4.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

2 + 2 equals 4.

</details>





## Test 14

### Inputs

* **Query:** Who painted the Mona Lisa?
* **Ground truth:** Leonardo da Vinci

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 4.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Leonardo da Vinci painted the Mona Lisa.

</details>





## Test 15

### Inputs

* **Query:** What is the speed of light?
* **Ground truth:** 299,792 km/s

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

The speed of light in vacuum is approximately 299,792 kilometers per second.

</details>





## Test 16

### Inputs

* **Query:** What is the chemical symbol for gold?
* **Ground truth:** Au

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

The chemical symbol for gold is Au.

</details>





## Test 17

### Inputs

* **Query:** Who is the CEO of Microsoft?
* **Ground truth:** Satya Nadella

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Satya Nadella is the CEO of Microsoft.

</details>





## Test 18

### Inputs

* **Query:** What is the tallest mountain in the world?
* **Ground truth:** Mount Everest

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Mount Everest is the tallest mountain in the world.

</details>





## Test 19

### Inputs

* **Query:** What is the freezing point of water?
* **Ground truth:** 0°C

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

The freezing point of water is 0°C.

</details>





## Test 20

### Inputs

* **Query:** What is the main language spoken in Brazil?
* **Ground truth:** Portuguese

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Portuguese is the main language spoken in Brazil.

</details>





## Test 21

### Inputs

* **Query:** Who discovered penicillin?
* **Ground truth:** Alexander Fleming

### Eval Scores

| Evaluator | |
| :-------- |  ---: |
| coherence | 4.0 |
| relevance | 5.0 |
| intent_resolution | 5.0 |




### Raw Outputs

<details>

Alexander Fleming discovered penicillin.

</details>



