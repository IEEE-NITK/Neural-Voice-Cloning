# Neural-Voice-Cloning
Neural Voice Cloning with a few voice samples, using the speaker adaptation method. Speaker adaptation is based on fine-tuning a multi-speaker generative model with a few cloning samples. 

**Team Members:**
* Adil Ashique
* Govardhan GD 
* Prajwal S Belagavi
* Rosa Anil George

**Instructions to execute the model.**
1. Clone the deep voice 3 repository.
2. Download the pre-trained model from https://www.dropbox.com/s/uzmtzgcedyu531k/20171222_deepvoice3_vctk108_checkpoint_step000300000.pth?dl=0 and save it in the deep voice 3 reposiroty.
3. Do 'git checkout 0421749'
4. To the cloned repo, add the folders and files that are present in the folder 'back'. Replace the synthesis.py in deep voice 3 file with the one in this repository.
4. The sentences to be converted to speech must be entered in the sentences.txt file.
5. The input audio is to be stored in the audio folder as 'in.wav'. This can be modified and if modified change the synthesis.py file accordingly.

# Acknowledgements

- The implementation of Multi-Speaker Generative model was inspired from https://github.com/r9y9/deepvoice3_pytorch

- [Neural Voice Cloning with Few Samples](https://arxiv.org/pdf/1802.06006)
