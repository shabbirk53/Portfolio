# E-Commerce Sales & Customer Cohort Analysis

**Author:** Shabbir Kutbuddin  
**Portfolio:** [github.com/shabbirk53/Portfolio](https://github.com/shabbirk53/Portfolio)

---

## Overview

End-to-end data analysis of a Brazilian e-commerce platform (Olist-style dataset), covering 2,000 orders across 723 customers over 18 months (Jan 2022 – Jun 2023).

## Objectives

- Analyse monthly revenue trends and seasonal patterns
- Break down performance by product category and region
- Build a customer cohort retention heatmap
- Segment customers by purchase frequency (LTV proxy)
- Surface actionable business recommendations

## Stack

| Tool | Purpose |
|------|---------|
| Python / Pandas | Data wrangling & aggregation |
| pandasql | SQL queries against DataFrames |
| Matplotlib / Seaborn | Static visualisations |
| React / Recharts | Interactive dashboard |

## Files

```
├── ecommerce_analysis.ipynb     # Full analysis notebook
├── ecommerce_dashboard.jsx      # Interactive React dashboard
├── data/
│   └── orders_sample.csv        # Synthetic dataset (2,000 orders)
└── README.md
```

## Key Findings

1. **Electronics** is the highest-revenue category at R$55k despite ~9.5% of orders — driven by 1.4× AOV premium
2. **Aug–Sep 2022 dip** of ~35% revenue indicates a seasonal pattern requiring proactive promotional planning
3. **72.5% repeat purchase rate** — strong baseline retention for an e-commerce platform
4. Cohorts stabilise at an **8–15% monthly retention floor** from M+2, indicating a loyal core segment
5. **Salvador (BA) and Curitiba (PR)** outperform São Paulo on revenue despite lower population — underserved market opportunity

## How to Run

```bash
pip install pandas numpy matplotlib seaborn pandasql
jupyter notebook ecommerce_analysis.ipynb
```

---

*Dataset is synthetic, modelled on Olist Brazilian E-Commerce patterns.*
