from src.db_connect import CnxAS400

class DB400Error(Exception):
    pass

class DB400:
    def __init__(self):
        self.connection = CnxAS400()

    def execute(self, query_type, query):
        with self.connection.connect() as conn:
            cursor = conn.cursor()

            # Vérifie que la requête correspond au type spécifié
            if query_type == "CREATE" and not query.strip().upper().startswith("INSERT"):
                raise DB400Error("Invalid query type for CREATE")
            if query_type == "READ" and not query.strip().upper().startswith("SELECT"):
                raise DB400Error("Invalid query type for READ")
            if query_type == "UPDATE" and not query.strip().upper().startswith("UPDATE"):
                raise DB400Error("Invalid query type for UPDATE")
            if query_type == "DELETE" and not query.strip().upper().startswith("DELETE"):
                raise DB400Error("Invalid query type for DELETE")

            # Exécute la requête
            cursor.execute(query)

            # Pour les requêtes de type READ, renvoie le résultat
            if query_type == "READ":
                results = cursor.fetchall()
                return [dict(zip([column[0] for column in cursor.description], row)) for row in results]
            else:
                # Pour les autres types, effectue un commit et renvoie un message de succès
                conn.commit()
                return {"message": f"{query_type} query executed successfully"}
