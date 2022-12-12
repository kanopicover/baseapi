from baseapi.apis import RestApi


class TodosApi(RestApi):
    def list_todos(self):
        # The following logging will not show up on pytest without extra flags:
        # pytest -o log_cli=true -o log_cli_level=info
        self.client.logger.info("Retrieving todos...")
        return self.get("/todos")

    def _just_a_test(self):
        # Shouldn't be exposed.
        pass
