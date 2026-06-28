import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def ddda(self):
        self._view._ddAnno1.options.clear()
        self._view._ddAnno1.value = None
        lista=self._model.get_anni()
        for l in lista:
            self._view._ddAnno1.options.append(
                    ft.dropdown.Option(
                        key=str(l),
                        text=str(l),
                    )
                )
        self._view.update_page()


    def dda(self):
            self._view._ddAnno2.options.clear()
            self._view._ddAnno2.value = None
            lista = self._model.get_anni()
            for l in lista:
                self._view._ddAnno2.options.append(
                    ft.dropdown.Option(
                        key=str(l),
                        text=str(l),
                    )
                )
            self._view.update_page()


    def handleCreaGrafo(self,e):
        self._view.txt_result.controls.clear()
        try:
            anno1 = int(self._view._ddAnno1.value)
            anno2 = int(self._view._ddAnno2.value)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("selezionare entrambi gli anni"))
        if anno1 is None or anno2 is None or anno1 > anno2:
            self._view.txt_result.controls.append(
                ft.Text("selezionare entrambi gli anni", color="red")
            )

        self._model.build_graph(anno1, anno2)
        stats=self._model.get_stats()
        self._view.txt_result.controls.append(ft.Text(f"stats:{stats[0]} e {stats[1]}"))
        self._view.update_page()



    def handleDettagli(self, e):
        self._view.txt_result.controls.clear()
        s=self._model.top3()

        stats, lista_lunga = self._model.connesse()
        self._view.txt_result.controls.append(ft.Text(f"la top 3 è:{s}"))
        self._view.txt_result.controls.append(ft.Text(f"numero tot di connessi:{stats}",color="red"))
        for k in lista_lunga:
            self._view.txt_result.controls.append(ft.Text(f"numero tot di connessi:{k.driverRef}",color="blue"))
        self._view.update_page()



    def handleCerca(self, e):
        pass

