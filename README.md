# Analysis of the World's Billionaires in 2021
[![Format](https://github.com/nogibjj/zihan_polar_project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/zihan_polar_project/actions/workflows/format.yml)[![Install](https://github.com/nogibjj/zihan_polar_project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/zihan_polar_project/actions/workflows/install.yml)[![Lint](https://github.com/nogibjj/zihan_polar_project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/zihan_polar_project/actions/workflows/lint.yml)[![Test](https://github.com/nogibjj/zihan_polar_project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/zihan_polar_project/actions/workflows/test.yml)

**A quick tour of this project**([Demo Video.mp4](https://youtu.be/KVoo54Emnjs))

## Dataset Introduction

The [data file](Billionaire_2021.csv) used in this analysis is a comprehensive list of all the world's billionaires as of 2021. This dataset is sourced from the prestigious Forbes Billionaires List, which is widely recognized as one of the most authoritative rankings of global wealth.

Key features of the dataset:
- It includes billionaires from various countries and industries.
- The data provides insights into the distribution of extreme wealth across the globe.
- Each entry contains information such as net worth, source of wealth, and country of origin.

This analysis aims to provide a descriptive statistical overview of the world's billionaire population, offering insights into wealth distribution, geographical trends, and other relevant patterns.

If you need to refer to a **summary report** containing **detailed analysis**, **data**, and **charts**, [click here](Panda_Descriptive_Project.ipynb).

## Project Structure

* Python script (`.py`) together with the Jupyter Notebook (`.ipynb`) is provided for the analysis.
* A Markdown file (`.md`) is provided as the report of the analysis.
* By running the `.py` file, a graph (`.png`) will be generated automatically, visualizing key aspects of the data.

## Generating the Markdown Report

To generate the markdown file from the Jupyter Notebook, you can run the following code in the terminal:

```bash
pip install jupyter nbconvert
```
```bash
jupyter nbconvert --to markdown filename.ipynb
```

## Setup Instructions
To set up this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```
   
2. **Navigate to the project directory**:
    ```bash
    cd your-repo-name
    ```

3. **Build the Docker container** (if you are using Docker):
    ```bash
    docker build -t your-container-name .
    ```

4. **Install the required packages** using the `Makefile`:
    ```bash
    make install
    ```

   This command will install all the necessary dependencies listed in `requirements.txt`.

## Usage Instructions
To use this project:

1. **Run the `main.py` file** to check the data and descriptive statistics:
    ```bash
    python main.py
    ```

2. **Run the tests** using:
    ```bash
    pytest
    ```

3. **Lint the code**:
    ```bash
    make lint
    ```

4. **Format the code**:
    ```bash
    make format
    ```

By following these instructions, you will be able to set up and run the project smoothly.
