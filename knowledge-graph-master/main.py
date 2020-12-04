import flask
import knowledge


app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/api/build-graph')
def build_graph():
    term = flask.request.args['term']
    knowledge_graph = knowledge.KnowledgeGraph(term)
    return {
        'nodes': [{'id': node} for node in knowledge_graph.nodes],
        'edges': [{'from': edge[0], 'to': edge[1]} for edge in knowledge_graph.edges],
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
