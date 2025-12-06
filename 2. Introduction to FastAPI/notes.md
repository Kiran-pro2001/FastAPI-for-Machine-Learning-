1. Create virtual environment 


python -m venv demo        
source demo/bin/activate




| Purpose              | Using `pip` (with `venv`)         | Using `uv`                  |
| -------------------- | --------------------------------- | --------------------------- |
| Create venv          | `python -m venv venv`             | `uv venv`                   |
| Activate (Mac/Linux) | `source venv/bin/activate`        | `source .venv/bin/activate` |
| Activate (Windows)   | `venv\Scripts\activate`           | `.venv\Scripts\activate`    |
| Install package      | `pip install fastapi`             | `uv add fastapi`            |
| Install from file    | `pip install -r requirements.txt` | `uv sync`                   |
| Save dependencies    | `pip freeze > requirements.txt`   | `uv lock`                   |
| Deactivate venv      | `deactivate`                      | `deactivate`                |
| Delete venv          | `rm -rf venv`                     | `rm -rf .venv`              |
