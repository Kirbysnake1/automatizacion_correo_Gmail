import pandas as pd


class ExcelService:

    def __init__(self, path):
        self.path = path

    def get_companies(self):

        dataframe = pd.read_excel(self.path)

        companies = []

        for _, row in dataframe.iterrows():

            companies.append({
                "empresa": row["Empresa"],
                "correo": row["Correo"]
            })

        return companies