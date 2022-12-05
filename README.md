# Containerized Web App

![Machine Learning build & test](https://github.com/software-students-fall2022/containerized-app-exercise-team9/actions/workflows/machine-learning.yml/badge.svg)

![Web App build & test](https://github.com/software-students-fall2022/containerized-app-exercise-team9/actions/workflows/web-app.yml/badge.svg)

## Project Description

Machine Learning Client: An online transcriber where the user is given a quote which they have to read out loud. The machine learning client records audio input from the user's microphone while reading this quote.

Web App: Contains the results of user's recording with various statistics such as total words spoken, accuracy, and correct words spoken, etc.

## How to run

To run this application, first run:

``` bash
docker compose up
```

This project has two web applications. One will be running on port 8080 and the other one in port 5001.

First, open the application in port 8080 and follow the steps to record the audio message. After that, open the second application on port 5001 to see the statistic analysis about the audio transcription that you just submitted.

### Web application instructions

In order for the machine learning application to record your audio message properly, you have to give the application permission to use your microphone. After doing that, press "Record" and read the random quote that was generated in the grey box. After finishing the recording, press "Stop". You are able to listen to your recording by clicking the audio controls. If you are happy with your recording, press "Download" to save your recording into your machine. Then, submit this recording into the submission field in the application and press "Submit query". You are now able to see the statistics of your audio in the application on port 5001.

## Team members

Pedro Baggio ([Jignifs](https://github.com/Jignifs))

Eduarda Martini ([ezmartini](https://github.com/ezmartini))

Laura Lourenco ([qlaueen](https://github.com/qlaueen))

Manny Soto Ruiz ([MannySotoRuiz](https://github.com/MannySotoRuiz))

Amaan Khwaja ([AmaanmKhwaja](https://github.com/Amaanmkhwaja))

Michelle Lu ([michellelu8](https://github.com/michellelu8))
