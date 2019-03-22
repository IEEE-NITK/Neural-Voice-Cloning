from docopt import docopt

import sys
from os.path import dirname, join
from tqdm import tqdm, trange
from datetime import datetime

# The deepvoice3 model
from dv3.deepvoice3_pytorch import frontend, builder
import dv3.audio
import dv3.lrschedule

import torch
from torch.utils import data as data_utils
from torch.autograd import Variable
from torch import nn
from torch import optim
import torch.backends.cudnn as cudnn
from torch.utils import data as data_utils
from torch.utils.data.sampler import Sampler
import numpy as np
from numba import jit

from nnmnkwii.datasets import FileSourceDataset, FileDataSource
from os.path import join, expanduser
import random

import librosa.display
from matplotlib import pyplot as plt
import sys
import os
from tensorboardX import SummaryWriter
from matplotlib import cm
from warnings import warn
from dv3.hparams import hparams, hparams_debug_string

def save_alignment(path, attn):
    plot_alignment(attn.T, path, info="{}, {}, step={}".format(
        hparams.builder, time_string(), global_step))


def eval_model(global_step, writer, model, checkpoint_dir, ismultispeaker):
    # harded coded
    texts = [
        "Scientists at the CERN laboratory say they have discovered a new particle.",
        "There's a way to measure the acute emotional intelligence that has never gone out of style.",
        "President Trump met with other leaders at the Group of 20 conference.",
        "Generative adversarial network or variational auto-encoder.",
        "Please call Stella.",
        "Some have accepted this as a miracle without any physical explanation.",
    ]
    import dv3.synthesis as synthesis
    synthesis._frontend = _frontend

    eval_output_dir = join(checkpoint_dir, "eval")
    os.makedirs(eval_output_dir, exist_ok=True)

    # hard coded
    speaker_ids = [0, 1, 10] if ismultispeaker else [None]
    for speaker_id in speaker_ids:
        speaker_str = "multispeaker{}".format(speaker_id) if speaker_id is not None else "single"

        for idx, text in enumerate(texts):
            signal, alignment, _, mel = synthesis.tts(
                model, text, p=0, speaker_id=speaker_id, fast=False)
            signal /= np.max(np.abs(signal))

            # Alignment
            path = join(eval_output_dir, "step{:09d}_text{}_{}_alignment.png".format(
                global_step, idx, speaker_str))
            save_alignment(path, alignment)
            tag = "eval_averaged_alignment_{}_{}".format(idx, speaker_str)
            #writer.add_image(tag, np.uint8(cm.viridis(np.flip(alignment, 1).T) * 255), global_step)

            # Mel
            #writer.add_image("(Eval) Predicted mel spectrogram text{}_{}".format(idx, speaker_str),
                             # prepare_spec_image(mel), global_step)

            # Audio
            path = join(eval_output_dir, "step{:09d}_text{}_{}_predicted.wav".format(
                global_step, idx, speaker_str))
            dv3.audio.save_wav(signal, path)

            try:
                #writer.add_audio("(Eval) Predicted audio signal {}_{}".format(idx, speaker_str),
                #                 signal, global_step, sample_rate=fs)
			pass
            except Exception as e:
                warn(str(e))
                pass

log_event_path=None
if log_event_path is None:
        log_event_path = "log/run-test" + str(datetime.now()).replace(" ", "_")
    print("Los event path: {}".format(log_event_path))
    writer = SummaryWriter(log_dir=log_event_path)
