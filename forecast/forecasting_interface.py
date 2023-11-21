import abc


class ForecastingModelInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self,file_source,name_of_model):
        pass

    @abc.abstractmethod
    def _file_edit(self):
        pass
    @abc.abstractmethod
    def _model(self):
        pass
    @abc.abstractmethod
    def forecast(self):
        pass

    @abc.abstractmethod
    def get_r2_error(self):
        pass

    @abc.abstractmethod
    def plot_cases(self):
        pass
    @abc.abstractmethod
    def plot_forecasting(self):
        pass
    @abc.abstractmethod
    def plot_all_change_points(self):
        pass

    @abc.abstractmethod
    def plot_all_magnitude_change_points(self):
        pass
