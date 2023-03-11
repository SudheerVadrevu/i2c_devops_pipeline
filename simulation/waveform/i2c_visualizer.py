import matplotlib.pyplot as plt
from fpdf import FPDF

class I2CSignalVisualizer:
    def __init__(self):
        self.signals = []

    def plot_signals(self, devices):
        times = list(range(10))
        plt.figure(figsize=(8, 4))
        for i, dev in enumerate(devices):
            plt.plot(times, [(t + i) % 2 for t in times], label=f"Device {hex(dev.address)}")

        plt.title("I2C Acknowledgement Waveform")
        plt.xlabel("Time")
        plt.ylabel("Signal")
        plt.legend()
        plt.grid(True)
        plt.savefig("reports/i2c_waveform.png")
        self.generate_pdf("reports/i2c_waveform.pdf")

    def generate_pdf(self, output_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="I2C Simulation Output", ln=True, align='C')
        pdf.image("reports/i2c_waveform.png", x=10, y=30, w=180)
        pdf.output(output_path)
