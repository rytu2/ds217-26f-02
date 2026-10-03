#!/usr/bin/env python3
"""Summarize one week of clinic encounters and save the two report files."""

from pathlib import Path

from vitals_tools import (
    count_patients,
    mean_systolic,
    patients_at_or_above,
    systolic_readings,
)


DATA_PATH = Path("data") / "clinic_encounters.csv"
OUTPUT_DIR = Path("output")


def read_encounters(data_path):
    """TODO: describe what one usable encounter looks like.

    Give back two values: the list of usable encounters, and how many data
    rows you skipped. `main()` unpacks them the way the lecture unpacks a
    tuple, with two names on the left of the `=`.
    """
    # TODO: read the rows and skip the header line.
    # TODO: keep a row only when it has three fields, int() can read the
    #       systolic field, and the reading is plausible.
    # TODO: count every other data row as skipped, the blank line included,
    #       and print one line per skipped row so you can see what dropped out.
    # TODO: end with `return encounters, skipped`.
    encounters = []
    skipped = 0

    with open(data_path, "r") as file:
        next(file)

        for line in file:
            row = line.strip().split(",")

            if len(row) != 3:
                skipped += 1
                print("Skipped:", line.strip())
                continue

            try:
                systolic = int(row[2])
            except ValueError:
                skipped += 1
                print("Skipped:", line.strip())
                continue

            if systolic < 50 or systolic > 250:
                skipped += 1
                print("Skipped:", line.strip())
                continue

            encounters.append(row)

    return encounters, skipped
    pass


def main():
    """TODO: describe the two artifacts this writes."""
    encounters, skipped = read_encounters(DATA_PATH)

    # TODO: build the six report lines and write them to output/vitals_report.txt.
    # TODO: read the file back and print it, so you can see what was saved.
    # TODO: choose your follow-up cutoff, then write output/followup_list.txt
    #       with the Cutoff line, the Reason line, and one patient ID per line.

    patient_ids = set()
    systolics = []

    for row in encounters:
        patient_ids.add(row[0])
        systolics.append(int(row[2]))

    report_lines = [
        f"Usable encounters: {len(encounters)}",
        f"Skipped rows: {skipped}",
        f"Patients seen: {len(patient_ids)}",
        f"Mean systolic: {sum(systolics) / len(systolics)} mmHg",
        f"Highest systolic: {max(systolics)} mmHg",
        f"Lowest systolic: {min(systolics)} mmHg"
    ]

    with open("output/vitals_report.txt", "w") as outfile:
        for line in report_lines:
            outfile.write(line + "\n")

    with open("output/vitals_report.txt", "r") as infile:
        print(infile.read())

    cutoff = 140

    with open("output/followup_list.txt", "w") as outfile:
        outfile.write(f"Cutoff: {cutoff} mmHg\n")
        outfile.write("Reason: systolic blood pressure at or above cutoff\n")

        for row in encounters:
            patient_id = row[0]
            systolic = int(row[2])

            if systolic >= cutoff:
                outfile.write(f"{patient_id}\n")

if __name__ == "__main__":
    main()
