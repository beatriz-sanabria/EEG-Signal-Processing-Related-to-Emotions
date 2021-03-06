from signal_frequency import freq_per_channel, frequencies_per_area
from signal_power import psd_calculation, power_per_channel, absolute_power, \
    relative_power, power_per_area, relative_power_per_area, plotting_topographies
from signal_amplitude import amp_per_channel, amplitude_per_area


def eeg_analysis(filt_signal, name, age, laterality, group, state, index, workbook, title):
    power_psd, amp_psd, freqs, psd = psd_calculation(filt_signal)

    # Frequency calculation
    frequencies = freq_per_channel(filt_signal, power_psd, freqs)
    front_freq, central_freq, posterior_freq, right_freq, left_freq, medium_freq = frequencies_per_area(frequencies)

    # Amplitudes calculation
    amplitudes = amp_per_channel(filt_signal, amp_psd)
    front_amp, central_amp, posterior_amp, right_amp, left_amp, medium_amp = amplitude_per_area(amplitudes)

    # Power calculation
    power = power_per_channel(freqs, power_psd, filt_signal)

    # Absolute power calculation
    abs_delta, abs_theta, abs_alpha, abs_beta_1, abs_beta_2, abs_gamma, abs_power = absolute_power(power)

    # Relative power calculation
    rel_delta, rel_theta, rel_alpha, rel_beta_1, rel_beta_2, rel_gamma = relative_power(abs_delta, abs_theta, abs_alpha,
                                                                                        abs_beta_1, abs_beta_2,
                                                                                        abs_gamma,
                                                                                        abs_power)

    # Absolute power per areas calculation
    front_d, front_t, front_a, front_b_1, front_b_2, front_g, central_d, central_t, central_a, central_b_1, central_b_2, central_g, posterior_d, \
    posterior_t, posterior_a, posterior_b_1, posterior_b_2, posterior_g, right_d, right_t, right_a, right_b_1, right_b_2, right_g, left_d, left_t, \
    left_a, left_b_1, left_b_2, left_g, medium_d, medium_t, medium_a, medium_b_1, medium_b_2, medium_g, min_delta, max_delta, min_theta, max_theta, \
    min_alpha, max_alpha, min_beta1, max_beta1, min_beta2, max_beta2, min_gamma, max_gamma = power_per_area(power)

    # Relative power per areas calculation
    rel_front_d, rel_front_t, rel_front_a, rel_front_b_1, rel_front_b_2, rel_front_g, rel_central_d, \
    rel_central_t, rel_central_a, rel_central_b_1, rel_central_b_2, rel_central_g, rel_posterior_d, \
    rel_posterior_t, rel_posterior_a, rel_posterior_b_1, rel_posterior_b_2, rel_posterior_g, \
    rel_right_d, rel_right_t, rel_right_a, rel_right_b_1, rel_right_b_2, rel_right_g, rel_left_d, \
    rel_left_t, rel_left_a, rel_left_b_1, rel_left_b_2, rel_left_g, rel_medium_d, rel_medium_t, rel_medium_a, \
    rel_medium_b_1, rel_medium_b_2, rel_medium_g = relative_power_per_area(front_d, front_t, front_a, front_b_1,
                                                                           front_b_2,
                                                                           front_g, central_d, central_t, central_a,
                                                                           central_b_1,
                                                                           central_b_2, central_g, posterior_d,
                                                                           posterior_t,
                                                                           posterior_a, posterior_b_1, posterior_b_2,
                                                                           posterior_g,
                                                                           right_d, right_t, right_a, right_b_1,
                                                                           right_b_2,
                                                                           right_g, left_d, left_t, left_a, left_b_1,
                                                                           left_b_2,
                                                                           left_g, medium_d, medium_t, medium_a,
                                                                           medium_b_1,
                                                                           medium_b_2, medium_g)

    if index == 0:
        worksheet1 = workbook.add_worksheet("Joy")
        worksheet2 = workbook.add_worksheet("AbsolutePowerPerChannel_Joy")
    if index == 1:
        worksheet3 = workbook.add_worksheet("Anger")
        worksheet4 = workbook.add_worksheet("AbsolutePowerPerChannel_Anger")
    if index == 2:
        worksheet5 = workbook.add_worksheet("Fear")
        worksheet6 = workbook.add_worksheet("AbsolutePowerPerChannel_Fear")
    if index == 3:
        worksheet7 = workbook.add_worksheet("Sadness")
        worksheet8 = workbook.add_worksheet("AbsolutePowerPerChannel_Sadness")
    if index == 4:
        worksheet9 = workbook.add_worksheet("Neutral")
        worksheet10 = workbook.add_worksheet("AbsolutePowerPerChannel_Neutral")
    if index == 5:
        worksheet11 = workbook.add_worksheet("Objects")
        worksheet12 = workbook.add_worksheet("AbsolutePowerPerChannel_Objects")

    data = (['Name', name], ['Age', age], ['Laterality', laterality], ['Group', group], ['State', state],
            ['Front area frequency', front_freq], ['Central area frequency', central_freq],
            ['Posterior area frequency', posterior_freq], ['Right area frequency', right_freq],
            ['Left area frequency', left_freq], ['Medium area frequency', medium_freq],
            ['Frontal area amplitude', front_amp], ['Central area amplitude', central_amp],
            ['Posterior area amplitude', posterior_amp], ['Right area amplitude', right_amp],
            ['Left area amplitude', left_amp], ['Medium area amplitude', medium_amp],
            ['Abs Power Delta', abs_delta], ['Abs Power Theta', abs_theta], ['Abs Power Alpha', abs_alpha],
            ['Abs Power Beta 1', abs_beta_1], ['Abs Power Beta 2', abs_beta_2], ['Abs Power Gamma', abs_gamma],
            ['Abs Power Total', abs_power], ['Rel Power Delta', rel_delta], ['Rel Power Theta', rel_theta],
            ['Rel Power Alpha', rel_alpha], ['Rel Power Beta 1', rel_beta_1], ['Rel Power Beta 2', rel_beta_2],
            ['Rel Power Gamma', rel_gamma], ['Front Abs Power Delta', front_d], ['Front Abs Power Theta', front_t],
            ['Front Abs Power Alpha', front_a], ['Front Abs Power Beta 1', front_b_1],
            ['Front Abs Power Beta 2', front_b_2],
            ['Front Abs Power Gamma', front_g], ['Central Abs Power Delta', central_d],
            ['Central Abs Power Theta', central_t], ['Central Abs Power Alpha', central_a],
            ['Central Abs Power Beta 1', central_b_1], ['Central Abs Power Beta 2', central_b_2],
            ['Central Abs Power Gamma', central_g], ['Posterior Abs Power Delta', posterior_d],
            ['Posterior Abs Power Theta', posterior_t], ['Posterior Abs Power Alpha', posterior_a],
            ['Posterior Abs Power Beta 1', posterior_b_1], ['Posterior Abs Power Beta 2', posterior_b_2],
            ['Posterior Abs Power Gamma', posterior_g], ['Right Abs Power Delta', right_d],
            ['Right Abs Power Theta', right_t], ['Right Abs Power Alpha', right_a],
            ['Right Abs Power Beta 1', right_b_1],
            ['Right Abs Power Beta 2', right_b_2], ['Right Abs Power Gamma', right_g], ['Left Abs Power Delta', left_d],
            ['Left Abs Power Theta', left_t], ['Left Abs Power Alpha', left_a], ['Left Abs Power Beta 1', left_b_1],
            ['Left Abs Power Beta 2', left_b_2], ['Left Abs Power Gamma', left_g], ['Medium Abs Power Delta', medium_d],
            ['Medium Abs Power Theta', medium_t], ['Medium Abs Power Alpha', medium_a],
            ['Medium Abs Power Beta 1', medium_b_1], ['Medium Abs Power Beta 2', medium_b_2],
            ['Medium Abs Power Gamma', medium_g], ['Front Rel Power Delta', rel_front_d],
            ['Front Rel Power Theta', rel_front_t], ['Front Rel Power Alpha', rel_front_a],
            ['Front Rel Power Beta 1', rel_front_b_1], ['Front Rel Power Beta 2', rel_front_b_2],
            ['Front Rel Power Gamma', rel_front_g], ['Central Rel Power Delta', rel_central_d],
            ['Central Rel Power Theta', rel_central_t], ['Central Rel Power Alpha', rel_central_a],
            ['Central Rel Power Beta 1', rel_central_b_1], ['Central Rel Power Beta 2', rel_central_b_2],
            ['Central Rel Power Gamma', rel_central_g], ['Posterior Rel Power Delta', rel_posterior_d],
            ['Posterior Rel Power Theta', rel_posterior_t], ['Posterior Rel Power Alpha', rel_posterior_a],
            ['Posterior Rel Power Beta 1', rel_posterior_b_1], ['Posterior Rel Power Beta 2', rel_posterior_b_2],
            ['Posterior Rel Power Gamma', rel_posterior_g], ['Right Rel Power Delta', rel_right_d],
            ['Right Rel Power Theta', rel_right_t], ['Right Rel Power Alpha', rel_right_a],
            ['Right Rel Power Beta 1', rel_right_b_1], ['Right Rel Power Beta 2', rel_right_b_2],
            ['Right Rel Power Gamma', rel_right_g], ['Left Rel Power Delta', rel_left_d],
            ['Left Rel Power Theta', rel_left_t], ['Left Rel Power Alpha', rel_left_a],
            ['Left Rel Power Beta 1', rel_left_b_1], ['Left Rel Power Beta 2', rel_left_b_2],
            ['Left Rel Power Gamma 1', rel_left_g], ['Medium Rel Power Delta', rel_medium_d],
            ['Medium Rel Power Theta', rel_medium_t], ['Medium Rel Power Alpha', rel_medium_a],
            ['Medium Rel Power Beta 1', rel_medium_b_1], ['Medium Rel Power Beta 2', rel_medium_b_2],
            ['Medium Rel Power Gamma', rel_medium_g])

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    if index == 0:
        for name, score in data:
            worksheet1.write(row, col, name)
            worksheet1.write(row + 1, col, score)
            col += 1

        worksheet2.write(0, 0, 'Channel')
        worksheet2.write(0, 1, 'Delta')
        worksheet2.write(0, 2, 'Theta')
        worksheet2.write(0, 3, 'Alpha')
        worksheet2.write(0, 4, 'Beta1')
        worksheet2.write(0, 5, 'Beta2')
        worksheet2.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet2.write(index + 1, 0, power[index]['channel'])
            worksheet2.write(index + 1, 1, power[index]['abs_delta'])
            worksheet2.write(index + 1, 2, power[index]['abs_theta'])
            worksheet2.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet2.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet2.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet2.write(index + 1, 6, power[index]['abs_gamma'])

    if index == 1:
        for name, score in data:
            worksheet3.write(row, col, name)
            worksheet3.write(row + 1, col, score)
            col += 1

        worksheet4.write(0, 0, 'Channel')
        worksheet4.write(0, 1, 'Delta')
        worksheet4.write(0, 2, 'Theta')
        worksheet4.write(0, 3, 'Alpha')
        worksheet4.write(0, 4, 'Beta1')
        worksheet4.write(0, 5, 'Beta2')
        worksheet4.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet4.write(index + 1, 0, power[index]['channel'])
            worksheet4.write(index + 1, 1, power[index]['abs_delta'])
            worksheet4.write(index + 1, 2, power[index]['abs_theta'])
            worksheet4.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet4.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet4.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet4.write(index + 1, 6, power[index]['abs_gamma'])

    if index == 2:
        for name, score in data:
            worksheet5.write(row, col, name)
            worksheet5.write(row + 1, col, score)
            col += 1

        worksheet6.write(0, 0, 'Channel')
        worksheet6.write(0, 1, 'Delta')
        worksheet6.write(0, 2, 'Theta')
        worksheet6.write(0, 3, 'Alpha')
        worksheet6.write(0, 4, 'Beta1')
        worksheet6.write(0, 5, 'Beta2')
        worksheet6.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet6.write(index + 1, 0, power[index]['channel'])
            worksheet6.write(index + 1, 1, power[index]['abs_delta'])
            worksheet6.write(index + 1, 2, power[index]['abs_theta'])
            worksheet6.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet6.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet6.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet6.write(index + 1, 6, power[index]['abs_gamma'])

    if index == 3:
        for name, score in (data):
            worksheet7.write(row, col, name)
            worksheet7.write(row + 1, col, score)
            col += 1

        worksheet8.write(0, 0, 'Channel')
        worksheet8.write(0, 1, 'Delta')
        worksheet8.write(0, 2, 'Theta')
        worksheet8.write(0, 3, 'Alpha')
        worksheet8.write(0, 4, 'Beta1')
        worksheet8.write(0, 5, 'Beta2')
        worksheet8.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet8.write(index + 1, 0, power[index]['channel'])
            worksheet8.write(index + 1, 1, power[index]['abs_delta'])
            worksheet8.write(index + 1, 2, power[index]['abs_theta'])
            worksheet8.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet8.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet8.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet8.write(index + 1, 6, power[index]['abs_gamma'])

    if index == 4:
        for name, score in data:
            worksheet9.write(row, col, name)
            worksheet9.write(row + 1, col, score)
            col += 1

        worksheet10.write(0, 0, 'Channel')
        worksheet10.write(0, 1, 'Delta')
        worksheet10.write(0, 2, 'Theta')
        worksheet10.write(0, 3, 'Alpha')
        worksheet10.write(0, 4, 'Beta1')
        worksheet10.write(0, 5, 'Beta2')
        worksheet10.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet10.write(index + 1, 0, power[index]['channel'])
            worksheet10.write(index + 1, 1, power[index]['abs_delta'])
            worksheet10.write(index + 1, 2, power[index]['abs_theta'])
            worksheet10.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet10.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet10.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet10.write(index + 1, 6, power[index]['abs_gamma'])

    if index == 5:
        for name, score in data:
            worksheet11.write(row, col, name)
            worksheet11.write(row + 1, col, score)
            col += 1

        worksheet12.write(0, 0, 'Channel')
        worksheet12.write(0, 1, 'Delta')
        worksheet12.write(0, 2, 'Theta')
        worksheet12.write(0, 3, 'Alpha')
        worksheet12.write(0, 4, 'Beta1')
        worksheet12.write(0, 5, 'Beta2')
        worksheet12.write(0, 6, 'Gamma')

        for index in range(len(power)):
            worksheet12.write(index + 1, 0, power[index]['channel'])
            worksheet12.write(index + 1, 1, power[index]['abs_delta'])
            worksheet12.write(index + 1, 2, power[index]['abs_theta'])
            worksheet12.write(index + 1, 3, power[index]['abs_alpha'])
            worksheet12.write(index + 1, 4, power[index]['abs_beta_1'])
            worksheet12.write(index + 1, 5, power[index]['abs_beta_2'])
            worksheet12.write(index + 1, 6, power[index]['abs_gamma'])

        workbook.close()

    filt_signal.plot_psd(fmin=0.5, fmax=50, tmin=30, tmax=280, proj=False, picks=None, n_fft=2048, dB=False,
                         estimate='amplitude')
    filt_signal.plot_psd(fmin=0.5, fmax=50, tmin=30, tmax=280, proj=False, picks=None, n_fft=2048, dB=False,
                         estimate='power')

    plotting_topographies(power_psd, freqs, filt_signal, min_delta, max_delta, min_theta, max_theta, min_alpha,
                          max_alpha, min_beta1, max_beta1, min_beta2, max_beta2, min_gamma, max_gamma, rel_delta,
                          rel_theta, rel_alpha, rel_beta_1, rel_beta_2, rel_gamma, title)
