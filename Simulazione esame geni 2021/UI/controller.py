import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._gene = None
        self._listGeni = None

    def handle_graph(self, e):
        self._model.buildGraph()

        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Creato grafo con {self._model.getNumNodi()} vertici e {self._model.getNumArchi()} archi"))
        self._view.update_page()

    def handle_adiacenti(self, e):
        self._gene = self._view.dd_geni.value
        if self._gene is None :
            self._view.create_alert("Gene non inserito")
            return

        self._view.txt_result1.controls.clear()
        lista = self._model.calcolaAdiacenti(self._gene)
        self._view.txt_result2.controls.append(ft.Text(f"Geni adiacenti a: {self._gene}"))
        for i in lista:
            self._view.txt_result2.controls.append(ft.Text(f"{i[0]} - {i[1]}"))
        self._view.update_page()

    def fillDDGeni(self):
        self._listGeni = self._model.getGeniId()
        for s in self._listGeni:
            self._view.dd_geni.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def read_geni(self, e):
        if e.control.value == "None":
            self._gene = None
        else:
            self._gene = e.control.value