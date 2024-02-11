import streamlit as st
import plotly.graph_objects as go

st.set_page_config("wide")

def create_sankey_diagram():
    # Example data
    labels = ["Source 1", "Source 2", "Intermediate 1", "Intermediate 2", "Destination"]
    source_indices = [0, 1, 0, 2, 3]
    target_indices = [2, 2, 3, 3, 4]
    values = [10, 15, 5, 10, 30]

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color='black', width=0.5),
            label=labels
        ),
        link=dict(
            source=source_indices,
            target=target_indices,
            value=values
        )
    )])

    # Update layout
    fig.update_layout(title_text="Sankey Diagram Example")

    return fig

def main():
    st.title("Sankey Diagram in Streamlit")
    st.plotly_chart(create_sankey_diagram())

if __name__ == "__main__":
    main()
