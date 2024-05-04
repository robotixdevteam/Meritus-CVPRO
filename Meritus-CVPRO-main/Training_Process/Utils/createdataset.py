"""
CVPRO v1.0.0. 
Code Developed by Augustin Rajkumar, Suresh Balaji, E.V.V Thrilok kumar, and Meritus R & D Team - August 31, 2023.
Copyright © 2023 Meritus R & D Team. All rights reserved.
This program is the intellectual property of Meritus AI, and may not be distributed 
or reproduced without explicit authorization from the copyright holder.
-------------------------------------------------------------------------------------------------------------------
This script has the code for processing the Dataset.
"""

# Import Packages
import os
import time
import csv
import cv2
import pandas as pd
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

class CreateDataset:
    """
    This class depicts the function for converting raw data to processed dataset 
    """
    def __init__(self):
        """
        Initialize
        """
        self.missing_file = "MissingFile.log"
        self.root_folder, self.log_file_path = self.main_folder()
        print("Training Progress is Started....")

    def main_folder(self):
        """
        Change the directory to the root folder and create the log file for missing elements
        """
        root_path = 'Training_Data/Dataset_CVPRO'# root-path of Datasets
        root_folder = os.path.join(os.getcwd(), root_path) # root_folder
        log_file_path = os.path.join(root_path.split("/", maxsplit=1)[0], self.missing_file)
        # print("Log File Path:", log_file_path)
        if not os.path.exists(log_file_path):
            with open(log_file_path,'w', encoding='utf-8') as file:
                file.write("**** This File contains the error message of Missing File ****\n")
        return root_folder, log_file_path

    def path_folders(self):
        """
        Rooting the current working directory to "Videos" and "Files"
        """
        folder_list = []
        for dataset_folder in os.listdir(self.root_folder):
            dataset_folder_path = os.path.join(self.root_folder, dataset_folder)
            # print("Dataset_Folder :", dataset_folder_path)
            if os.path.isdir(dataset_folder_path):
                print("Dataset_Folder :", dataset_folder_path)
                for list_folder in os.listdir(dataset_folder_path):
                    list_folder_path = os.path.join(dataset_folder_path, list_folder)
                    # print("List_Folder :", list_folder_path)
                    if os.path.isdir(list_folder_path):
                        for folder in os.listdir(list_folder_path):
                            inside_folder_path = os.path.join(list_folder_path, folder)
                            # print("Inside_Folder_Path :", inside_folder_path)
                            if os.path.isdir(inside_folder_path):
                                folder_list.append(inside_folder_path)
                            else:
                                print("Inside Folder is not Folder")
                    else:
                        print("The Folder is not Present in List_Folder")
            else:
                print("No! Folder is not present.")
        return folder_list

    def video_to_image(self, folder_list):
        """
        Convert video (appeared as timestamp format) to image (.jpg)
        """
        no_errors = True  # Flag to track if any errors occurred

        for list_folders in tqdm(range(len(folder_list))):
            folder_dir = folder_list[list_folders]
            print(f"Status : Current Directory -> {folder_dir}")
            # Checking whether Files folder is missing or not
            files_dir = os.path.join(folder_dir, 'Files')
            if not os.path.exists(files_dir):
                print(f"Status : WARNING ! \nFiles Directory missing for : {folder_dir}")
                with open('MissingFile.log', 'a', encoding='utf-8') as missingfile:
                    missingfile.write(str(f'Files directory missing for : {folder_dir}\n'))
                time.sleep(2)
                continue

            csv_file = [file for file in os.listdir(files_dir) if file.endswith('.csv')]

            # Checking whether Videos Folder is missing or not
            videos_dir = os.path.join(folder_dir, 'Videos')
            if not os.path.exists(videos_dir):
                print(f"Status : WARNING ! \nVideos directory missing for : {folder_dir}")
                with open('MissingFile.log', 'a', encoding='utf-8') as missingfile:
                    missingfile.write(str(f'Videos directory missing for : {folder_dir}\n'))
                time.sleep(2)
                continue

            video_file = [file for file in os.listdir(videos_dir) if file.endswith('.mp4')]

            # Checking if .csv or .mp4 file is missing
            if len(csv_file) == 0 or len(video_file) == 0:
                if len(csv_file) == 0:
                    print(f"Status : WARNING ! \nCSV missing for : {folder_dir}")
                    with open('MissingFile.log', 'a', encoding='utf-8') as missingfile:
                        missingfile.write(str(f'CSV missing for : {folder_dir}\n'))
                    time.sleep(2)
                elif len(video_file) == 0:
                    print(f"Status : WARNING ! \nVideo missing for : {folder_dir}")
                    with open('MissingFile.log', 'a', encoding='utf-8') as missingfile:
                        missingfile.write(str(f'Video missing for : {folder_dir}\n'))
                    time.sleep(2)
                continue

            elif len(csv_file) > 0 and len(video_file) > 0:
                case_1 = False
                csv_content_list = []
                with open(os.path.join(files_dir, csv_file[0]), 'r', encoding='utf-8') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                        csv_content_list.append(row)

                csv_length = len(csv_content_list)
                print("CSV_Length : ",csv_length)

                # Finding the total frame count
                video_path = os.path.join(videos_dir, video_file[0])
                cap = cv2.VideoCapture(video_path)
                property_id = int(cv2.CAP_PROP_FRAME_COUNT)
                video_length = int(cv2.VideoCapture.get(cap, property_id))
                print("Video length : ",video_length)

                # csv processing
                for i in range(csv_length):
                    current_name = csv_content_list[i][0]
                # comparing csv length and video frame length
                iteration_stopper = 0
                if csv_length > video_length:
                    case_1 = True
                    iteration_stopper = video_length
                    print(f"The CSV length - {csv_length} is greater, so limiting no. of frames to video frame length count - {video_length}\n")
                elif video_length > csv_length:
                    iteration_stopper = csv_length
                    print(f"The Video frame length - {video_length} is greater, so limiting no. of frames to csv length count - {csv_length}\n")
                # Save the output Image and CSV in New Folder Directory
                output_dir = os.path.join(folder_dir, 'Process_Image')
                output_csv_dir = os.path.join(folder_dir, 'Controls_CSV')
                os.makedirs(output_dir, exist_ok=True)
                os.makedirs(output_csv_dir, exist_ok=True)

                column_split = 0
                print("Status : Writing images and csv to output folder ...\n")
                for k in range(iteration_stopper):
                    file_name_path = csv_content_list[column_split][0]
                    first_value = csv_content_list[column_split][1]
                    second_value = csv_content_list[column_split][2]
                    split1 = file_name_path.split('/')
                    target_name = split1[len(split1) - 1]
                    # Reading the video and convert into frames
                    ret, frame = cap.read()
                    # frame = cv2.flip(frame, 0)
                    cv2.imwrite(os.path.join(output_dir, target_name), frame)
                    # update the input csv file and write it to output-csv folder
                    out_file = open(os.path.join(output_csv_dir, 'Frame.csv'), 'a', encoding='utf-8')
                    out_file.write(f"{file_name_path},{first_value},{second_value}\n")
                    out_file.close()
                    column_split += 1

                    split_folder_name = folder_dir.split('/')
                    inner_folder_name = split_folder_name[len(split_folder_name) - 1]
                print(f"\nStatus : Completed writing outputs ! for {inner_folder_name}\n")

        if no_errors:
            with open(self.log_file_path, 'a', encoding='utf-8') as missingfile:
                missingfile.write("No, Error occurred during processing.\n")
        print("Data Pre-Processing Completed ")

    def appending_csv(self, csv_path, path):
        """
        Appending the CSV from folders to a new csv files
        """
        try:
            data = pd.read_csv(csv_path)
            if data.shape[1] == 3:
                csv_data = pd.read_csv(csv_path, header=None, names=["Image_Path", "Left", "Right"], na_values=[""])
                csv_data.dropna(subset=["Image_Path", "Left", "Right"], inplace=True)
                csv_data = csv_data.astype({"Left": int, "Right": int})
                csv_data["Label"] = csv_data[["Left", "Right"]].apply(lambda row: ",".join(row.values.astype(str)), axis=1)
                csv_data = csv_data[csv_data.Label != "0,0"]
                # csv_data = csv_data[csv_data.Label != "-210,-210"]
                csv_data = csv_data[~csv_data["Label"].str.contains("-\d+,-\d+")]
            elif data.shape[1] == 2:
                csv_data = pd.read_csv(csv_path, header=None, names=["Image_Path", "Label"], na_values=[""])
                csv_data.dropna(subset=["Image_Path", "Label"], inplace=True)
            else:
                print("Invalid CSV format. Expected either 2 or 3 columns.")
            csv_data["Image_Path"] = csv_data["Image_Path"].apply(lambda x: os.path.join(path, x))
            return csv_data
        except pd.errors.EmptyDataError:
            print(f"File {csv_path} is empty.")
            return pd.DataFrame()

    def image_classify(self,folder_path, dataset_folder, save_df):
        """
        Image-Classification 
        """
        full_path = os.path.join(folder_path, dataset_folder)
        # print(f"Full path: {full_path}")
        for actual_dataset in os.listdir(full_path):
            actual_dataset_path = os.path.join(full_path, actual_dataset)
            # print(f"Actual-Dataset Path:{actual_dataset_path}")
            for dataset_folder in os.listdir(actual_dataset_path):
                dataset_path = os.path.join(actual_dataset_path, dataset_folder)
                # print(f"Dataset_Folder:{dataset_path}")
                folder_path = os.path.join(dataset_path, 'Controls_CSV/', "Frame.csv")
                print(f"Folder_Path:{folder_path}")
                try:
                    csv_data = self.appending_csv(folder_path, actual_dataset_path)
                    save_df.append(csv_data)
                except Exception as csv_error:
                    print(f"Error processing CSV: {folder_path}")
                    print(f"Error message: {str(csv_error)}")
        # pass

    def autonomous_driving(self, folder_path, dataset_folder, save_df):
        """
        Autonomous-Driving
        """
        full_path = os.path.join(folder_path, dataset_folder)
        # print(f"Full path: {full_path}")
        for actual_dataset in os.listdir(full_path):
            actual_dataset_path = os.path.join(full_path, actual_dataset)
            # print(f"Actual-Dataset Path:{actual_dataset_path}")
            for dataset_folder in os.listdir(actual_dataset_path):
                dataset_path = os.path.join(actual_dataset_path, dataset_folder)
                # print(f"Dataset_Folder:{dataset_path}")
                folder_path = os.path.join(dataset_path, 'Controls_CSV/', "Frame.csv")
                print(f"Folder_Path:{folder_path}")
                try:
                    csv_data = self.appending_csv(folder_path, actual_dataset_path)
                    save_df.append(csv_data)
                except Exception as csv_error:
                    print(f"Error processing CSV: {folder_path}")
                    print(f"Error message: {str(csv_error)}")

    # main function for list-of-folders
    def data_frame(self):
        """
        Save Dataframe in list
        """
        save_df = []
        for folder in os.listdir(self.root_folder):
            print(folder)
            if folder == "Image_Classification":
                self.image_classify(self.root_folder, folder, save_df)
            elif folder == "Autonomous_Driving":
                self.autonomous_driving(self.root_folder, folder, save_df)
        return save_df

    def list_to_dataframe(self, save_df):
        """
        To save the list to dataframe of csv
        """
        save_dataframe = pd.concat(save_df)
        shuffled = shuffle(save_dataframe, random_state=42)
        dataframe_path = os.path.join(os.path.dirname(self.root_folder), "cvpro.csv")
        try:
            if os.path.exists(dataframe_path) and os.path.isfile(dataframe_path):
                os.remove(dataframe_path)
                print("Already, CSV File delete and create a new CSV file")
                print(f"dataframe path: {dataframe_path}")
                # shuffled['Image_Path'] = shuffled['Image_Path'].replace('Videos', 'Process_Image')
                shuffled['Image_Path'] = shuffled['Image_Path'].apply(lambda x: x.replace('Videos', 'Process_Image'))
                shuffled.to_csv(dataframe_path, index=False)
            else:
                print("The CSV File not found. Please, Continue.... ")
                print(f"dataframe path: {dataframe_path}")
                # shuffled['Image_Path'] = shuffled['Image_Path'].replace('Videos', 'Process_Image')
                shuffled['Image_Path'] = shuffled['Image_Path'].apply(lambda x: x.replace('Videos', 'Process_Image'))
                shuffled.to_csv(dataframe_path, index=False)
            return dataframe_path
        except Exception as dataframe_error:
            print(f"Error saving dataframe: {str(dataframe_error)}")
            return None

    def random_images(self, csv_path):
        """
        Show the random_images and its respective control_values
        """
        data = pd.read_csv(csv_path)
        selected_images = data.sample(n=9) #num-images is 9 (default, we fixed)
        # plt.figure(1)
        fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
        axes = axes.flatten()
        for i, (_, row) in enumerate(selected_images.iterrows()):
            image_path = row["Image_Path"]
            label = row["Label"]
            image = Image.open(image_path)
            axes[i].imshow(image)
            axes[i].set_title(label)
            axes[i].axis("off")
        plt.savefig(os.path.join(os.path.dirname(self.root_folder), 'Random_Images_Labels.png'))
        plt.show()
