## IMU2Music: Learning to Generate Music from IMU Sensor Readings

In this project we will be exploring a way to generate music given IMU readings from a person playing an instrument.

### Project Goal

Explore different neural network architectures in the task of generating music from IMU readings present in performers' bodies.

With the advent of diverse neural network architectures for the task of processing time sequences, in the form of Recurrent Neural Networks (RNNs) and the variants that have been created since its inception, like Long Short-Term Memory (LSTM) architectures and transformers, among others, a plethora of uses have been engineered for these types of networks that go beyond classification tasks, like machine translation which convert one sequence of inputs into another, usually language-related. A further development has seen the creation of networks that translate a sequence from one sensor modality to another, which is the task we are undertaking in this project.

Previous work has dealt with translating from images to speech, as in \[[1](#references)\], where an image is translated into a spoken description of it via a transformer that uses text as an intermediate modality or translating video to sound, like in \[[5](https://kiototeko.github.io/IMU2Music/#References)\], where for videos with natural occurrences a sound is produced using an RNN. In contrast, in \[[2](https://kiototeko.github.io/IMU2Music/#References)\], the cross-modality is done between speech and face images, where the task is to produce a biometric system that identifies individuals based on one of this modalities. More interesting work has been that done in MIT's Computer Science and Artificial Intelligence Laboratory, where, for example, in \[[3](https://kiototeko.github.io/IMU2Music/#References)\], given a robot arm equipped with a touch sensor and a camera recording the robot arm's motion, a bidirectional correspondence between these modalities is established by using conditional GANs. More related to our current task, in \[[4](https://kiototeko.github.io/IMU2Music/#References)\] they are able to translate video recordings of musicians performing into the actual sound one would expect hearing, by means of a transformer. Finally, we have work like in \[[6](https://kiototeko.github.io/IMU2Music/#References)\] where the objective is to translate an audio recording of a musician performing into an animation of it, with the body dynamics included. This could be thought as the inverse of the task we are exploring in this work, whereas in here they use an LSTM network trained on videos, where keypoints are extracted from the bodies shown. Our work instead uses only IMU readings and tries to translate those into the respective audio recording.

### Technical Approach

The approach followed in here

#### Obtaining the dataset



Given the tiny amount of data available to train a model using both IMU sensors and audio of musicians performing, an interesting future direction could deal with generating the IMU readings directly from videos of musicians so as to surpass this problem. In fact, in \[[7](https://kiototeko.github.io/IMU2Music/#References)\] they do exactly that, although for the purpose of human activity recognition, where they test both an LSTM and a Random Forest model. Unfortunately, their code is not open to the public so we are not able to test it for now.

## References

\[1\] Ma, S., Mcduff, D., & Song, Y. (2019, October). Unpaired Image-to-Speech Synthesis With Multimodal Information Bottleneck. 2019 IEEE/CVF International Conference on Computer Vision (ICCV). 2019 IEEE/CVF International Conference on Computer Vision (ICCV). [https://doi.org/10.1109/iccv.2019.00769 ](https://doi.org/10.1109/iccv.2019.00769)


\[2\] Arsha Nagrani, Samuel Albanie, Andrew Zisserman. Seeing Voices and Hearing Faces: Cross-Modal Biometric Matching (2018). Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 8427-8436. [https://openaccess.thecvf.com/content_cvpr_2018/html/Nagrani_Seeing_Voices_and_CVPR_2018_paper.html](https://openaccess.thecvf.com/content_cvpr_2018/html/Nagrani_Seeing_Voices_and_CVPR_2018_paper.html)

\[3\] Yunzhu Li, Jun-Yan Zhu, Russ Tedrake, Antonio Torralba. Connecting Touch and Vision via Cross-Modal Prediction (2019). Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 10609-10618. [https://openaccess.thecvf.com/content_CVPR_2019/html/Li_Connecting_Touch_and_Vision_via_Cross-Modal_Prediction_CVPR_2019_paper.html](https://openaccess.thecvf.com/content_CVPR_2019/html/Li_Connecting_Touch_and_Vision_via_Cross-Modal_Prediction_CVPR_2019_paper.html)

\[4\] Chuang Gan and Deng Huang and Peihao Chen and Joshua B. Tenenbaum and Antonio Torralba (2020). Foley Music: Learning to Generate Music from Videos. [https://arxiv.org/abs/2007.10984](https://arxiv.org/abs/2007.10984)

\[5\] Yipin Zhou, Zhaowen Wang, Chen Fang, Trung Bui, Tamara L. Berg (2018). Visual to Sound: Generating Natural Sound for Videos in the Wild. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 3550-3558. [https://openaccess.thecvf.com/content_cvpr_2018/html/Zhou_Visual_to_Sound_CVPR_2018_paper.html](https://openaccess.thecvf.com/content_cvpr_2018/html/Zhou_Visual_to_Sound_CVPR_2018_paper.html)

\[6\] Eli Shlizerman, Lucio Dery, Hayden Schoen, Ira Kemelmacher-Shlizerman (2018). Audio to Body Dynamics. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 7574-7583. [https://openaccess.thecvf.com/content_cvpr_2018/html/Shlizerman_Audio_to_Body_CVPR_2018_paper.html](https://openaccess.thecvf.com/content_cvpr_2018/html/Shlizerman_Audio_to_Body_CVPR_2018_paper.html)

\[7\] Kwon, H., Tong, C., Haresamudram, H., Gao, Y., Abowd, G. D., Lane, N. D., & Plötz, T. (2020). IMUTube. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 4(3), 1–29. [https://doi.org/10.1145/3411841](https://doi.org/10.1145/3411841)
