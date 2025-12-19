# research question
The proposed research hypothesis is: "There is a negative correlation between the proportion of women in parliamentary seats and ministerial positions and the percentage of women who justify wife-beating across different countries and time periods."

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
