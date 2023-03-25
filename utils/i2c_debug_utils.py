"""
I2C Debug Utility Script
Author: Sudheer Vadrevu
Course: BTH DV2530
Description:
  - Provides reusable functions for debugging and validating I2C ACK/NACK signals.
  - Designed for integration with I2C waveform simulation pipeline.
"""

import os
import json
import logging
from datetime import datetime
import matplotlib.pyplot as plt


# Logger setup
logger = logging.getLogger("i2c_debug")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("i2c_debug.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def read_ack_file(filepath):
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        return []

    with open(filepath, "r") as f:
        lines = f.readlines()

    ack_data = []
    for line in lines:
        if line.strip() == "":
            continue
        parts = line.strip().split(",")
        if len(parts) == 2:
            timestamp, ack = parts
            ack_data.append((float(timestamp), int(ack)))
        else:
            logger.warning(f"Ignoring malformed line: {line.strip()}")
    return ack_data


def detect_ack_errors(ack_data):
    errors = []
    for i, (_, ack) in enumerate(ack_data):
        if ack not in [0, 1]:
            errors.append((i, ack))
    return errors


def plot_ack_signals(ack_data, title="I2C ACK Signal Trace", output_file="ack_trace.png"):
    timestamps = [t for t, _ in ack_data]
    values = [v for _, v in ack_data]

    plt.figure(figsize=(10, 4))
    plt.step(timestamps, values, where='post')
    plt.title(title)
    plt.xlabel("Time (µs)")
    plt.ylabel("ACK (0 = ACK, 1 = NACK)")
    plt.grid(True)
    plt.savefig(output_file)
    logger.info(f"Plot saved to {output_file}")


def save_ack_summary(ack_data, summary_file="ack_summary.json"):
    ack_count = sum(1 for _, v in ack_data if v == 0)
    nack_count = sum(1 for _, v in ack_data if v == 1)
    summary = {
        "total": len(ack_data),
        "ack_count": ack_count,
        "nack_count": nack_count,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    logger.info(f"ACK summary written to {summary_file}")


def run_debug_pipeline(filepath):
    logger.info(f"Running I2C debug pipeline for {filepath}")
    data = read_ack_file(filepath)
    if not data:
        logger.error("No ACK data found.")
        return

    errors = detect_ack_errors(data)
    if errors:
        logger.warning(f"Detected {len(errors)} malformed ACK entries.")
        for idx, val in errors:
            logger.debug(f"Line {idx}: Invalid ACK = {val}")

    plot_ack_signals(data)
    save_ack_summary(data)
    logger.info("Debug pipeline completed successfully.")


# Entry point
if __name__ == "__main__":
    test_file = "ack_data_sample.csv"
    logger.info(f"Starting debug utility on {test_file}")
    run_debug_pipeline(test_file)
