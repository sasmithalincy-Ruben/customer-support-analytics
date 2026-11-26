# Customer Support Analytics

## Project Overview
This project analyzes customer support ticket data to understand support performance, response efficiency, ticket resolution, and customer satisfaction.

The project uses Python for data cleaning, SQL for data analysis, and Power BI to build an interactive dashboard that presents key customer support metrics.

## Business Objectives
- Monitor total and resolved support tickets
- Measure ticket resolution rate and open ticket volume
- Analyze ticket distribution by channel and priority
- Evaluate average first response time
- Compare average resolution time across ticket priorities
- Understand customer satisfaction (CSAT) by support channel

## Tools & Technologies
- **Python:** Pandas, data cleaning and preprocessing
- **SQL:** SQLite, aggregation and analytical queries
- **Power BI:** Dashboard development and visualization
- **VS Code:** Development environment
- **Git & GitHub:** Version control and project hosting

## Project Structure
```text
customer-support-analytics/
├── data/
│   ├── support-tickets.csv
│   ├── support-tickets-cleaned.csv
│   └── support_tickets.db
├── powerbi/
│   └── Customer Support Analytics.pbix
├── python/
│   ├── inspect_data.py
│   └── load_to_sqlite.py
├── sql/
│   └── support_analysis.sql
└── .gitignore
```

## Key Metrics
- Total Tickets
- Resolved Tickets
- Open Tickets
- Resolution Rate
- Average First Response Time
- Average Resolution Time
- Average Customer Satisfaction (CSAT)

## Key Insights
- Chat had the fastest average first response time among the support channels.
- In-app support had the slowest average first response time.
- Low-priority tickets had the longest average resolution time.
- Urgent tickets had the shortest average resolution time.
- Chat had the highest average CSAT among the channels analyzed.
- The overall ticket resolution rate was approximately **94.37%**.

## Dashboard
The Power BI dashboard provides a visual overview of ticket volume, priority distribution, response time, resolution time, and customer satisfaction.![Customer Support Analytics Dashboard](./powerbi/power%20bi%20dashboard.png)

## Project Outcome
This project demonstrates practical skills in data cleaning, SQL analysis, KPI development, dashboard creation, and translating data into business insights.

## Author
**Sasmitha Lincy Ruben**  
Aspiring Data Analyst
