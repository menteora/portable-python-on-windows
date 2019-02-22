import luigi
import os
from Utils import PathHelper

class LuigiCore(luigi.Task):

    def output(self):
        return luigi.LocalTarget(PathHelper.getCustomLogFile(self.__class__.__name__ + ".csv"))

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