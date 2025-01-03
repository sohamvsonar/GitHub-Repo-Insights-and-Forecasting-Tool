# GitHub Repo Insights and Forecasting Tool

This project provides an end-to-end solution for analyzing and forecasting trends in GitHub repositories. Using historical data, the tool generates insights into repository activity, such as issue creation patterns, resolutions, and trends, and applies forecasting models to predict future repository dynamics

## Project Overview
- Fetch and preprocess data from GitHub repositories (e.g., issues, pull requests).  
- Analyze key metrics like the number of open/closed issues, average resolution times, etc.  
- Visualize trends using time series plots and interactive dashboards.  
- Apply machine learning models (e.g., ARIMA, LSTM) to forecast future repository activity.  
- Generate actionable insights to help maintainers and contributors manage repositories effectively.
- In the Analytics file I have used OpenAI's text-embedding-ada-002 model to generate embeddings for the search queries and the semantic search is performed using Elasticsearch.

### Key Features
- **Data Retrieval**: Uses the GitHub API to retrieve issues data for the past two months and two years (for different analyses).
- **Visualization**: Creates charts to visualize historical trends in issues.
- **Forecasting**: Implements time-series forecasting models to predict future issue trends.
- **Repositories Tracked**:
  - [LangChain](https://github.com/langchain-ai/langchain)
  - [LangGraph](https://github.com/langchain-ai/langgraph)
  - [AutoGen](https://github.com/microsoft/autogen)
  - [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
  - [Elasticsearch](https://github.com/elastic/elasticsearch)
  - [PyMilvus](https://github.com/milvus-io/pymilvus)

## Requirements
1. **Retrieve Issues Data**: Fetch issue information for the above repositories over the last two months (semantic search) and two years (visualization).
2. **Generate Visualizations**: Plot issue trends using Python libraries.
3. **Forecast Future Issues**: Apply forecasting techniques to predict future issue counts.

## Setup Instructions

### Prerequisites
- Python 3.8+
- GitHub personal access token (required for API authentication)
- Python libraries: `pandas`, `matplotlib`, `seaborn`, `statsmodels`, `prophet`, `requests`, `tensorflow`, `scikit-learn`

### Part 1: File - GitHub_Repos_Issues_Forecasting.ipynb
- Ensure that all required libraries are installed before executing this notebook.
- Plots and forecast results are included within the Jupyter notebook.

1. Backend - Flask
To run the backend, navigate to the Flask directory and execute the following command in a separate terminal:

```bash
python App.py
```

2. Frontend - React

Install the necessary node_modules packages by executing:
```bash
npm install
```

Start the frontend server locally by running:
```bash
npm start
```
(This should be executed in a separate terminal)

This would start a web server with all the forecasting results.

Part 2: File - Analytics.ipynb
Updates in the Directory - 'GitHub_Issues_ES_Docker_OpenAI'

Uploaded these changes to Elasticsearch using Docker.
Subsequently, the notebook Analytics.ipynb retrieves the Top 5 most similar issues from Elasticsearch.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/sohamvsonar/github-issues-forecasting.git
   cd github-issues-forecasting
   ```
2. Add your GitHub personal access token:
   Update the `GITHUB_TOKEN` variable in the notebook or environment variables.
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook GitHub_Repos_Issues_Forecasting.ipynb
   ```
4. Run the notebook to analyze and forecast GitHub repository issues.

## Deliverables
- **Jupyter Notebook**: `GitHub_Repos_Issues_Forecasting.ipynb` containing the source code and outputs.
- **Analysis Report**: A detailed PDF or HTML document summarizing the findings and results.



## Results
- Clear visualizations of issue trends over the past two years.
- Accurate forecasts of future issue trends for better repository management.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions.

## Acknowledgments
- [GitHub API Documentation](https://docs.github.com/en/rest)
- Python libraries: `matplotlib`, `pandas`, `statsmodels`, `prophet`, `LSTM`

---

### Author
Developed by [Soham Sonar](https://github.com/sohamvsonar).

