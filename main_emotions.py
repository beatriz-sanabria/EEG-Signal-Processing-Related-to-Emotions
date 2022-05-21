from utils import init_eeg_emotions
import xlsxwriter
from close_open_eyes import init_marks, emotions_segment
from signal_filtering import signal_filtering
import mne
from patient_information import patient_information
from psd_calculation import eeg_analysis

routes = [""] # Route of the EEG file or files (format file: .cnt)

marks = [""] # Route of emotions marks (format file: .csv)

finalraw = {}
isGroupAnalysis = False

for idx in range(len(routes)):
    eeg = routes[idx]
    mark = marks[idx]
    events_eeg, raw, duration_bad_marks, name, laterality, group, age, state, file_name = init_eeg_emotions(
        eeg, mark)  # Call function that read the CNT file and change the annotations to events
    init_marks(events_eeg)  # Call function that recover the value of the eeg marks
    raw = raw.resample(1000)

    print(events_eeg)
    joy_segment, anger_segment, fear_segment, sadness_segment, neutral_segment, objects_segment, joy_times, anger_times,\
        fear_times, sadness_times, neutral_times, objects_times = emotions_segment(events_eeg, raw)

    filt_joy_segment = signal_filtering(joy_segment)
    filt_anger_segment = signal_filtering(anger_segment)
    filt_fear_segment = signal_filtering(fear_segment)
    filt_sadness_segment = signal_filtering(sadness_segment)
    filt_neutral_segment = signal_filtering(neutral_segment)
    filt_objects_segment = signal_filtering(objects_segment)

    if routes[0] == eeg:
        finaljoy = filt_joy_segment
        finalanger = filt_anger_segment
        finalfear = filt_fear_segment
        finalsadness = filt_sadness_segment
        finalneutral = filt_neutral_segment
        finalobjects = filt_objects_segment

    else:
        isGroupAnalysis = True
        finaljoy = mne.io.concatenate_raws([finaljoy, filt_joy_segment])
        finalanger = mne.io.concatenate_raws([finalanger, filt_anger_segment])
        finalfear = mne.io.concatenate_raws([finalfear, filt_fear_segment])
        finalsadness = mne.io.concatenate_raws([finalsadness, filt_sadness_segment])
        finalneutral = mne.io.concatenate_raws([finalneutral, filt_neutral_segment])
        finalobjects = mne.io.concatenate_raws([finalobjects, filt_objects_segment])

    final = [filt_joy_segment, filt_anger_segment, filt_fear_segment, filt_sadness_segment, filt_neutral_segment,
             filt_objects_segment]
    emotion = ['Joy', 'Anger', 'Fear', 'Sadness', 'Neutral', 'Objects']

    workbook = xlsxwriter.Workbook(file_name) # File generated with all calculations per patient

    for index in range(len(final)):
        title = emotion[index]
        eeg_analysis(final[index], name, age, laterality, group, state, index, workbook, title) #Frequency, amplitude and PSD calculation


if isGroupAnalysis:

    name, laterality, group, age, state, file_name = patient_information()
    final = [finaljoy, finalanger, finalfear, finalsadness, finalneutral, finalobjects]
    emotion = ['Joy', 'Anger', 'Fear', 'Sadness', 'Neutral', 'Objects']

    workbook = xlsxwriter.Workbook(file_name) # File generated with all calculations per group

    for index in range(len(final)):
        eeg_analysis(final[index], name, age, laterality, group, state, index, workbook, emotion[index]) #Frequency, amplitude and PSD calculation
