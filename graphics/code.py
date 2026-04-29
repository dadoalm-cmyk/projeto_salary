# =========================
# IMPORTS
# =========================
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# =========================
# DATA
# =========================
df = pd.read_csv("C:/Users/dadoa/Downloads/archive (11)/job_salary_prediction_dataset.csv")

# =========================
# FUNÇÃO PADRÃO
# =========================
def aplicar_layout(fig, titulo, x_title="", y_title=""):
    fig.update_layout(
        width=900,
        height=500,
        template="plotly_white",
        font=dict(family="Arial", size=14, color="#1a1a1a"),
        title=dict(text=titulo, font=dict(size=24)),
        xaxis=dict(title=x_title),
        yaxis=dict(title=y_title)
    )
    return fig

# =========================
# 1. Salary vs Experience
# =========================
exp_salary = df.groupby("experience_years")["salary"].mean().reset_index()

fig = px.line(exp_salary, x="experience_years", y="salary")

fig.update_traces(
    line=dict(color="#0B6E4F", width=4),
    marker=dict(size=8, color="#08A045"),
    mode="lines+markers"
)

fig = aplicar_layout(fig, "Salary vs Experience", "Years of Experience", "Salary")
fig.show()

# =========================
# 2. Salary by Education
# =========================
fig = px.box(
    df,
    x='education_level',
    y='salary',
    color='education_level',
    color_discrete_sequence=["#0B6E4F", "#08A045", "#6BBF59", "#9BE564"]
)

fig = aplicar_layout(fig, "Salary by Education Level", "Education Level", "Salary")
fig.show()

# =========================
# 3. Top 10 Locations
# =========================
loc_salary = (
    df.groupby('location')['salary']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = go.Figure(go.Bar(
    x=loc_salary['salary'],
    y=loc_salary['location'],
    orientation='h',
    marker=dict(
        color=loc_salary['salary'],
        colorscale='Greens',
        showscale=False
    )
))

fig = aplicar_layout(fig, "Top 10 Locations by Salary", "Salary", "Location")
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()

# =========================
# 4. Boxplot Top Locations
# =========================
top_loc = loc_salary['location']
df_top = df[df['location'].isin(top_loc)]

fig = px.box(
    df_top,
    x='location',
    y='salary',
    color='location'
)

fig = aplicar_layout(fig, "Salary Distribution by Top Locations", "Location", "Salary")
fig.update_layout(xaxis=dict(categoryorder='array', categoryarray=top_loc))
fig.show()

# =========================
# 5. Salary vs Skills
# =========================
skills_salary = df.groupby('skills_count')['salary'].mean().reset_index()

fig = px.line(skills_salary, x='skills_count', y='salary')

fig.update_traces(
    line=dict(color="#0B6E4F", width=4),
    marker=dict(size=9, color="#08A045"),
    mode="lines+markers"
)

fig = aplicar_layout(fig, "Salary vs Number of Skills", "Number of Skills", "Average Salary")
fig.show()

# =========================
# 6. Correlation Matrix
# =========================
corr = df[['salary', 'experience_years', 'skills_count', 'certifications']].corr()

plt.figure(figsize=(10, 7))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='Greens')
plt.title("Correlation Matrix")
plt.show()

# =========================
# 7. Company Size vs Salary
# =========================
company_salary = (
    df.groupby('company_size')['salary']
    .mean()
    .sort_values(ascending=True)
    .reset_index()
)

fig = go.Figure(go.Bar(
    x=company_salary['salary'],
    y=company_salary['company_size'],
    orientation='h',
    marker=dict(color=company_salary['salary'], colorscale='Greens')
))

fig = aplicar_layout(fig, "Salary by Company Size", "Salary", "Company Size")
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()

# =========================
# 8. Remote Work vs Salary
# =========================
remote_salary = (
    df.groupby('remote_work')['salary']
    .mean()
    .sort_values(ascending=True)
    .reset_index()
)

fig = go.Figure(go.Bar(
    x=remote_salary['salary'],
    y=remote_salary['remote_work'],
    orientation='h',
    marker=dict(color=remote_salary['salary'])
))

fig = aplicar_layout(fig, "Salary by Remote Work", "Salary", "Remote Work")
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()

# =========================
# 9. Salary by Job Title (Top 10 Highest)
# =========================
job_salary = (
    df.groupby('job_title')['salary']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = go.Figure(go.Bar(
    x=job_salary['salary'],
    y=job_salary['job_title'],
    orientation='h',
    marker=dict(color=job_salary['salary'], colorscale='Greens')
))

fig = aplicar_layout(fig, "Top 10 Highest Paying Jobs", "Salary", "Job Title")
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()

# =========================
# 10. Most Frequent Jobs
# =========================
top_jobs = (
    df['job_title']
    .value_counts()
    .head(10)
    .reset_index()
)

top_jobs.columns = ['job_title', 'count']

fig = go.Figure(go.Bar(
    x=top_jobs['count'],
    y=top_jobs['job_title'],
    orientation='h',
    marker=dict(color=top_jobs['count'], colorscale='Oranges')
))

fig = aplicar_layout(fig, "Top 10 Most Frequent Job Roles", "Count", "Job Title")
fig.update_layout(yaxis=dict(autorange="reversed"))
fig.show()
