# Attendance-System-Face-Recognition-Based

The Attendance Management System plays a crucial role in monitoring student performance in educational institutions. Traditionally, institutes have relied on paper-based or file-based systems, while others have embraced automated attendance systems using biometric techniques. Our project focuses on implementing a Facial Recognition System, a computerized software capable of identifying and validating individuals based on their facial appearances. To accomplish this, we utilized the OpenCV and Face Recognition libraries, renowned for their face detection capabilities.

The system starts by capturing student photos and storing them in a database for training purposes. Once the training is complete, the system compares the captured face with the stored images to find a perfect match. Upon successful identification, the system generates the student's name, student ID, date, time, and attendance mark, storing the entry in a CSV file. This CSV file can be easily opened with Microsoft Excel for further analysis.

# Key Feature

- Enhanced User Interface (UI) with a bright and visually appealing background window pop-up.
- Automatic folder creation when adding a new subject, facilitating organization and management.
- Alert functionality utilizing text-to-speech technology to provide important notifications.
- Live display of date and time, ensuring accuracy and real-time monitoring.
- Fullscreen window mode upon launching, maximizing the user's viewing experience.
- Data storage to a MySQL database using PhpMyAdmin, allowing easy access and management.

# Libraries Utilized

- OpenCV
- Tkinter
- PIL
- Numpy
- Pyttsx3
- Datetime
- Time
- Pandas
- Glob
- Os
- Csv
- MySQL-python
  
# Project Flow
Upon launching the program, the following steps outline the process:
1. User Registration: Users must register their faces by entering their Student ID and Name, followed by capturing their images using the Take Image button.
2. Image Training: The system collects up to 50 images and stores them in the TrainingImage folder. Clicking the Train Image button converts these images into a numeric format for computer understanding.
3. Attendance Taking: Users can take attendance by entering the subject name and using the trained model to recognize faces. The system creates a separate .csv file for each subject, ensuring organized attendance records.
4. Database Integration: Attendance data is stored in a MySQL database, facilitating efficient data management and retrieval.
5. Attendance Viewing: By clicking the View Attendance button, users can access attendance records, which are displayed in a tabular format.
The Automated Attendance Management System revolutionizes the traditional manual attendance process, offering an efficient and accurate solution. By harnessing the power of facial recognition technology and incorporating user-friendly features, our project ensures streamlined attendance management for educational institutions.

# Register the user
![pasted image 0-11](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/bf84907e-3a3e-4de4-a634-0aae0f03c392)
![pasted image 0-13](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/edee5d34-44d5-446d-bdee-1045c6cda9f0)
![pasted image 0-14](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/40781c50-7f81-49b6-965f-648e11fa32e1)
![pasted image 0-15](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/307930d2-1a70-4572-8059-1a6c636e7bfd)
![pasted image 0-16](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/fbba6e1a-611f-44a6-bdf5-7ab143878763)

# Mark the attendance of user
![pasted image 0-17](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/439045f5-b9df-407a-ad55-9ff290064578)
![pasted image 0-18](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/b6d4bb12-2a6d-4009-a1d2-36851f9940e6)
![pasted image 0-19](https://github.com/dikidwid/Attendance-System-Face-Recognition-Based/assets/92709211/6a439606-8614-4b35-8a37-25124843ef07)


# Output the result


