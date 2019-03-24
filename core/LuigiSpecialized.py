import luigi
import os
from Utils import PathHelper, Singleton
import datetime

class LuigiSharedData(metaclass=Singleton):
    def __init__(self):
        self.data = {}

    def getData(self):
        return self.data

    def setData(self, data):
        self.data.update(data)

class LuigiCore(luigi.Task):

    def output(self):
        return luigi.LocalTarget(PathHelper.getCustomLogFile(self.__class__.__name__ + '.csv'))

class LuigiOutputTime(luigi.Task):

    def output(self):
        luigidata = LuigiSharedData().getData()
        date = luigidata['date']
        return luigi.LocalTarget(PathHelper.getCustomLogFile('{:%Y-%m-%d %H%M%S} '.format(date) + self.__class__.__name__ + '.csv'))

class LuigiTaskFreshOutput(LuigiCore):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        outputs = luigi.task.flatten(self.output())
        for out in outputs:
            if out.exists():
                os.remove(self.output().path)

"""
class LuigiEmptyTask(LuigiTaskFreshOutput):
    task_complete = False

    def requires(self): #TO IMPLEMENT
        return [ ItTasksProjects(), Workpackages() ]

    def run(self):
        self.task_complete = True

    def complete(self):
        return self.task_complete

"""