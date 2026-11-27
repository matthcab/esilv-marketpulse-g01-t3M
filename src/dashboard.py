from dash import Dash, dcc, html
import plotly.graph_objects as go

from main import build_market_snapshot


def create_app():
    snapshot = build_market_snapshot()
    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    figure = go.Figure()
    for asset, series_key, color in (
        (instrument, "instrument_base_100", "#2455C3"),
        (benchmark, "benchmark_base_100", "#A25419"),
    ):
        rows = snapshot[series_key]
        figure.add_scatter(
            x=[row["date"] for row in rows],
            y=[row["value"] for row in rows],
            name=asset["ticker"],
            mode="lines",
            line={"color": color, "width": 2.5},
        )
    figure.update_layout(
        template="plotly_white",
        title="Instrument vs Benchmark · Base 100",
        xaxis_title="Date",
        yaxis_title="Base 100",
        hovermode="x unified",
        legend={"orientation": "h", "y": 1.02, "yanchor": "bottom"},
        margin={"l": 56, "r": 20, "t": 90, "b": 56},
    )

    context = (
        ("Provider", f"{snapshot['provider']} · {snapshot['access_mode']}"),
        ("Instrument", f"{instrument['ticker']} · {instrument['name']}"),
        ("Benchmark", f"{benchmark['ticker']} · {benchmark['name']}"),
        ("Lookback", snapshot["lookback"]),
        ("Interval", snapshot["interval"]),
    )
    indicators = (
        ("Instrument return", f"{snapshot['instrument_return']:+.2f}%"),
        ("Benchmark return", f"{snapshot['benchmark_return']:+.2f}%"),
        ("Relative performance", f"{snapshot['relative_performance']:+.2f} pts"),
    )

    app = Dash(__name__, title="MarketPulse")
    app.layout = html.Main(
        [
            html.H1("MarketPulse"),
            html.Dl(
                [
                    html.Div([html.Dt(label), html.Dd(value, style={"margin": 0})])
                    for label, value in context
                ],
                style={"display": "flex", "flexWrap": "wrap", "gap": "16px 28px"},
            ),
            html.Section(
                [
                    html.Article(
                        [
                            html.H2(label, style={"fontSize": "14px", "margin": 0}),
                            html.P(value, style={"fontSize": "30px", "margin": "8px 0 0"}),
                        ],
                        style={"padding": "16px", "backgroundColor": "#F1F5FB"},
                    )
                    for label, value in indicators
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fit, minmax(180px, 1fr))",
                    "gap": "12px",
                    "margin": "24px 0",
                },
            ),
            dcc.Graph(figure=figure),
        ],
        style={
            "maxWidth": "1040px",
            "margin": "auto",
            "padding": "16px 24px",
            "fontFamily": "system-ui, sans-serif",
            "color": "#18243A",
        },
    )
    return app


if __name__ == "__main__":
    create_app().run(debug=False)
