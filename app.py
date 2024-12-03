from flask import Flask, request, jsonify, render_template_string
from ariadne import make_executable_schema, gql, graphql_sync
from schema_def import query, mutation

# Definición del esquema GraphQL
type_defs = gql("""
    type Query {
        productos: [Producto]
        nombres: [Nombre]
    }

    type Mutation {
        crearNombre(nombre: String!): Nombre
    }

    type Producto {
        id: ID
        nombre: String
        precio: Float
    }

    type Nombre {
        id: ID
        nombre: String
    }
""")


schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)

# HTML para GraphiQL
graphiql_html = """
<!DOCTYPE html>
<html>
<head>
    <title>GraphiQL</title>
    <link rel="stylesheet" href="https://unpkg.com/graphiql/graphiql.min.css" />
</head>
<body style="margin: 0;">
    <div id="graphiql" style="height: 100vh;"></div>
    <script
        crossorigin
        src="https://unpkg.com/react/umd/react.production.min.js"
    ></script>
    <script
        crossorigin
        src="https://unpkg.com/react-dom/umd/react-dom.production.min.js"
    ></script>
    <script
        crossorigin
        src="https://unpkg.com/graphiql/graphiql.min.js"
    ></script>
    <script>
        const graphQLFetcher = graphQLParams =>
            fetch('/graphql', {
                method: 'post',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(graphQLParams),
            }).then(response => response.json());

        ReactDOM.render(
            React.createElement(GraphiQL, { fetcher: graphQLFetcher }),
            document.getElementById('graphiql'),
        );
    </script>
</body>
</html>
"""

@app.route("/graphql", methods=["GET", "POST"])
def graphql_server():
    if request.method == "GET":
        return render_template_string(graphiql_html)
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True, port=5000)
