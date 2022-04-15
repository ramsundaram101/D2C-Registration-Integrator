# D2C-Registration-Integrator
This automatically converts the D2C registration sheet into the format of the ICC Mastersheet

## Intructions ##

First, clone this repository

`git clone https://github.com/ramsundaram101/D2C-Registration-Integrator`

Then, open Command Prompt and run the following

`python python [folder path to the cloned repo]/D2C.py --last_team_id=[Last Team ID visible on the Mastersheet] --csv_folder=[folder path to csv registration file]`

### Example ###

`python C:\Users\D2C.py --last_team_id=MYQ9995 --csv_folder=C:\Users\1b7e71fb2b9ca72e63eebd84d021e8fd62584a0ca3ff4-registration.csv`


The sample Before and After files show how the script works

The D2C Sheet (Before)
![image](https://user-images.githubusercontent.com/87599801/163529350-9989f460-2478-4864-b316-4d51be65c1c8.png)


MasterSheet Format (After)
![image](https://user-images.githubusercontent.com/87599801/163529509-35ee57fc-460d-493b-9149-8697989c91e8.png)

