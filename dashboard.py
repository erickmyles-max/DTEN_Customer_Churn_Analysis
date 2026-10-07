
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# -----------------------------------------
# Load and clean dataset
# -----------------------------------------

DATA_URL = (
    "https://raw.githubusercontent.com/IBM/"
    "telco-customer-churn-on-icp4d/master/data/"
    "Telco-Customer-Churn.csv"
)

df = pd.read_csv(DATA_URL)

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(0)

# -----------------------------------------
# Create Dash application
# -----------------------------------------

app = Dash(__name__)

# Needed by some deployment platforms
server = app.server

contract_options = sorted(
    df["Contract"].dropna().unique()
)

internet_options = sorted(
    df["InternetService"].dropna().unique()
)

# -----------------------------------------
# Dashboard layout
# -----------------------------------------

app.layout = html.Div([

    html.H1(
        "Telco Customer Churn Dashboard",
        style={
            "textAlign": "center",
            "color": "#1F3A5F"
        }
    ),

    html.P(
        "Interactive exploration of telecommunications customer churn",
        style={
            "textAlign": "center",
            "color": "#666"
        }
    ),

    # FILTERS
    html.Div([

        html.Div([
            html.Label("Contract Type"),

            dcc.Dropdown(
                id="contract-filter",
                options=[
                    {"label": x, "value": x}
                    for x in contract_options
                ],
                value=[],
                multi=True,
                placeholder="All Contract Types"
            )

        ], style={
            "width": "47%",
            "display": "inline-block",
            "marginRight": "5%"
        }),

        html.Div([
            html.Label("Internet Service"),

            dcc.Dropdown(
                id="internet-filter",
                options=[
                    {"label": x, "value": x}
                    for x in internet_options
                ],
                value=[],
                multi=True,
                placeholder="All Internet Services"
            )

        ], style={
            "width": "47%",
            "display": "inline-block"
        })

    ], style={
        "padding": "20px",
        "backgroundColor": "#F4F6F7"
    }),

    # KPI CARDS
    html.Div([

        html.Div([
            html.H4("Total Customers"),
            html.H2(id="total-customers")
        ], className="kpi-card",
           style={
               "backgroundColor": "#3498DB",
               "color": "white"
           }),

        html.Div([
            html.H4("Churned Customers"),
            html.H2(id="churned-customers")
        ], className="kpi-card",
           style={
               "backgroundColor": "#E74C3C",
               "color": "white"
           }),

        html.Div([
            html.H4("Churn Rate"),
            html.H2(id="churn-rate")
        ], className="kpi-card",
           style={
               "backgroundColor": "#F39C12",
               "color": "white"
           }),

        html.Div([
            html.H4("Average Monthly Charge"),
            html.H2(id="avg-charge")
        ], className="kpi-card",
           style={
               "backgroundColor": "#27AE60",
               "color": "white"
           })

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "gap": "10px",
        "margin": "20px"
    }),

    # CHARTS
    html.Div([

        html.Div(
            dcc.Graph(id="churn-pie"),
            style={"width": "49%"}
        ),

        html.Div(
            dcc.Graph(id="contract-chart"),
            style={"width": "49%"}
        )

    ], style={"display": "flex"}),

    html.Div([

        html.Div(
            dcc.Graph(id="monthly-chart"),
            style={"width": "49%"}
        ),

        html.Div(
            dcc.Graph(id="tenure-chart"),
            style={"width": "49%"}
        )

    ], style={"display": "flex"}),

    html.Hr(),

    html.P(
        "DTEN Data Science & Analytics Internship Project",
        style={
            "textAlign": "center",
            "color": "#777"
        }
    )

], style={
    "fontFamily": "Arial, sans-serif",
    "maxWidth": "1400px",
    "margin": "auto"
})


# -----------------------------------------
# Dashboard callback
# -----------------------------------------

@app.callback(
    [
        Output("total-customers", "children"),
        Output("churned-customers", "children"),
        Output("churn-rate", "children"),
        Output("avg-charge", "children"),
        Output("churn-pie", "figure"),
        Output("contract-chart", "figure"),
        Output("monthly-chart", "figure"),
        Output("tenure-chart", "figure")
    ],
    [
        Input("contract-filter", "value"),
        Input("internet-filter", "value")
    ]
)
def update_dashboard(selected_contracts, selected_internet):

    filtered_df = df.copy()

    if selected_contracts:
        filtered_df = filtered_df[
            filtered_df["Contract"].isin(selected_contracts)
        ]

    if selected_internet:
        filtered_df = filtered_df[
            filtered_df["InternetService"].isin(selected_internet)
        ]

    # KPI calculations
    total = len(filtered_df)

    churned = (
        filtered_df["Churn"] == "Yes"
    ).sum()

    churn_rate = (
        churned / total * 100
        if total > 0
        else 0
    )

    avg_charge = (
        filtered_df["MonthlyCharges"].mean()
        if total > 0
        else 0
    )

    # Churn distribution
    churn_counts = (
        filtered_df["Churn"]
        .value_counts()
        .reset_index()
    )

    churn_counts.columns = [
        "Churn",
        "Customers"
    ]

    pie_fig = px.pie(
        churn_counts,
        names="Churn",
        values="Customers",
        hole=0.45,
        title="Customer Churn Distribution",
        color="Churn",
        color_discrete_map={
            "Yes": "#E74C3C",
            "No": "#3498DB"
        }
    )

    # Contract chart
    contract_data = (
        filtered_df
        .groupby(
            ["Contract", "Churn"],
            observed=True
        )
        .size()
        .reset_index(name="Customers")
    )

    contract_fig = px.bar(
        contract_data,
        x="Contract",
        y="Customers",
        color="Churn",
        barmode="group",
        title="Churn by Contract Type",
        color_discrete_map={
            "Yes": "#E74C3C",
            "No": "#3498DB"
        }
    )

    # Monthly charges
    monthly_fig = px.histogram(
        filtered_df,
        x="MonthlyCharges",
        color="Churn",
        nbins=30,
        title="Monthly Charges Distribution",
        color_discrete_map={
            "Yes": "#E74C3C",
            "No": "#3498DB"
        }
    )

    # Tenure scatter plot
    tenure_fig = px.scatter(
        filtered_df,
        x="tenure",
        y="MonthlyCharges",
        color="Churn",
        hover_data=[
            "Contract",
            "InternetService",
            "PaymentMethod"
        ],
        title="Tenure vs Monthly Charges",
        color_discrete_map={
            "Yes": "#E74C3C",
            "No": "#3498DB"
        }
    )

    return (
        f"{total:,}",
        f"{churned:,}",
        f"{churn_rate:.1f}%",
        f"${avg_charge:.2f}",
        pie_fig,
        contract_fig,
        monthly_fig,
        tenure_fig
    )


# -----------------------------------------
# Run application
# -----------------------------------------

if __name__ == "__main__":
    app.run(debug=False)
