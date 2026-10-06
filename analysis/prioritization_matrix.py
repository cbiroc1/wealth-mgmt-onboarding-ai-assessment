# AI Opportunity Prioritization Matrix
# y = AI Value Potential = Composite Score column from the Scored Matrix tab (workbook's own weighted blend of all 5 scoring dimensions)
# x = Implementation Complexity = 6 - avg(Data Availability, Risk Level Inverse)- low data access or high regulatory risk pushes complexity up
from pathlib import Path

import matplotlib.pyplot as plt

# Scores below are copied from the Scored Matrix tab of deliverables/opportunity_matrix.xlsx
steps = {
    "1. Discovery": (3.0, 2.90),
    "2. KYC/AML": (3.5, 3.20),
    "3. Suitability": (3.5, 3.10),
    "4. Account Setup": (2.0, 3.95),
    "5. IPS Creation": (2.5, 3.10),
    "6. Portfolio": (3.5, 3.25),
    "7. Welcome/CRM": (1.5, 4.30),
}

# Thresholds
complexity_threshold = 2.8
value_threshold = 3.4

# Automatically classify each opportunity
def quadrant(complexity, value):
    if complexity < complexity_threshold and value >= value_threshold:
        return "Quick Wins"
    elif complexity >= complexity_threshold and value >= value_threshold:
        return "Strategic Bets"
    elif complexity >= complexity_threshold and value < value_threshold:
        return "Low Priority"
    else:
        return "Optimize / Monitor"

# Create matrix
fig, ax = plt.subplots(figsize=(11, 7))

for step, (complexity, value) in steps.items():
    ax.scatter(complexity, value, s=90)
    ax.annotate(
        step,
        (complexity, value),
        xytext=(8, 7),
        textcoords="offset points",
        fontsize=9
    )

# Draw quadrant thresholds
ax.axvline(complexity_threshold, linestyle="--", linewidth=1)
ax.axhline(value_threshold, linestyle="--", linewidth=1)

# Quadrant labels
ax.text(1.15, 4.55, "QUICK WINS", fontsize=11, fontweight="bold")
ax.text(3.15, 4.55, "STRATEGIC BETS", fontsize=11, fontweight="bold")
ax.text(1.15, 2.55, "OPTIMIZE / MONITOR", fontsize=11, fontweight="bold")
ax.text(3.15, 2.55, "LOW PRIORITY", fontsize=11, fontweight="bold")

# Formatting
ax.set_xlim(1.0, 4.0)
ax.set_ylim(2.5, 4.6)
ax.set_xlabel("Implementation Complexity →")
ax.set_ylabel("AI Value Potential →")
ax.set_title("AI Opportunity Prioritization Matrix")
ax.grid(True, alpha=0.25)

plt.tight_layout()

# Save the chart next to this script so the repo always has the latest version
output_path = Path(__file__).with_name("prioritization_matrix_2x2_graph.png")
plt.savefig(output_path, dpi=100)
plt.show()

# Print classifications
print("Quadrant classification:")
for step, (complexity, value) in steps.items():
    print(f"{step}: {quadrant(complexity, value)}")