import plotly.express as px
import pandas as pd


def skills_chart(skills):
    """
    Creates a bar chart for detected skills.
    """

    if not skills:
        return None

    df = pd.DataFrame({
        "Skill": skills,
        "Value": [1] * len(skills)
    })

    fig = px.bar(
        df,
        x="Skill",
        y="Value",
        title="Detected Skills",
        text="Value"
    )

    fig.update_yaxes(visible=False)
    fig.update_traces(textposition="outside")

    return fig


def missing_skills_chart(skills):
    """
    Creates a pie chart for missing skills.
    """

    if not skills:
        return None

    df = pd.DataFrame({
        "Skill": skills,
        "Count": [1] * len(skills)
    })

    fig = px.pie(
        df,
        names="Skill",
        values="Count",
        title="Missing Skills"
    )

    return fig