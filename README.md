# E-Commerce Analytics Project

## Project Overview
This project analyzes e-commerce sales data to identify trends, top products, top customers, and provide machine learning predictions for sales forecasting.

## Dataset
- **Size:** 541,909 transactions
- **Date Range:** 2010-12-01 to 2011-12-09
- **Columns:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- **Source:** Real e-commerce transaction data

## Project Structure
```
ecommerce-analytics-project/
├── data/
│   ├── raw/
│   │   └── data.csv                
│   └── processed/
│       └── cleaned_data.csv         
├── src/
│   ├── data_analysis.py           
│   ├── feature_engineering.py    
│   ├── eda.py                      
│   ├── advanced_eda.py             
│   └── model.py                    
├── sql_queries/
│   ├── basic_queries.sql          
│   └── analysis_queries.sql    
├── visualizations/
│   ├── sales_analysis.png          
│   ├── top_products.png           
│   ├── top_customers.png       
│   ├── price_distribution.png     
│   └── top_10_countries.png       
├── models/
│   └── sales_model.pkl             
├── requirements.txt               
├── .gitignore                    
└── README.md                       
```

## Installation

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Steps
1. Clone the repository
```bash
git clone https://github.com/yourusername/ecommerce-analytics-project.git
cd ecommerce-analytics-project
```

2. Create virtual environment
```bash
python -m venv venv
```

3. Activate virtual environment
```bash
venv\Scripts\activate

source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run Data Analysis
```bash
python src/data_analysis.py
```
Initial exploration of the dataset - shows first 5 rows, dataset info, and basic statistics.

### Run Feature Engineering
```bash
python src/feature_engineering.py
```
Creates new features from existing data (Month, DayOfWeek, TotalAmount).

### Run EDA Visualizations
```bash
python src/eda.py
```
Generates basic visualizations - sales by month and day of week.

### Run Advanced EDA
```bash
python src/advanced_eda.py
```
Creates advanced visualizations:
- Top 10 products by sales
- Top 10 customers by spending
- Top 10 countries by sales
- Price distribution histogram

### Train ML Model
```bash
python src/model.py
```
Trains RandomForest model for sales prediction. Model saved to `models/sales_model.pkl`.
- Model Performance: R² Score = 0.5711 (57% accuracy)

## Key Insights

### Sales Trends
- **Peak Month:** November has the highest sales (~1.5M)
- **Weekly Pattern:** Wednesday (Day 3) has the most sales
- **Seasonal Effect:** Strong increase towards end of year (Christmas shopping)

### Top Performers
- **Best Product:** DOT with ~200K in sales
- **Best Customer:** Customer 14646.0 spent ~280K total
- **Top Country:** United Kingdom dominates with highest total sales

### Customer Behavior
- **Price Distribution:** Most products are budget-friendly ($0-5 range)
- **Customer Base:** 4,068 unique customers from 38 countries
- **Transaction Volume:** 541,909 total transactions

### Business Recommendations
1. Focus marketing on November/December for seasonal demand
2. Target high-value customers (top 10 customers = 20% of revenue)
3. Maintain inventory for top products (DOT, 22423, etc.)
4. Implement retention strategy for inactive customers (>90 days without purchase)

## Technologies Used

### Data Processing & Analysis
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Python 3.11** - Programming language

### Machine Learning
- **Scikit-learn** - ML algorithms (RandomForest)
- **Sklearn.metrics** - Model evaluation (MSE, R² Score)

### Data Visualization
- **Matplotlib** - Plotting library
- **Seaborn** - Statistical data visualization

### Database & Queries
- **SQL** - Data analysis queries

### Version Control
- **Git & GitHub** - Code repository and version control

### Development Environment
- **Virtual Environment (venv)** - Package isolation
- **Jupyter** - Interactive notebooks (optional)

## Machine Learning Model

### Model Type
- **Algorithm:** Random Forest Regressor
- **Task:** Sales Amount Prediction
- **Input Features:** Quantity, UnitPrice, Month, DayOfWeek
- **Target Variable:** TotalAmount (Quantity × UnitPrice)

### Model Performance
```
Training Set Size: 379,336 samples (70%)
Test Set Size: 379,336 samples (30%)

Metrics:
- Mean Squared Error (MSE): 99691.13
- R² Score: 0.5711 (57.11% accuracy)
```

### Interpretation
- The model explains ~57% of variance in sales amount
- Reasonable performance for initial model
- Can be improved with feature engineering and hyperparameter tuning

### Model Usage
```python
import pickle

# Load trained model
with open('models/sales_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(test_data)
```

## SQL Analysis Queries

All SQL queries are located in `sql_queries/analysis_queries.sql`

### Available Queries

1. **Top 10 Countries by Sales**
   - Identifies best-performing markets
   - Useful for regional strategy planning

2. **Top 10 Products by Revenue**
   - Shows most profitable products
   - Includes transaction count for each product

3. **Monthly Sales Trend**
   - Tracks sales over time
   - Identifies seasonal patterns

4. **Top 10 Customers by Spending**
   - Identifies VIP/high-value customers
   - Helps with customer retention strategy

5. **Data Quality Check**
   - Validates dataset completeness
   - Shows date range, price ranges, averages

6. **Inactive Customers (>90 days)**
   - Finds customers who haven't purchased recently
   - Target for re-engagement campaigns

### Running Queries
To execute these queries, import the data into a SQL database and run the `.sql` file.

## Future Improvements

### Model Enhancements
- [ ] Add more features (customer age, product category, seasonality indicators)
- [ ] Try different algorithms (Gradient Boosting, XGBoost, Neural Networks)
- [ ] Hyperparameter tuning for better accuracy
- [ ] Cross-validation for more robust evaluation
- [ ] Feature importance analysis

### Data Analysis
- [ ] Time series analysis for forecasting
- [ ] Customer segmentation clustering
- [ ] Sentiment analysis on product descriptions
- [ ] Anomaly detection for fraud/errors

### Visualization
- [ ] Interactive dashboards (Plotly, Dash)
- [ ] Real-time monitoring dashboard
- [ ] Geographical heatmaps

### Deployment
- [ ] REST API for model predictions
- [ ] Web application interface
- [ ] Database integration (PostgreSQL, MongoDB)
- [ ] Docker containerization

## Author
- **Name:** Demian Pyrih
- **Email:** demianpyrih@gmail.com
- **GitHub:** https://github.com/DemianPyrih25
- **LinkedIn:** https://www.linkedin.com/in/demian-pyrih-720214336/

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Dataset source: E-commerce transaction data
- Built as a portfolio project for data science/analytics roles
- Technologies: Python, SQL, Machine Learning, Data Visualization

## Questions or Feedback?
Feel free to open an issue on GitHub or contact me directly.