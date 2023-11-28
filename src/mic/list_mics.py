import sounddevice as sd


def list_mics():
    """
    Check and print the available microphones using the sounddevice library.

    Example:
    check_available_microphones()
    """
    mics = sd.query_devices()
    default_devices = sd.default.device
    default_input = default_devices[0]
    default_output = default_devices[1]

    # Print all available devices
    for i in range(len(mics)):
        print(mics[i])

    # You can set the default microphone easily with:
    # sounddevice.default.device = 0
    # For example, for recording microphone:
    # {'name': 'Built-in Microphone', 'hostapi': 0, 'max_input_channels': 2, 'max_output_channels': 0,
    # 'default_low_input_latency': 0.0029478458049886623, 'default_low_output_latency': 0.01,
    # 'default_high_input_latency': 0.01310657596371882, 'default_high_output_latency': 0.1,
    # 'default_samplerate': 44100.0}

    # For recording output:
    # {'name': 'Built-in Output', 'hostapi': 0, 'max_input_channels': 0, 'max_output_channels': 2,
    # 'default_low_input_latency': 0.01, 'default_low_output_latency': 0.008798185941043084,
    # 'default_high_input_latency': 0.1, 'default_high_output_latency': 0.018956916099773242,
    # 'default_samplerate': 44100.0}


# Example usage:
# list_mics()
