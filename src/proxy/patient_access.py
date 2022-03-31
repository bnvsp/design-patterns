"""
Patient Access Manager using Proxy Design Pattern
"""

from abc import abstractmethod, ABC
from uuid import uuid4

class PatientRecord(ABC):
    """PatientRecord
    """

    @abstractmethod
    def add_patient(self, patient_record: dict) -> str:
        """_add_patient
        """

    @abstractmethod
    def get_patient_records(self, patient_id: str) -> dict:
        """_get_patient_records
        """
        raise NotImplementedError

    @abstractmethod
    def discharge_patient(self, patient_id: str):
        """_discharge_patient
        """


class PatientManager(PatientRecord):
    """Patient Records
    """
    VALID_CREDENTIALS: dict = {
        "doctor":{
            "username":"Dr X",
            "password":"sudo_x"
        },
        "accounts":{
            "username": "Billing",
            "password": "sudo_billing"
        }
    }

    def __init__(self) -> None:
        self.__patients: dict = {}
        self.__new_patients: list = []
        self.__discharged_patients: list = []


    def add_patient(self, patient_record: dict):
        """_add_patient: Add patient to the records

        Args:
            patient_id (int): Unique Patient Id
            patient_record (dict): Patient data
        """
        patient_uid: str = f"Patient-{str(uuid4())}"
        self.__patients[patient_uid] = patient_record
        self.__new_patients.append(patient_uid)

        return patient_uid


    def get_patient_records(self, patient_id: str) -> dict:
        """_get_patient_records: Get patient record from Id

        Args:
            patient_id (str): Patient-<ID>

        Returns:
            dict: Patient details
        """
        if patient_id not in self.__patients:
            raise ValueError(f"Patient not found with ID: {patient_id}")

        if patient_id in self.__discharged_patients:
            print(f"{patient_id} discharged")

        return self.__patients[patient_id]


    def discharge_patient(self, patient_id: str):
        """_get_patient_records: Discharge patient

        Args:
            patient_id (str): Patient-<ID>

        Returns:
            dict: Patient details
        """
        if patient_id not in self.__patients:
            raise ValueError(f"Patient not found with ID: {patient_id}")

        self.__new_patients.remove(patient_id)

        self.__discharged_patients.append(patient_id)

        return f"Patient with ID: {patient_id} has been discharged"


class PatientAccessManager(PatientRecord):
    """PatientAccessManager: Proxy to PatientManager
    """

    def __init__(self, title: str, credentials: dict) -> None:
        self.is_manager_valid = self.check_access(
            title=title, credentials=credentials
        )
        self.patient_manager = None
        if self.is_manager_valid:
            self.patient_manager = PatientManager()


    def add_patient(self, patient_record: dict) -> str:
        """add_patient: Add patient to record
        Args:
            patient_id (int): Patient unique Id
            patient_record (dict): Patient details
        """

        return self.patient_manager.add_patient(patient_record)


    def get_patient_records(self, patient_id: str) -> dict:
        """get_patient_records: Authenticate

        Args:
            patient_id (str): Patient ID
            credentials (dict): Credentials to access records

        Returns:
            dict: Patient Details
        """

        return self.patient_manager.get_patient_records(patient_id=patient_id)


    def discharge_patient(self, patient_id: str) -> str:
        """discharge_patient: Discharge patient with given Id

        Args:
            patient_id (str): Patient unique Id
        """

        return self.patient_manager.discharge_patient(patient_id)

    @staticmethod
    def check_access(title: str, credentials: dict) -> bool:
        """check_access: Validate Title and Credentials

        Args:
            title (str): _description_
            credentials (dict): _description_

        Returns:
            bool: _description_
        """
        _is_valid = True

        if title.lower() not in PatientManager.VALID_CREDENTIALS:
            _is_valid = False

        if credentials["username"] != PatientManager.VALID_CREDENTIALS[title]["username"]:
            _is_valid = False

        if credentials["password"] != PatientManager.VALID_CREDENTIALS[title]["password"]:
            _is_valid = False

        return _is_valid


def main(title: str, username: str, password: str):
    """main: Manage Patient Records

    Args:
        title (str): Designated individual
        username (str): Username
        password (str): Password
    """

    access_manager = PatientAccessManager(
        title=title,
        credentials={"username": username, "password": password}
    )
    if access_manager.patient_manager is not None:
        patient_id = access_manager.add_patient(
            patient_record={
                "Name": "Mr X",
                "Age": "56",
                "Reason": "Weakness"
            }
        )
        print(patient_id)

        info = access_manager.get_patient_records(patient_id=patient_id)
        print(info)

if __name__ == "__main__":
    main(title="accounts", username="Billing", password="sudo_billing")
