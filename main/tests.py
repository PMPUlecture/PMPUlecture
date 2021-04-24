from .test_models import ModelsTestCase
from .api.test_api_get import LecturerApiTestCase, SubjectsApiTestCase, ProgrammesApiTestCase

__test__ = {"Models": ModelsTestCase, "ApiLecturer": LecturerApiTestCase, "ApiSubjects": SubjectsApiTestCase,
            "ApiProgrammes": ProgrammesApiTestCase}