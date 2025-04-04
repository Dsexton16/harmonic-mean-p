import numpy as np

def generate_spectra(num_samples, sampling_rate, spectrum='alternating')
    # Parameters
    num_samples = 100  # Number of samples in the signal
    sampling_rate = 100  # Hz
    frequencies = np.fft.rfftfreq(num_samples, 1 / sampling_rate)  # Frequency bins

    # Create alternating power spectrum (10 for even frequencies, 20 for odd)
    if spectrum == 'alternating':
        power_spectrum = np.array([10 if freq % 2 == 0 else 20 for freq in frequencies])

    # Gamma distribution parameters
    shape = 1  # Shape parameter (k=1 for single bin, doubled for combined bins)

    # Sample power for individual bins using the alternating power spectrum
    single_bin_power = np.random.gamma(shape, power_spectrum)

    # Combine power for conjugate symmetric bins
    combined_power = []
    for i in range(len(frequencies)):
        if i == 0 or i == len(frequencies) - 1:  # DC or Nyquist, keep as is
            combined_power.append(single_bin_power[i])
        else:
            combined_power.append(
                np.random.gamma(shape, power_spectrum[i]) +
                np.random.gamma(shape, power_spectrum[i])
            )
    
    return combined_power
    
'''
# Plot results
plt.figure(figsize=(12, 6))
plt.plot(frequencies, single_bin_power, label="Single Bin Power (Gamma k=1)")
plt.plot(frequencies, combined_power, label="Combined Power (Gamma k=2)", linestyle="--")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.title("Power Spectrum with Alternating Power (10 for even, 20 for odd)")
plt.legend()
plt.grid()
plt.show()
'''