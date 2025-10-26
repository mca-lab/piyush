# Big Data Project Template

## Project Overview

Build a Big Data project using Python, PySpark and Docker. The workflow includes:

1. Data ingestion from multiple sources
2. Data cleaning and integration
3. Analysis and visualization
4. Reproducible Docker-based setup for data collection and processing

pick **2 or more datasets**, define a **research question or hypothesis** and implement the pipeline.

---

## Project Workflow

### Module 1. Data Collection & Ingestion

**Objective:** Automate downloading datasets and storing them for processing.

**Tasks:**

- Choose 2+ public datasets (Kaggle, Data.gov, WHO, World Bank, UCI, etc.)
- Write Python script to fetch datasets dynamically (URLs, APIs, Kaggle datasets)
- Store raw datasets in `data/raw/`
- Optional: convert datasets to Parquet for efficient storage
- Docker container ensures uniform data collection environment

**Deliverables:**

- `Dockerfile` + `requirements.txt`
- Scripts in `src/` (e.g., `fetch_data.py`)
- `data/raw/` populated when container runs

---

### Module 2. Data Cleaning & Integration

**Objective:** Prepare raw data for analysis using PySpark.

**Tasks:**

- Load raw datasets into PySpark
- Handle missing values, inconsistent formats, duplicates
- Merge, join or aggregate datasets as required
- Store processed data in `data/processed/`
- Docker container ensures reproducible cleaning pipeline

**Deliverables:**

- `Dockerfile` + `requirements.txt` for cleaning
- Scripts in `src/` (e.g., `clean_data.py`)
- `data/processed/` ready for analysis

---

### Module 3. Data Analysis & Visualization

**Objective:** Explore and analyze cleaned datasets to answer the research question.

**Tasks:**

- Load processed data in Jupyter Notebook
- Perform descriptive statistics, correlations, aggregations or regression or other appropiate analysis methods
- Visualize using Matplotlib, Seaborn or Plotly
- Document findings and interpretations in notebook cells

**Deliverables:**

- Jupyter Notebook(s) in `/notebooks/`
- Plots and charts illustrating key insights
- Problem statement, explanation and conclusion in the README.md

---

## Technologies

- Python
- PySpark
- Matplotlib, Seaborn, Plotly
- Docker

---

## Notes

- Module 1 and Module 2 require Docker for reproducibility
- Module 3 is executed in Jupyter Notebook (no Docker required)
- End goal: automated pipeline from data fetching → cleaning → analysis → insights

## Git Configuration

- Use `.gitignore` file to prevent large or sensitive files, cache files and any other unnecessary files and folders from being committed.
- Do not commit raw or processed datasets to the repository.
- Do not commit python cache files, notebook checkpoints, virtual environments
- Only commit scripts, notebooks, Docker setup and README.
- Do not commit raw or processed datasets to the repository.
- Only commit scripts, notebooks, Docker setup and README.

---

## To Get Started

1. **Fork the Template**:

   - Click **Use this template → Create a new repository**.
   - Select the organization namespace for the forked repository.

2. **Clone Your Repository**:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
3. **Work Locally**:

   - Implement data fetching, cleaning and analysis in your forked repo.
   - Commit and push changes to your repository

4. **(optional) Pull Updates from Template (if updated)**:

   - Add the template repository as an upstream remote:

   ```bash
   git remote add upstream https://github.com/<org-name>/big-data-template.git
   git fetch upstream
   git merge upstream/main
   ```

---

## Running the Data Pipeline with Docker

These steps will build your Docker image and run the container, ensuring the collected and processed data is saved to a local folder named `data` in your current directory.

### Step 1: Build the Docker Image

Run this command in the project root directory (where the `Dockerfile` is located):

```bash
docker build -t bigdata .
```

### Step 2: Run the Docker Container

Use a bind mount to link your host machine's local data folder to the container's /data directory.

**Option A:** Recommended for Windows PowerShell/Command Prompt This uses the current directory variable ${PWD} to ensure portability on your machine.

```bash
docker run -v ${PWD}/data:/data bigdata
```

**Option B:** Using an Absolute Windows Path Replace the path with your exact local project folder:

```bash
docker run -v C:\Users\piyus\Desktop\5TH_SEM\BIG_DATA\piyush\data:/data bigdata
```
