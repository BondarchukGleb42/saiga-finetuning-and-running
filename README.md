# Saiga-Mistral finetuning and running in Docker with FastAPI
RuLLM Saiga finetuning, quantization, inference with llama cpp library and running in Docker with FastAPI

В репозитории реализован jupyter-notebook для дообучения и квантизации русскоязычной LLM Saiga. Также есть пример импорта обученной заквантованной модели и запуска на llama-cpp с использованием GPU. Поддерживается multi-gpu. В целом, пайплайн можно использовать для дообучения любых других LLM c hugging face (но не уверен, что квантизация будет работать с ними - не проверял). На Saiga13b и Saiga70b тоже работает.  
Также, представлен готовый образ для запуска обученной модели на гпу из докера в обёртке FastAPI. Предварительно необходимо поместить модель в ту же директорию, где докерфайл (назвать *model.gguf* или поменять *MODEL_NAME* в main.py). 
main.py и requirements.txt можно менять в зависимости от задачи, докерфайл подтягивает их при билде.  
Запускать как всегда:  
```cmd
docker compose up
```
