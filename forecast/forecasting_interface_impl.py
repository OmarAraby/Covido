# importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from prophet import Prophet
from sklearn.metrics import r2_score

from .forecasting_interface import ForecastingModelInterface


class ForecastingModelInterfaceImp(ForecastingModelInterface):

    def __init__(self, file_source, name_of_model):
        super().__init__(file_source, name_of_model)
        self.file_source=file_source
        self.name_of_model=name_of_model

    def _file_edit(self):
        # get a copy of data
        # cases_data = self.get_original_universal_data_file().copy()
        cases_data =  self.file_source.copy()
        cases_data.drop(['Country', 'CountryCode', 'Province', 'City', 'CityCode', 'Lat', 'Lon', 'Status'], axis=1,
                             inplace=True)
        cases_data.dropna()
        cases_data["Date"] = pd.to_datetime(cases_data["Date"]).dt.date

        # manipulte data before broadcasting
        cases_data.columns = ['y', 'ds']
        print(cases_data)
        cols = cases_data.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        confirmed_cases = cases_data[cols]
        return confirmed_cases

    def _model(self):
        # self._egypt_data.columns = ['ds', 'y']
        # # Training confirmed_cases model
        model = Prophet(interval_width=0.97)
        model.fit(self._file_edit())
        return model

    def forecast(self):
        model = self._model()
        future = model.make_future_dataframe(periods=7, freq='M')
        forecast = model.predict(future)
        return forecast

    def get_r2_error(self):
        metric_df = self.forecast().set_index('ds')[['yhat']].join(self.file_source.set_index('ds').y).reset_index()
        # nane as the future data first
        # was not exsist
        metric_df.dropna(inplace=True)
        return r2_score(metric_df.y, metric_df.yhat)

    def plot_cases(self):
        plt.xlabel('Time')
        plt.ylabel(self.name_of_model)
        plt.plot(self.file_source['Date'], self.file_source['Cases'])
        plt.show()

        # I have to change the ip
        # of my browser
        # to open it
        # fig = go.Figure()
        # fig.add_trace(
        #     go.Scatter(x=self._egypt_original_data['reported_date'], y=self._egypt_original_data[self.name_of_model],
        #                mode='lines+markers',
        #                name=self.name_of_model, line=dict(color='blue', width=2)))
        # fig.update_layout(title='Egypt COVID-19 {}'.format(self.name_of_model), xaxis_tickfont_size=14,
        #                   yaxis=dict(title='Number of Cases'))
        # fig.show()

    def plot_forecasting(self):
        self._model().plot(self.forecast())
        plt.show()

    def plot_all_change_points(self):
        self._model().plot(self.forecast())
        for changepoint in self._model().changepoints:
            plt.axvline(changepoint, ls='--', lw=1)
        plt.show()

    def plot_all_magnitude_change_points(self):
        # the magnitude of changepoints
        deltas = self._model().params['delta'].mean(0)
        fig = plt.figure(facecolor='w')
        ax = fig.add_subplot(111)
        ax.bar(range(len(deltas)), deltas)
        ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
        ax.set_ylabel('Rate change')
        ax.set_xlabel('Potential change point')
        fig.tight_layout()
        plt.show()
