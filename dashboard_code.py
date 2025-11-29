import matplotlib.pyplot as plt
import numpy as np

# ====================================================
# 1) HR KPI – Employee Count by Department
# ====================================================

# This chart shows how many employees work in each department.
departments = ["HR", "IT", "Sales", "Finance", "Operations"]
employee_count = [12, 35, 50, 22, 40]

plt.figure()
plt.bar(departments, employee_count, color="orange")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Employees")
plt.tight_layout()
plt.savefig("employee_count_department.png")
plt.close()

# ====================================================
# 2) HR KPI – Monthly Turnover Rate (%)
# ====================================================

# This chart shows the monthly employee turnover rate (%).
months = np.arange(1, 13)
turnover_rate = [3.2, 2.3, 4.3, 3.1, 3.75, 4.45,
                 3.4, 1.7, 4.1, 4.35, 2.28, 1.97]

plt.figure()
plt.plot(months, turnover_rate, marker="o", color="orange")
plt.title("Monthly Turnover Rate (%)")
plt.xlabel("Month")
plt.ylabel("Turnover %")
plt.xticks(months)
plt.tight_layout()
plt.savefig("monthly_turnover_rate.png")
plt.close()

# ====================================================
# 3) Customer Analytics – Customer Churn by Region
# ====================================================

# This chart compares customer churn (%) across regions.
regions = ["Ankara", "İstanbul", "İzmir", "Bursa", "Antalya"]
churn_rates = [5.2, 8.1, 4.7, 6.0, 3.9]

plt.figure()
plt.bar(regions, churn_rates, color="orange")
plt.title("Customer Churn by Region (%)")
plt.xlabel("Region")
plt.ylabel("Churn %")
plt.tight_layout()
plt.savefig("customer_churn_region.png")
plt.close()

# ====================================================
# 4) Financial Dashboard – Monthly Revenue (TL)
# ====================================================

# This chart shows simulated monthly revenue for one year.
monthly_revenue = [245000, 238000, 239500, 103000, 112000, 159000,
                   222000, 213000, 197000, 186000, 126000, 157000]

plt.figure()
plt.plot(months, monthly_revenue, marker="s", color="orange")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (TL)")
plt.xticks(months)
plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.close()

# ====================================================
# 5) Operational Performance – Delivery Performance
# ====================================================

# This chart shows on-time vs delayed deliveries (%).
labels = ["On Time", "Delayed"]
values = [82, 18]

plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%", colors=["orange", "skyblue"])
plt.title("Delivery Performance")
plt.tight_layout()
plt.savefig("delivery_performance.png")
plt.close()

print("All dashboard images have been successfully generated!")
