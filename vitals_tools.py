"""Reusable helpers for summarizing clinic systolic readings."""


def systolic_readings(encounters):
    """TODO: describe what this pulls out of the encounter records."""
    # TODO: collect the systolic value of every encounter into one list.

    readings = []

    for encounter in encounters:
        readings.append(int(encounter[2]))

    return readings

    pass


def mean_systolic(readings):
    """TODO: describe what this returns, including the empty-list result."""
    # TODO: return None when there is nothing to average, then sum() / len().
    if len(readings) == 0:
        return None

    return sum(readings) / len(readings)
    
    pass


def count_patients(encounters):
    """TODO: describe what this counts."""
    # TODO: collect the patient IDs and keep only the distinct ones.
    patient_ids = set()

    for encounter in encounters:
        patient_ids.add(encounter[0])

    return len(patient_ids)

    pass


def patients_at_or_above(encounters, cutoff):
    """TODO: describe which patient IDs come back."""
    # TODO: keep each patient whose systolic reading is at or above cutoff.
    patients = []

    for encounter in encounters:
        if int(encounter[2]) >= cutoff:
            patients.append(encounter[0])

    return patients
    
    pass
