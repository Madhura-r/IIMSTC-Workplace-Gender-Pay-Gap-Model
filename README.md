# IIMSTC-Workplace-Gender-Pay-Gap-Model
Mini Project - Workplace Gender Pay Gap Analysis using Dummy Variables and Comparative Regression (SDG 5)


Setup and Installation
Follow these steps to prepare your environment and run the model.

Option 1: Google Colab
For a quick-start execution without local configuration:
1.	Upload the notebook to your Google Drive.
2.	Open the file in Google Colab.
3.	Execute the cells sequentially from top to bottom.

Option 2: Local Environment (VS Code / Jupyter Notebook)
Follow these steps to configure your local environment and execute the model:
Step 1: Environment Creation
Create a dedicated virtual environment to manage dependencies:
python -m venv venv_gender_gap
Step 2: Environment Activation
Activate the environment based on your operating system:
•	Windows: .\venv_gender_gap\Scripts\activate
•	macOS/Linux: source venv_gender_gap/bin/activate
Step 3: Verify Tools
Check that your core components are correctly installed:
python --version
pip --version
jupyter --version
Step 4: Install Dependencies
Install the required Python packages:
!pip install kagglehub statsmodels seaborn joblib scipy scikit-learn matplotlib pandas numpy

Execution Workflow
Once your environment is set up, the project follows these sequential steps:
Phase 1: Data Initialization
1.	Library Imports: Load essential libraries (Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn).
2.	Data Ingestion: Download the dataset using the kagglehub API or load it from your local file path.
Phase 2: Data Preprocessing
3.	Data Cleaning: Handle missing values and resolve data inconsistencies.
4.	Statistical Analysis: Review descriptive statistics to understand data structure.
5.	Outlier Handling: Detect and manage anomalies using cap-range methods.
6.	Feature Engineering: Address skewness and create new features to improve model accuracy.
7.	Data Persistence: Save the cleaned dataset for future use.
Phase 3: Modeling and Evaluation
8.	Model Definition: Configure the predictive architecture for salary estimation.
9.	Data Partitioning: Split the dataset into Training and Testing sets.
10.	Evaluation: Generate model summaries and calculate performance metrics (MAE, RMSE, R²).
11.	Validation: Perform Cross-Validation to ensure the model generalizes well to new data.
Phase 4: Visualization & Insights
12.	Visual Analysis: Generate charts for:
o	Gender Salary Distribution.
o	Salary vs. Experience by Gender.
o	Average Salary by Education Level and Gender.
Phase 5: Finalization
13.	Summary: Review the final model findings and drivers of the pay gap.
14.	Save Model: Export the final trained model for deployment or inference.