
# Composite KPI

## Overview
Composite KPI is a data-driven project designed to calculate a comprehensive performance index using five core KPIs:

- 1.Net Sales
- 2.Margin
- 3.Product Mix
- 4.NPS
- 5.Sales from New Products

The project leverages advanced weighting methods such as PCA (Principal Component Analysis), Entropy, and CRITIC to generate an optimized composite index.
The dataset (synthetic) covers 60 monthly records from September 2020 over a 5-year period.

---

## Prerequisites
- Conda (Anaconda or Miniconda)
- Python 3.10 or higher
- Git

---

## Key Objectives
- Develop a composite performance index using multiple KPIs.
- Apply advanced weighting methods to generate robust weights for KPIs:
  - PCA (Principal Component Analysis)
  - Entropy Method
  - CRITIC Method
- Integrate sub-KPIs into the composite index calculation:
  - net_sales_adj
  - margin_pct
  - nps
  - sales_new_pct_of_sales
  - pm_refrigerator_pct
  - pm_washer_pct
  - pm_oven_pct
  - pm_other_pct
  
---

## Methodology
1. **Data Creation & Preprocessing**  
   - Synthetic monthly data spanning 60 months from September 2020, covering 5 main KPIs.  
   - adjustment, EDA analysis, normalization, and standardization of KPIs.   

2. **Weight Calculation**  
   - PCA: Extract principal components and determine contribution of each KPI.  
   - Entropy Method: Measure the information content of each KPI to assign weights.
   - CRITIC Method: Combine contrast intensity and conflict among KPIs to calculate robust weights.
   - calculating the average of weights and use it. 

3. **Composite Index Calculation**  
   - Aggregate weighted KPIs and sub-KPIs into a single composite score per month.  
   - Enable comparison across time periods and KPI categories for business performance analysis.  

---

## Results
- Successfully generated a robust composite KPI index reflecting overall performance trends.
- Demonstrated that weighting methods (PCA, Entropy, CRITIC) produce slightly different but consistent rankings of KPI importance.
- Approach provides a scalable framework for adding new KPIs or updating weights as business needs evolve.

---

## Project Structure

composite-kpi/
│
├── data/               
│   ├── dummy/ 
│   ├── normalized/  
│   ├── output/  
│   ├── pca/        
│   ├── preprocessing/
│   │   ├── eda_results/  
│   ├── satandardization/        
│   └── weights/
│       ├── ahp/
│       ├── critic/
│       ├── entropy/
│       └── pca-weights/   
│  
├── src/                
│   ├── __init__.py
│   ├── adjustment.py       
│   ├── composite-index.py
│   ├── correlation.py       
│   ├── cpi_generator.py
│   ├── critic.py       
│   ├── data_generator.py
│   ├── eda.py 
│   ├── entropy.py       
│   ├── Normalization.py       
│   ├── pca_weights.py             
│   └── Standardization.py 
│    
│── environment.yml 
│── LICENSE
└── README.md


---

## Installation

To run this project, it is recommended to use **Conda** to recreate the exact environment used in development. Follow the steps below:

1. **Clone the repository:**
```bash
git clone https://github.com/MohammadGholami-MG/Composite-KPI
cd Composite-KPI
2. **Create the Conda environment:**
conda env create -f environment.yml
3. **Activate the environment:**
conda activate composite-kpi

```

## Technologies Used
- **Python 3.10+**
- **Scikit-learn**
- **Pandas, NumPy, Matplotlib, Seaborn**

---

## Author
**Mohammad Gholami**  
LinkedIn: https://www.linkedin.com/in/mohammad-gholami-mgh22

---

## Contributing

We welcome contributions! To contribute:

1.Fork the repository.
2.Create a new branch (git checkout -b feature/YourFeature).
3.Make your changes and commit them (git commit -m 'Add YourFeature').
4.Push to the branch (git push origin feature/YourFeature).
5.Create a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

