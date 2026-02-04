# 🚀 Learning FastAPI

Welcome to **Learning-FastAPI**! This repository documents my journey as an **AI Engineer** learning **FastAPI** to build robust, high-performance APIs for deploying Machine Learning models.

## 📖 About This Repository

This repository is a structured collection of examples and exercises covering the core concepts of FastAPI. It starts from the basics and progresses to more advanced topics like validation, nested models, and complex request bodies.

My goal is to bridge the gap between model development and model deployment, ensuring that my AI solutions are production-ready.

## 🎯 Why I Created This Repo

As an AI Engineer, building the model is only half the battle. Serving that model efficiently to users or other systems is equally critical. I created this repository to:

- **Create a reference** for future projects involving ML deployment.
- **Deepen my understanding** of modern web frameworks.
- **Practice best practices** in API development.

## 📂 Folder Structure

Each folder corresponds to a specific topic or concept in FastAPI:
| Folder | Description |
| :---------------------------- | :-------------------------------------------------------- |
| `1- Intro` | Basic setup, first API endpoints, and "Hello World". |
| `2- Path_Parameters` | Handling dynamic path variables in URLs. |
| `3- Query_Parameters` | Filtering and sorting data using query strings. |
| `4- Request_Body` | Sending JSON data to the API using Pydantic models. |
| `5- String_Validation` | Enforcing constraints and validation on string inputs. |
| `6- Numeric_Validation` | Validating integer and float inputs. |
| `7- Body_Multiple_Parameters` | Handling mixed path, query, and multiple body parameters. |
| `8- Fields` | Advanced field validation and metadata for models. |
| `9- Nested_Models` | Working with hierarchical JSON structures. |

## 🛠️ Getting Started

Follow these steps to clone and run the code examples locally.

### Prerequisites

- Python installed on your machine.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohamed-abdelazizz/Learning-FastAPI.git
   cd Learning-FastAPI
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   # On Windows:
   .\env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 How to Run Examples

You can run any example file using `uvicorn`. Navigate to the specific folder and run the api.

**Example: Running the Intro API**

```bash
cd 1- Intro
uvicorn api:app --reload
```

_Note: Replace `api` with the name of the python file if it differs, and ensure the FastAPI instance is named `app`._

Once the server is running, open your browser and navigate to:

- **API**: `http://127.0.0.1:8000`
- **Interactive Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`
