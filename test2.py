import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

def find_all_indexes(list_data, element):
    indexes = []
    for index, item in enumerate(list_data):
        if item == element:
            indexes.append(index)
    return indexes

def preprocessCode(lst: list) -> list:
    lst = list(map(lambda x: x[:-1], lst))
    lst = list(filter(lambda x: True if x != "" and x != '#' else False, lst))
    lst = list(map(lambda x: x.split(), lst))

    result = []

    for lt in lst:
        result += lt

    indices = find_all_indexes(result, "<p>")
    ans = []

    for i in indices:
        ans.append(result[i + 1])

    return ans

def displayPipeline():

    labels = []
    source_indices = []
    target_indices = []

    labels.append("Data Ingestion")

    file = open("D:/itest/rgh/1.py", "r")
    ans = preprocessCode(file.readlines())
    file.close()
    prevKeys = []

    for i in range(len(ans)):
        source_indices.append(0)
        target_indices.append(len(labels))
        prevKeys.append(len(labels))
        labels.append(ans[i])

    labels.append("Data Transformation")
    h = len(labels) - 1

    for i in range(len(prevKeys)):
        source_indices.append(prevKeys[i])
        target_indices.append(h)


    file = open("D:/itest/rgh/2.py", "r")
    ans = preprocessCode(file.readlines())
    file.close()
    prevKeys = []
    h=len(labels)-1

    for i in range(len(ans)):
        source_indices.append(h)
        target_indices.append(len(labels))
        prevKeys.append(len(labels))
        labels.append(ans[i])

    labels.append("Model Trainer")
    h = len(labels) - 1

    for i in range(len(prevKeys)):
        source_indices.append(prevKeys[i])
        target_indices.append(h)


    file = open("D:/itest/rgh/3.py", "r")
    ans = preprocessCode(file.readlines())
    file.close()
    prevKeys = []
    h=len(labels)-1

    for i in range(len(ans)):
        source_indices.append(h)
        target_indices.append(len(labels))
        prevKeys.append(len(labels))
        labels.append(ans[i])

    labels.append("Model Predictor")
    h = len(labels) - 1

    for i in range(len(prevKeys)):
        source_indices.append(prevKeys[i])
        target_indices.append(h)


    file = open("D:/itest/rgh/4.py", "r")
    ans = preprocessCode(file.readlines())
    file.close()
    prevKeys = []
    h=len(labels)-1

    for i in range(len(ans)):
        source_indices.append(h)
        target_indices.append(len(labels))
        prevKeys.append(len(labels))
        labels.append(ans[i])

    labels.append("Model Evaluator")
    h = len(labels) - 1

    for i in range(len(prevKeys)):
        source_indices.append(prevKeys[i])
        target_indices.append(h)

    file = open("D:/itest/rgh/4.py", "r")
    ans = preprocessCode(file.readlines())
    file.close()
    prevKeys = []
    h=len(labels)-1

    for i in range(len(ans)):
        source_indices.append(h)
        target_indices.append(len(labels))
        prevKeys.append(len(labels))
        labels.append(ans[i])

    labels.append("EOP")
    h = len(labels) - 1

    for i in range(len(prevKeys)):
        source_indices.append(prevKeys[i])
        target_indices.append(h)






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
            value=[10 for _ in range(len(source_indices))]
        )
    )])

    fig.update_layout(title_text="Sankey Diagram Example")

    return fig

st.title("Sankey Diagram in Streamlit")
st.plotly_chart(displayPipeline())
