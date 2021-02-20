## IMU2Music: Learning to Generate Music from IMU Sensor Readings

In this project we will be exploring a way to generate music given IMU readings from a person playing an instrument.

### Project Goal

Explore different neural network architectures in the task of generating music from IMU readings present in performers' bodies.

With the advent of diverse neural network architectures for the task of processing time sequences, in the form of Recurrent Neural Networks (RNNs) and the variants that have been created since its inception, like Long Short-Term Memory (LSTM) architectures and transformers, among others, a plethora of uses have been engineered for these types of networks that go beyond classification tasks, like machine translation which convert one sequence of inputs into another, usually language-related. A further development has seen the creation of networks that translate a sequence from one sensor modality to another, which is the task we are undertaking in this project.

Previous work has dealt with translating from images to speech, as in \[[1](https://kiototeko.github.io/IMU2Music/#References)\], where an image is translated into a spoken description of it via a transformer that uses text as an intermediate modality. In contrast, in [\[2\]](https://kiototeko.github.io/IMU2Music/#References), the cross-modality is done between speech and face images, where the task is to produce a biometric system that identifies individuals based on one of this modalities. More interesting work has been that done in MIT's Computer Science and Artificial Intelligence Laboratory, where, for example, in [\[3\]](https://kiototeko.github.io/IMU2Music/#References)


## References

\[1\] Ma, S., Mcduff, D., & Song, Y. (2019, October). Unpaired Image-to-Speech Synthesis With Multimodal Information Bottleneck. 2019 IEEE/CVF International Conference on Computer Vision (ICCV). 2019 IEEE/CVF International Conference on Computer Vision (ICCV). [https://doi.org/10.1109/iccv.2019.00769 ](https://doi.org/10.1109/iccv.2019.00769)


\[2\] Arsha Nagrani, Samuel Albanie, Andrew Zisserman; Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 8427-8436. [https://openaccess.thecvf.com/content_cvpr_2018/html/Nagrani_Seeing_Voices_and_CVPR_2018_paper.html](https://openaccess.thecvf.com/content_cvpr_2018/html/Nagrani_Seeing_Voices_and_CVPR_2018_paper.html)

\[3\] Yunzhu Li, Jun-Yan Zhu, Russ Tedrake, Antonio Torralba; Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 10609-10618. [https://openaccess.thecvf.com/content_CVPR_2019/html/Li_Connecting_Touch_and_Vision_via_Cross-Modal_Prediction_CVPR_2019_paper.html](https://openaccess.thecvf.com/content_CVPR_2019/html/Li_Connecting_Touch_and_Vision_via_Cross-Modal_Prediction_CVPR_2019_paper.html)
