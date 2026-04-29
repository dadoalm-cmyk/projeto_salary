# =========================
# IMPORT
# =========================
import pandas as pd

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("C:/Users/dadoa/Downloads/archive (11)/job_salary_prediction_dataset.csv")

# =========================
# VISÃO GERAL
# =========================
print("\n=== HEAD ===")
print(df.head())

print("\n=== INFO ===")
print(df.info())

print("\n=== DESCRIBE ===")
print(df.describe())

# =========================
# SALÁRIOS
# =========================
print("\n=== SALÁRIO POR EDUCAÇÃO ===")
print(df.groupby("education_level")["salary"].mean().sort_values(ascending=False))

print("\n=== SALÁRIO POR EXPERIÊNCIA ===")
print(df.groupby("experience_years")["salary"].mean().head(10))

print("\n=== SALÁRIO POR TIPO DE TRABALHO (REMOTE) ===")
print(df.groupby("remote_work")["salary"].mean())

print("\n=== SALÁRIO POR CERTIFICAÇÕES ===")
print(df.groupby("certifications")["salary"].mean())


print("\n=== SALÁRIO POR INDÚSTRIA ===")
print(
    df.groupby("industry")["salary"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== SALÁRIO POR TAMANHO DA EMPRESA ===")
print(
    df.groupby("company_size")["salary"]
    .mean()
    .sort_values(ascending=False)
)


# =========================
# CORRELAÇÕES
# =========================
print("\n=== CORRELAÇÃO NUMÉRICA ===")
print(df[['salary', 'experience_years', 'certifications']].corr())

df_encoded = pd.get_dummies(
    df[['salary', 'industry', 'company_size']],
    drop_first=True
)

corr = df_encoded.corr()

salary_corr = corr['salary'].sort_values(ascending=False)

print("\n=== IMPACTO NO SALÁRIO ===")
print(salary_corr.head(10))   # maiores positivos
print(salary_corr.tail(10))   # maiores negativos

# =========================
# EDUCAÇÃO
# =========================
print("\n=== CERTIFICAÇÕES POR EDUCAÇÃO ===")
print(
    df.groupby('education_level')['certifications']
    .mean()
    .sort_values(ascending=False)
)

print("\n=== SKILLS POR EDUCAÇÃO ===")
print(
    df.groupby('education_level')['skills_count']
    .mean()
    .sort_values(ascending=False)
)

print("\n=== EDUCAÇÃO POR LOCALIZAÇÃO ===")
print(
    df.groupby(['location', 'education_level'])
    .size()
    .unstack(fill_value=0)
    .sort_index()
)



# =========================
# CARGOS
# =========================
print("\n=== QUANTIDADE DE CARGOS ===")
print(df['job_title'].nunique())

print("\n=== TOP 10 CARGOS MAIS FREQUENTES ===")
print(df['job_title'].value_counts().head(10))

print("\n=== TOP 10 SALÁRIOS POR CARGO ===")
print(
    df.groupby('job_title')['salary']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)


# =========================
# LOCALIZAÇÃO
# =========================
print("\n=== TOP 10 LOCALIZAÇÕES MAIS FREQUENTES ===")
print(df['location'].value_counts().head(10))

print("\n=== TOP 10 SALÁRIOS POR LOCALIZAÇÃO ===")
print(
    df.groupby('location')['salary']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\n=== CERTIFICAÇÕES POR LOCALIZAÇÃO ===")
print(
    df.groupby('location')['certifications']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)


# =========================
# SKILLS
# =========================
print("\n=== SALÁRIO POR NÚMERO DE SKILLS ===")
print(df.groupby('skills_count')['salary'].mean().head(10))
